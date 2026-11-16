import subprocess,tempfile,time,json,requests,websocket,base64,shutil
from pathlib import Path
root=Path(__file__).resolve().parent;profile=Path(tempfile.mkdtemp(prefix='article-report-qa-'));log=open('/tmp/article-report-browser.log','w');proc=subprocess.Popen(['google-chrome','--headless','--no-sandbox','--disable-gpu','--disable-dev-shm-usage','--no-first-run','--no-default-browser-check','--allow-file-access-from-files','--remote-debugging-port=0','--remote-allow-origins=*','--host-resolver-rules=MAP * ~NOTFOUND',f'--user-data-dir={profile}','about:blank'],stdout=log,stderr=log);ws=None
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
 report={'all_cards':ev("document.querySelectorAll('.agent').length"),'desktop_overflow':ev('document.documentElement.scrollWidth>innerWidth')}
 b=call('Page.captureScreenshot',{'format':'png'})['data'];Path('/tmp/article-report-desktop.png').write_bytes(base64.b64decode(b))
 ev("document.querySelector('[data-filter=korea]').click();true");report['korea_visible']=ev("[...document.querySelectorAll('.agent')].filter(x=>!x.hidden).length")
 ev("document.querySelector('[data-filter=ai]').click();true");report['ai_visible']=ev("[...document.querySelectorAll('.agent')].filter(x=>!x.hidden).length")
 ev("document.getElementById('search').value='ai_01';document.getElementById('search').dispatchEvent(new Event('input'));true");report['search_visible']=ev("[...document.querySelectorAll('.agent')].filter(x=>!x.hidden).map(x=>x.id)")
 ev("document.querySelector('[data-filter=all]').click();document.getElementById('search').value='';document.getElementById('search').dispatchEvent(new Event('input'));document.querySelector('a[href=\"#ai_01\"]').click();true");report['anchor_opens_card']=ev("document.getElementById('ai_01').open")
 report['images']=ev("[...document.images].map(x=>({src:x.getAttribute('src'),loaded:x.complete&&x.naturalWidth>0}))")
 call('Emulation.setDeviceMetricsOverride',{'width':390,'height':844,'deviceScaleFactor':1,'mobile':True});ev('scrollTo(0,0);true');report['mobile_overflow']=ev('document.documentElement.scrollWidth>innerWidth');b=call('Page.captureScreenshot',{'format':'png'})['data'];Path('/tmp/article-report-mobile.png').write_bytes(base64.b64decode(b))
 report['js_errors']=[e for e in events if e.get('method')=='Runtime.exceptionThrown'];report['passed']=(report['all_cards']==12 and report['ai_visible']==6 and report['korea_visible']==6 and report['search_visible']==['ai_01'] and report['anchor_opens_card'] and not report['desktop_overflow'] and not report['mobile_overflow'] and not report['js_errors'] and all(x['loaded']for x in report['images']))
 (root/'browser_check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False,indent=2))
finally:
 if ws:ws.close()
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill();proc.wait()
 log.close();shutil.rmtree(profile,ignore_errors=True)
