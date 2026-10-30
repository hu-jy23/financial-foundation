"""Publish catalog progress only for completed main reviews; never edits economic prose.

Creates a selective local commit and UTF-8 GitHub tree upload chunks in scratch.
Remote ref update is performed separately with a checked expected head.
"""
import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml
from filename_migration import markdown_target, current_input_hash

ap = argparse.ArgumentParser()
ap.add_argument('--output', required=True)
ap.add_argument('--commit', action='store_true')
args = ap.parse_args()
out = Path(__file__).resolve().parent
root = out.parent.parent
repo = root.parent
read = lambda p: json.loads(p.read_text())
dump = lambda x: json.dumps(x, ensure_ascii=False, indent=2) + '\n'
git = lambda *a: subprocess.check_output(['git', *a], cwd=repo).decode().strip()
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
reviews = read(out / 'MAIN_REVIEW.json')['entries']
paths = read(out / 'PATHS.json')
state = read(out / 'RUN_STATE.json')
resume = read(out / 'CONTINUATION_20261030.json')
previous = set(resume.get('committed_ids', []))
last = resume['checkpoints'][-1] if resume['checkpoints'] else None
if last and not last.get('local_commit'):
    previous -= set(last['ids'])
new_ids = [n for n in resume['remaining_ids'] if n in reviews and n not in previous]
assert len(new_ids) == 10 or (len(new_ids) < 10 and set(resume['remaining_ids']) <= set(reviews)), new_ids
for n in new_ids:
    assert digest(root / paths[n]) == reviews[n]['sha256'], n
index = read(root / '00_start/catalog_index.json')
flat = lambda kind: [i for g in index[kind] for i in g['items']]
items = {i['id']: i for k in ('concepts', 'mechanisms') for i in flat(k)}
for n in reviews:
    items[n]['status'] = 'complete'
    items[n]['path'] = '../' + paths[n]
    if n.startswith('R-'):
        y = yaml.safe_load((root / paths[n]).read_text().split('---', 2)[1])
        for f in ('node_ids', 'related_mechanism_ids', 'logic_groups'):
            items[n][f] = copy.deepcopy(y.get(f, []))
        items[n]['node_mapping_stage'] = 'authored_logic_groups'
for kind in ('concepts', 'mechanisms'):
    complete = sum(i['status'] == 'complete' for i in flat(kind))
    index['counts'][kind]['complete'] = complete
    index['counts'][kind]['pending'] = len(flat(kind)) - complete
nc, nm = (index['counts'][k]['complete'] for k in ('concepts', 'mechanisms'))
total, pending = nc + nm, 234 - nc - nm
index['updated'] = '2026-10-30'
index['build_progress'] = {'as_of': '2026-10-30', 'authored_nodes': total, 'pending_nodes': pending,
                         'complete_concepts': nc, 'complete_mechanisms': nm,
                         'review': '../50_reviews/FULL_BUILD_20261028/MAIN_REVIEW.json'}
(root / '00_start/catalog_index.json').write_text(dump(index))
maintained = resume.setdefault('maintained_inputs', {})
input_hashes = read(out / 'INPUT_HASHES.json')
for kind, filename in [('concepts', 'CONCEPT_IMPORT_LIST.md'), ('mechanisms', 'MECHANISM_IMPORT_LIST.md')]:
    rel = '00_start/' + filename
    p = root / rel
    base = maintained[rel]['base_sha256'] if rel in maintained else current_input_hash(rel, input_hashes.get(rel, digest(p)))
    s = p.read_text()
    count = index['counts'][kind]
    s = re.sub(r'正文 \*\*\d+ 份已完成、\d+ 份待(?:制作|完成主审)\*\*(?:（进度更新：[^）]+）)?',
               f'正文 **{count["complete"]} 份已完成、{count["pending"]} 份待完成主审**（进度更新：2026-10-30）', s, count=1)
    for g in index[kind]:
        num, p0 = len(g['items']), sum(i['priority'] == 'P0' for i in g['items'])
        done = sum(i['status'] == 'complete' for i in g['items'])
        s = re.sub(r'^\| ' + re.escape(g['title']) + r' \| \d+ \| \d+ \| \d+ \| \d+ \|$',
                   f'| {g["title"]} | {num} | {p0} | {done} | {num-done} |', s, flags=re.M)
    lines = []
    for line in s.splitlines():
        m = re.search(r'<a id="([CR]-[^"]+)"></a>', line)
        if m and items[m[1]]['status'] == 'complete':
            n = m[1]
            cells = line.split(' | ')
            cells[-1] = 'complete／[正文](' + markdown_target('../' + paths[n]) + ') |'
            if kind == 'mechanisms':
                cells[2] = '；'.join(f'[{items[c]["name"]} {c}](' + (markdown_target('../'+paths[c]) if items[c]['status']=='complete' else 'CONCEPT_IMPORT_LIST.md#'+c) + ')' for c in items[n]['node_ids']) or '—'
            line = ' | '.join(cells)
        lines.append(line)
    p.write_text('\n'.join(lines)+'\n')
    maintained[rel] = {'base_sha256': base, 'current_sha256': digest(p), 'reason': 'reviewed progress and authored mechanism mappings; selected scope unchanged'}
