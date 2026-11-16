import subprocess,tempfile,time,json,requests,websocket,base64,shutil
from pathlib import Path
root=Path(__file__).resolve().parent;profile=Path(tempfile.mkdtemp(prefix='single-report-qa-'));log=open('/tmp/single-report-browser.log','w');proc=subprocess.Popen(['google-chrome','--headless','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--no-first-run','--no-default-browser-check','--allow-file-access-from-files','--remote-debugging-port=0','--remote-allow-origins=*','--host-resolver-rules=MAP * ~NOTFOUND',f'--user-data-dir={profile}','about:blank'],stdout=log,stderr=log);ws=None
try:
 for _ in range(100):
  if (profile/'DevToolsActivePort').exists():break
  time.sleep(.1)
 port=(profile/'DevToolsActivePort').read_text().splitlines()[0];pages=requests.get(f'http://127.0.0.1:{port}/json/list').json();ws=websocket.create_connection(next(p['webSocketDebuggerUrl']for p in pages if p['type']=='page'),timeout=20);counter=0;events=[]
 def call(method,params=None):
  global counter
  counter+=1;i=counter;ws.send(json.dumps({'id':i,'method':method,'params':params or {}}))
  while True:
   m=json.loads(ws.recv())
   if m.get('id')==i:
    if 'error'in m:raise RuntimeError(m)
    return m.get('result',{})
   events.append(m)
 def ev(expr):return call('Runtime.evaluate',{'expression':expr,'returnByValue':True,'awaitPromise':True})['result'].get('value')
 call('Page.enable');call('Runtime.enable');call('Network.enable');call('Network.setBlockedURLs',{'urls':['http://*','https://*']});call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False});call('Page.navigate',{'url':(root/'报告.html').as_uri()})
 for _ in range(100):
  if ev("document.readyState==='complete' && document.querySelectorAll('.agent').length>0"):break
  time.sleep(.1)
 report={'knowledge_entries':ev("document.querySelectorAll('.agent').length"),'desktop_overflow':ev('document.documentElement.scrollWidth>innerWidth')}
 b=call('Page.captureScreenshot',{'format':'png'})['data'];Path('/tmp/single-report-desktop.png').write_bytes(base64.b64decode(b))
 ev("document.getElementById('open').click();true");report['open_all']=ev("[...document.querySelectorAll('.agent')].every(x=>x.open)")
 ev("document.getElementById('close').click();true");report['close_all']=ev("[...document.querySelectorAll('.agent')].every(x=>!x.open)")
 ev("document.querySelector('a[href=\"#korea-concepts-0\"]').click();true");report['sox_anchor_opens']=ev("document.getElementById('korea-concepts-0').open")
 report['sox_text']=ev("document.getElementById('korea-concepts-0').innerText.includes('SOX')")
 call('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True});ev('scrollTo(0,0);true');report['mobile_overflow']=ev('document.documentElement.scrollWidth>innerWidth');b=call('Page.captureScreenshot',{'format':'png'})['data'];Path('/tmp/single-report-mobile.png').write_bytes(base64.b64decode(b))
 report['js_errors']=[e for e in events if e.get('method')=='Runtime.exceptionThrown'];report['passed']=(report['knowledge_entries']==55 and report['open_all'] and report['close_all'] and report['sox_anchor_opens'] and report['sox_text'] and not report['desktop_overflow'] and not report['mobile_overflow'] and not report['js_errors'])
 (root/'browser_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
finally:
 if ws:ws.close()
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill();proc.wait()
 log.close();shutil.rmtree(profile,ignore_errors=True)
