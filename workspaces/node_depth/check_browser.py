import subprocess,tempfile,time,json,requests,websocket,base64,shutil
from pathlib import Path
root=Path(__file__).resolve().parent;profile=Path(tempfile.mkdtemp(prefix='node-depth-qa-'));log=open('/tmp/node-depth-browser.log','w');proc=subprocess.Popen(['google-chrome','--headless','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--no-first-run','--no-default-browser-check','--allow-file-access-from-files','--remote-debugging-port=0','--remote-allow-origins=*','--host-resolver-rules=MAP * ~NOTFOUND',f'--user-data-dir={profile}','about:blank'],stdout=log,stderr=log);ws=None
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
  if ev("document.readyState==='complete' && document.querySelectorAll('.document').length>0"):break
  time.sleep(.1)
 ev("document.querySelectorAll('img').forEach(x=>x.loading='eager');true")
 for _ in range(100):
  if ev('[...document.images].every(x=>x.complete&&x.naturalWidth>0)'):break
  time.sleep(.1)
 report={'documents':ev("document.querySelectorAll('.document').length"),'desktop_overflow':ev('document.documentElement.scrollWidth>innerWidth'),'images':ev('document.images.length'),'images_loaded':ev('[...document.images].every(x=>x.complete&&x.naturalWidth>0)')}
 b=call('Page.captureScreenshot',{'format':'png'})['data'];Path('/tmp/node-depth-desktop.png').write_bytes(base64.b64decode(b))
 ev("document.querySelector('.document').open=false;true");report['collapse']=ev("!document.querySelector('.document').open")
 ev("document.querySelector('.document').open=true;true");report['expand']=ev("document.querySelector('.document').open")
 call('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True});ev('scrollTo(0,0);true');report['mobile_overflow']=ev('document.documentElement.scrollWidth>innerWidth');b=call('Page.captureScreenshot',{'format':'png'})['data'];Path('/tmp/node-depth-mobile.png').write_bytes(base64.b64decode(b))
 call('Emulation.setDeviceMetricsOverride',{'width':1440,'height':1100,'deviceScaleFactor':1,'mobile':False})
 ev("location.hash='draft-3--h02';true")
 time.sleep(.2)
 report['source_anchor_opens_card']=ev("document.getElementById('draft-3').open && document.getElementById('draft-3--h02').getBoundingClientRect().top>=-2 && document.getElementById('draft-3--h02').getBoundingClientRect().top<innerHeight")
 report['js_errors']=[e for e in events if e.get('method')=='Runtime.exceptionThrown'];report['passed']=(report['documents']==5 and report['source_anchor_opens_card'] and report['images_loaded'] and report['collapse'] and report['expand'] and not report['desktop_overflow'] and not report['mobile_overflow'] and not report['js_errors'])
 (root/'browser_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
finally:
 if ws:ws.close()
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill();proc.wait()
 log.close();shutil.rmtree(profile,ignore_errors=True)