p = root / '00_start/README.md'
s = re.sub(r'^更新：[^\n]*', f'更新：2026-10-30。正式范围163个对象、71个机制，共234个节点；当前{total}份经审阅正文（{nc}个对象、{nm}个机制），{pending}份待完成主审。续作与远端分批提交见[续作记录](../50_reviews/FULL_BUILD_20261028/CONTINUATION_20261030.json)；正文按[标题命名](FILE_NAMING.md)。', p.read_text(), count=1, flags=re.M)
p.write_text(s)
p = root / 'README.md'
s = re.sub(r'现有\d+份经审阅正文（\d+个Concepts、\d+个Mechanisms），其余\d+份尚未完成主审。', f'现有{total}份经审阅正文（{nc}个Concepts、{nm}个Mechanisms），其余{pending}份尚未完成主审。', p.read_text())
p.write_text(s)
resume['committed_ids'] = list(dict.fromkeys(resume.get('committed_ids', []) + new_ids))
if last and not last.get('local_commit'):
    assert last['ids'] == new_ids
    checkpoint = last
else:
    checkpoint = {'sequence': len(resume['checkpoints'])+1, 'date':'2026-10-30', 'ids':new_ids, 'reviewed_total':total, 'remote_status':'prepared'}
    resume['checkpoints'].append(checkpoint)
(out / 'CONTINUATION_20261030.json').write_text(dump(resume))
subprocess.run(['python', str(out / 'validate_build.py'), '--reviewed-only'], cwd=repo, check=True)
if not args.commit:
    raise SystemExit('Prepared metadata only; --commit required to stage and commit.')
prefix = root.relative_to(repo).as_posix()
tracked = [str(p.relative_to(repo)) for p in (root/'README.md',root/'00_start/README.md',root/'00_start/catalog_index.json',root/'00_start/CONCEPT_IMPORT_LIST.md',root/'00_start/MECHANISM_IMPORT_LIST.md')]
tracked += [str((out/f).relative_to(repo)) for f in ('RUN_STATE.json','MAIN_REVIEW.json','CONTINUATION_20261030.json','record_review.py','validate_build.py','filename_migration.py','checkpoint_build.py')]
for n in new_ids:
    tracked.append(prefix+'/'+paths[n])
    b = next(b['batch'] for b in state['batches'] if any(i['id']==n for i in b['items']))
    for name in (n+'_FIRST_DRAFT.md','NOTES.md','RECOVERY_20261030.md'):
        p = out/b/name
        if p.exists(): tracked.append(str(p.relative_to(repo)))
subprocess.run(['git','add','--',*dict.fromkeys(tracked)],cwd=repo,check=True)
# Stage only reviewed delivery items; leave the author's live manifest intact.
for b in {next(b['batch'] for b in state['batches'] if any(i['id']==n for i in b['items'])) for n in new_ids}:
    p = out/b/'DELIVERY.json'
    d = read(p)
    if 'items' in d: d['items'] = [x for x in d['items'] if x.get('id') in reviews]
    else:
        raise AssertionError('Normalize delivery items before checkpoint: '+b)
    blob = subprocess.check_output(['git','hash-object','-w','--stdin'],input=dump(d).encode(),cwd=repo).decode().strip()
    subprocess.run(['git','update-index','--add','--cacheinfo','100644',blob,str(p.relative_to(repo))],cwd=repo,check=True)
subprocess.run(['git','-c','core.whitespace=-blank-at-eol','diff','--cached','--check'],cwd=repo,check=True)
message = f'Complete and review {len(new_ids)} nodes ({total}/234)'
subprocess.run(['git','commit','-m',message],cwd=repo,check=True,stdout=subprocess.DEVNULL)
dest = Path(args.output); dest.mkdir(parents=True,exist_ok=True)
raw = subprocess.check_output(['git','diff-tree','--no-commit-id','--raw','-r','--no-renames','-z','HEAD'],cwd=repo).split(b'\0')
tree, uploads = [], []
for i in range(0,len(raw)-1,2):
    head, path = raw[i].decode().split(), raw[i+1].decode()
    mode, sha = head[1], head[3]
    tree.append({'path':path,'mode':'100644' if mode=='000000' else mode,'type':'blob','sha':None if mode=='000000' else sha})
    if mode!='000000':
        content = subprocess.check_output(['git','show',sha],cwd=repo).decode()
        uploads.append({'path':path,'mode':mode,'type':'blob','content':content})
batches=[]; chunk=[]; size=0
for x in uploads:
    n=len(json.dumps(x,ensure_ascii=False).encode())
    if chunk and size+n>180000: batches.append(chunk);chunk=[];size=0
    chunk.append(x);size+=n
if chunk:batches.append(chunk)
for i,b in enumerate(batches):(dest/f'{i:02}.json').write_text(dump(b))
(dest/'tree.json').write_text(dump(tree))
manifest={'local_commit':git('rev-parse','HEAD'),'tree':git('rev-parse','HEAD^{tree}'),'base_tree':git('rev-parse','HEAD^^{tree}'),'message':message,'chunks':len(batches),'ids':new_ids}
(dest/'manifest.json').write_text(dump(manifest))
checkpoint['local_commit'] = manifest['local_commit']
checkpoint['tree'] = manifest['tree']
checkpoint['remote_status'] = 'awaiting_upload'
(out / 'CONTINUATION_20261030.json').write_text(dump(resume))
print(dump(manifest))
