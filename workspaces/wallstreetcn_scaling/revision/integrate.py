"""Integrate reviewed revisions against each writer's saved base."""
from pathlib import Path
import json, subprocess, tempfile, sys, yaml, re

V = Path(__file__).resolve().parent
R = V.parent
G = R.parent / 'step2_articles/graph'

def metadata(text):
    return yaml.safe_load(text.split('---', 2)[1])

def integrate(article_id):
    A = V / str(article_id)
    delivery = json.loads((A / 'revision_delivery.json').read_text())
    base = json.loads((A / 'base.json').read_text())
    prepared = []
    for f in delivery['files']:
        p = G / f['path']
        content = (A / f['draft_path']).read_text()
        m = metadata(content)
        for key in ['id', 'type', 'title']:
            if m[key] != f[key]:
                raise ValueError(f'Metadata mismatch: {f["path"]}, {key}')
        if f['operation'] == 'new':
            if p.exists():
                raise ValueError(f'New path exists: {p}')
        else:
            original = base[f['path']]
            if metadata(p.read_text())['id'] != m['id']:
                raise ValueError(f'Identity mismatch: {p}')
            if p.read_text() != original:
                with tempfile.TemporaryDirectory(prefix='ff-revision-') as td:
                    paths = [Path(td) / name for name in ['ours', 'base', 'theirs']]
                    for q, text in zip(paths, [p.read_text(), original, content]):
                        q.write_text(text)
                    result = subprocess.run(['git', 'merge-file', '-p', *map(str, paths)], capture_output=True, text=True)
                    if result.returncode:
                        raise ValueError(f'Merge conflict: {p}\n{result.stdout[:2500]}')
                    content = result.stdout
        content = re.sub(r'(?m)^revision_status: (?:pending_review|draft|local_revision_draft)$', 'revision_status: reviewed', content)
        if 'workspace_reviewed_by:' not in content.split('---', 2)[1]:
            content = content.replace('\nupdated:', '\nworkspace_reviewed_by: /root\nworkspace_reviewed_on: 2026-11-16\nupdated:', 1)
        prepared.append((p, content))
    for p, content in prepared:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    run = json.loads((V / 'run.json').read_text())
    task = next(t for t in run['tasks'] if t['article_id'] == int(article_id))
    original_path = R.parents[1] / task['delivery']
    original = json.loads(original_path.read_text())
    old = {f['path']: f for f in original['files']}
    for f in delivery['files']:
        if f['path'] in old:
            operation = old[f['path']]['operation']
            old[f['path']].update({k: v for k, v in f.items() if k != 'draft_path'})
            old[f['path']]['operation'] = operation
        else:
            original['files'].append({k: v for k, v in f.items() if k != 'draft_path'})
    original['revision_review'] = str((A / 'audit.md').relative_to(R.parents[1]))
    original_path.write_text(json.dumps(original, ensure_ascii=False, indent=2) + '\n')
    task['status'] = 'revised'
    (V / 'run.json').write_text(json.dumps(run, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'article_id': int(article_id), 'integrated': len(prepared)}))

if __name__ == '__main__':
    integrate(sys.argv[1])
