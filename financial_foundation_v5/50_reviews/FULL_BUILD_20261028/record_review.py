"""Record a main-agent full read. Input is a JSON mapping of IDs to review notes.

This records a human/agent review already performed; it does not review content.
It never changes the frozen first drafts.
"""
import hashlib
import json
import sys
from pathlib import Path

review_root = Path(__file__).resolve().parent
content_root = review_root.parent.parent
state_file = review_root / 'RUN_STATE.json'
review_file = review_root / 'MAIN_REVIEW.json'
state = json.loads(state_file.read_text())
review = json.loads(review_file.read_text())
paths = json.loads((review_root / 'PATHS.json').read_text())
batch_by_id = {item['id']: b['batch'] for b in state['batches'] for item in b['items']}
for node_id, notes in json.load(sys.stdin).items():
    assert node_id in batch_by_id, node_id
    assert isinstance(notes, str) and len(notes) > 20
    page = content_root / paths[node_id]
    body = page.read_text()
    assert 'status: draft' in body or 'status: reviewed_seed' in body
    body = body.replace('status: draft', 'status: reviewed_seed', 1)
    body = body.replace('reviewed_by: null', 'reviewed_by: /root', 1)
    page.write_text(body)
    review['entries'][node_id] = {
        'batch': batch_by_id[node_id], 'status': 'reviewed_seed',
        'full_read': True, 'reviewed_on': '2026-10-28', 'notes': notes,
        'sha256': hashlib.sha256(page.read_bytes()).hexdigest(),
    }
for batch in state['batches']:
    if all(item['id'] in review['entries'] for item in batch['items']):
        batch['status'] = 'reviewed'
state['reviewed_new_count'] = len(review['entries'])
review_file.write_text(json.dumps(review, ensure_ascii=False, indent=2) + '\n')
state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
print('reviewed_new_count:', state['reviewed_new_count'])
