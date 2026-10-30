"""Validate authored nodes and, with --final, the integrated full release.

This checks structure/provenance/navigation, never substitutes for MAIN_REVIEW.
Default mode permits unstarted batches and links to their frozen planned paths.
"""
import argparse
import hashlib
import json
import re
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

import yaml
from filename_migration import current_input_hash, original_path, rewrite_paths

parser = argparse.ArgumentParser()
parser.add_argument('--final', action='store_true')
parser.add_argument('--write', action='store_true')
parser.add_argument('--reviewed-only', action='store_true', help='checkpoint only: ignore active author deliveries')
args = parser.parse_args()
out = Path(__file__).resolve().parent
root = out.parent.parent
repo = root.parent
readj = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
flat = lambda j, k: [i for g in j[k] for i in g['items']]
baseline = readj(out / 'BASELINE_INDEX.json')
index = readj(root / '00_start/catalog_index.json')
state = readj(out / 'RUN_STATE.json')
paths = readj(out / 'PATHS.json')
reviews = readj(out / 'MAIN_REVIEW.json')['entries']
selected = {i['id']: i for k in ('concepts', 'mechanisms') for i in flat(baseline, k)}
new = {i for i, item in selected.items() if item['status'] != 'complete'}
errors, warnings = [], []


def check(ok, message):
    if not ok:
        errors.append(message)


def delivery_items(value):
    """Support author manifests as lists or nested items/documents/articles."""
    if isinstance(value, dict):
        if isinstance(value.get("id"), str):
            yield value
        for nested in value.values():
            if isinstance(nested, (dict, list)):
                yield from delivery_items(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from delivery_items(nested)


def front(path):
    text = path.read_text()
    parts = text.split('---', 2)
    check(text.startswith('---\n') and len(parts) == 3, f'{path.name}: front matter')
    return yaml.safe_load(parts[1]), parts[2]


def anchors(text):
    found = set(re.findall(r'\bid=[\"\']([^\"\']+)[\"\']', text))
    seen = Counter()
    for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        h = re.sub(r'<[^>]+>', '', h).strip().lower()
        h = ''.join(c for c in h if unicodedata.category(c)[0] not in 'PS' or c in '-_')
        h = re.sub(r'\s', '-', h)
        n = seen[h]
        seen[h] += 1
        found.add(h if n == 0 else f'{h}-{n}')
    return found


check(len(selected) == 234 and len(new) == 222, 'frozen selected/new counts')
check(set(paths) == set(selected), 'planned paths differ from selected scope')
check(state['main_ids'] == ['C-EXPECT-05', 'R-DERIV-CARRY'], 'main assignment changed')
assigned = []
by_id = {}
for batch in state['batches']:
    check(1 <= len(batch['items']) <= 3, batch['batch'] + ': worker exceeds three nodes')
    check(batch['model'] == 'gpt-6-astra' and batch['reasoning_effort'] == 'medium', batch['batch'] + ': model')
    original = readj(out / batch['batch'] / 'ASSIGNMENT.json')
    check(original['items'] == batch['items'], batch['batch'] + ': assignment altered')
    for item in batch['items']:
        assigned.append(item['id'])
        by_id[item['id']] = batch
check(len(assigned) == len(set(assigned)) == 220, 'worker duplicate/missing assignments')
check(set(assigned) | set(state['main_ids']) == new, 'new authorship coverage')

# Only examine delivered batches; an active writer may currently be saving a file.
ready = set()
for batch in state['batches']:
    delivery_path = out / batch['batch'] / 'DELIVERY.json'
    if delivery_path.exists():
        delivered = {x['id'] for x in delivery_items(readj(delivery_path))}
        assigned_here = {x['id'] for x in batch['items']}
        check(delivered <= assigned_here, batch['batch'] + ': foreign delivery')
        ready.update(delivered & assigned_here)
ready.update(state['main_ids'])
if args.reviewed_only:
    assert not args.final, 'final validation must include every delivery'
    ready &= set(reviews)
if args.final:
    check(ready == new, 'not every assigned node delivered')
    check(set(reviews) == new, 'not every new node has a main review')
    check(all(b['status'] == 'reviewed' for b in state['batches']), 'unreviewed batch remains')

metadata, source_counts, authors, first_hashes = {}, {}, Counter(), {}
for node in sorted(ready):
    page = root / paths[node]
    if not page.exists():
        errors.append(node + ': delivered file absent')
        continue
    y, body = front(page)
    metadata[node] = y
    check(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', body), node + ': unexpected control character in body')
    item = selected[node]
    check(y['id'] == node and y['title'] == item['name'], node + ': identity/name mismatch')
    check(y['type'] == ('concept' if node.startswith('C-') else 'mechanism'), node + ': type')
    check('evidence_as_of' in y, node + ': evidence cutoff absent')
    expected_author = '/root' if node in state['main_ids'] else state.get('author_by_id', {}).get(node, by_id[node]['agent'])
    check(y['draft_author'] == expected_author, node + ': wrong author')
    authors[expected_author] += 1
    if node not in state['main_ids']:
        check(y['model'] == 'gpt-6-astra' and y['reasoning_effort'] == 'medium', node + ': model')
    if node in reviews:
        check(y['status'] == 'reviewed_seed' and y['reviewed_by'] == '/root', node + ': review metadata')
        check(reviews[node]['full_read'] is True and len(reviews[node]['notes']) > 20, node + ': review record')
        check(reviews[node]['sha256'] == sha(page), node + ': post-review hash changed')
    elif args.final:
        errors.append(node + ': not reviewed')
    batch_name = 'MAIN' if node in state['main_ids'] else by_id[node]['batch']
    draft = out / batch_name / (node + '_FIRST_DRAFT.md')
    check(draft.exists(), node + ': frozen first draft absent')
    if draft.exists():
        first_hashes[node] = sha(draft)
        dy, _ = front(draft)
        check(dy['id'] == node and dy['draft_author'] == expected_author, node + ': first draft identity')
        delivery = readj(out / batch_name / 'DELIVERY.json')
        for di in delivery_items(delivery):
            if di.get('id') == node and di.get('first_draft_sha256'):
                check(first_hashes[node] == di['first_draft_sha256'], node + ': frozen first draft hash')
    source_anchors = re.findall(r'<a id="(S-[^"]+)"></a>', body)
    refs = re.findall(r'\]\(#(S-[^)]+)\)', body)
    check(len(source_anchors) == len(set(source_anchors)), node + ': duplicate source anchor')
    check(set(y['source_ids']) == set(source_anchors), node + ': source declaration mismatch')
    check(set(refs) == set(source_anchors), node + ': source citations mismatch')
    source_counts[node] = len(source_anchors)
    if node.startswith('R-'):
        groups = y.get('logic_groups', [])
        check(bool(groups), node + ': no logic groups')
        ga = [g['anchor'] for g in groups]
        check(len(ga) == len(set(ga)), node + ': duplicate logic group')
        check(set(ga) <= anchors(body), node + ': missing logic anchor')
        for g in groups:
            check(all(n in selected and n.startswith('C-') for n in g['node_ids']), node + ': invalid concept in logic')
            check(all(n in selected and n.startswith('R-') for n in g.get('related_mechanism_ids', [])), node + ': invalid related mechanism')
        check(set(y['node_ids']) == {n for g in groups for n in g['node_ids']}, node + ': logic node union mismatch')
        check(all(n in selected and n.startswith('R-') for n in y.get('related_mechanism_ids', [])), node + ': invalid page related mechanism')

check(authors['/root'] == 2, 'main did not author exactly one concept and one mechanism')
check(all(n <= 3 for a, n in authors.items() if a != '/root'), 'worker lifetime limit')

# The original confirmed scope, exclusions, and historical baseline are immutable.
mutable = {'path', 'planned_path', 'status', 'node_ids', 'logic_groups', 'related_mechanism_ids', 'node_mapping_stage'}
for kind in ('concepts', 'mechanisms'):
    before, now = flat(baseline, kind), flat(index, kind)
    check([i['id'] for i in before] == [i['id'] for i in now], kind + ': scope/order altered')
    for a, b in zip(before, now):
        check({k:v for k,v in a.items() if k not in mutable} == {k:v for k,v in b.items() if k not in mutable}, a['id'] + ': selection/name/scope altered')
    if args.final:
        check(all(i['status'] == 'complete' for i in now), kind + ': pending catalog entries')
        check(index['counts'][kind]['complete'] == len(now) and index['counts'][kind]['pending'] == 0, kind + ': wrong counts')
        list_name = 'CONCEPT_IMPORT_LIST.md' if kind == 'concepts' else 'MECHANISM_IMPORT_LIST.md'
        text = (root / '00_start' / list_name).read_text()
        check(re.findall(r'<a id="([CR]-[^"]+)"></a>', text) == [i['id'] for i in now], list_name + ': IDs/order')
        for i in now:
            line = next((l for l in text.splitlines() if f'<a id="{i["id"]}"></a>' in l), '')
            check(f'| {i["name"]} |' in line and 'complete／' in line and i['path'] in line, i['id'] + ': human catalog mismatch')
            check(i['path'] == '../' + paths[i['id']], i['id'] + ': catalog path mismatch')
        for g in index[kind]:
            n, p0 = len(g['items']), sum(i['priority'] == 'P0' for i in g['items'])
            check(f'| {g["title"]} | {n} | {p0} | {n} | 0 |' in text, g['title'] + ': group counts')
for key in ('excluded_concepts', 'excluded_mechanisms', 'deferred', 'build_baseline'):
    check(index[key] == baseline[key], key + ': historical scope altered')
for rel, digest in readj(out / 'INPUT_HASHES.json').items():
    if rel not in ('00_start/README.md', '00_start/catalog_index.json'):
        check(sha(root / rel) == current_input_hash(rel, digest), rel + ': authoring standard changed beyond recorded maintenance')

# Event/Source prose and assets stay intact; recorded filename navigation is allowed.
unchanged = {}
for folder in ('30_events', '40_sources', 'assets'):
    prefix = root.relative_to(repo).as_posix() + '/' + folder + '/'
    raw = subprocess.check_output(['git', 'ls-tree', '-r', state['base_commit'], '--', prefix], cwd=repo, text=True)
    expected = {}
    for line in raw.splitlines():
        mode_type_hash, rel = line.split('\t', 1)
        original_blob = mode_type_hash.split()[-1]
        if Path(rel).suffix == '.md':
            old_text = subprocess.check_output(['git', 'show', original_blob], cwd=repo).decode()
            expected[rel] = subprocess.check_output(['git', 'hash-object', '--stdin'], input=rewrite_paths(old_text).encode()).decode().strip()
        else:
            expected[rel] = original_blob
    actual = {p.relative_to(repo).as_posix(): subprocess.check_output(['git', 'hash-object', str(p)], text=True).strip() for p in (root / folder).rglob('*') if p.is_file()}
    unchanged[folder] = expected == actual
    check(unchanged[folder], folder + ': changed outside authorized scope')

# Release invariants: old explanations are preserved; new navigation is complete.
legacy_unchanged = None
if args.final:
    expected_authors = {state.get('author_by_id', {}).get(n, by_id[n]['agent']) for n in new if n not in state['main_ids']} | {'/root'}
    check(set(authors) == expected_authors and authors['/root'] == 2, 'author roster differs from recorded assignments')
    progress = index['build_progress']
    check(progress['authored_nodes'] == 234 and progress['pending_nodes'] == 0, 'build progress count')
    current = {i['id']: i for k in ('concepts', 'mechanisms') for i in flat(index, k)}
    for rn in (n for n in new if n.startswith('R-')):
        for field in ('node_ids', 'logic_groups', 'related_mechanism_ids'):
            check(current[rn][field] == metadata[rn][field], rn + ': catalog differs from authored ' + field)
        group_related = {r for g in metadata[rn]['logic_groups'] for r in g.get('related_mechanism_ids', [])}
        check(group_related <= set(metadata[rn]['related_mechanism_ids']), rn + ': missing group related mechanism at page level')
    for mechanism in flat(index, 'mechanisms'):
        for group in mechanism['logic_groups']:
            for cn in group['node_ids']:
                dest = '../' + paths[mechanism['id']] + '#' + group['anchor']
                check('](' + dest + ')' in (root / paths[cn]).read_text(), cn + ': missing backlink to ' + mechanism['id'] + '#' + group['anchor'])
    legacy_unchanged = True
    for node in set(selected) - new:
        rel = (root / paths[node]).relative_to(repo).as_posix()
        old_rel = (root / original_path(node)).relative_to(repo).as_posix()
        original = subprocess.check_output(['git', 'show', state['base_commit'] + ':' + old_rel], cwd=repo, text=True)
        original = rewrite_paths(original)
        for n, path in paths.items():
            filename = 'CONCEPT_IMPORT_LIST.md' if n.startswith('C-') else 'MECHANISM_IMPORT_LIST.md'
            for prefix in ('../00_start/', ''):
                original = original.replace(f'({prefix}{filename}#{n})', f'(../{path})')
        actual = (root / paths[node]).read_text()
        actual = re.sub(r'<!-- FULL_BUILD_MECHANISM_BACKLINKS_START -->.*?<!-- FULL_BUILD_MECHANISM_BACKLINKS_END -->\n*', '', actual, flags=re.S)
        equal = original.rstrip() == actual.rstrip()
        legacy_unchanged = legacy_unchanged and equal
        check(equal, node + ': legacy prose changed beyond approved navigation')

# Relative links are checked in live pages, excluding byte-preserved historical drafts.
pages = [root / paths[i] for i in ready]
if args.final:
    pages = [repo / 'README.md', root / 'README.md', root / '50_reviews/README.md', out / 'MAIN_REVIEW.md'] + [p for folder in ('00_start', '10_concepts', '20_mechanisms', '30_events', '40_sources') for p in (root / folder).rglob('*.md')]
cache, link_count, planned_links = {}, 0, 0
planned = {(root / p).resolve() for p in paths.values()}
for p in pages:
    text = re.sub(r'^```.*?^```[^\n]*', '', p.read_text(), flags=re.S | re.M)
    text = re.sub(r'`[^`\n]*`', '', text)
    for target in re.findall(r'\]\(([^\n)]*)\)', text):
        target = target.strip().strip('<>')
        if re.match(r'^[a-zA-Z][\w+.-]*:', target):
            continue
        filename, _, fragment = unquote(target).partition('#')
        destination = (p.parent / filename).resolve() if filename else p
        link_count += 1
        if not destination.exists():
            # This invocation creates its own report after validating all other links.
            if args.final and args.write and destination == (out / 'VALIDATION.json').resolve():
                continue
            if not args.final and destination in planned:
                planned_links += 1
                continue
            errors.append(f'{p.name}: missing local target {target}')
        elif fragment and destination.suffix == '.md':
            if destination not in cache:
                cache[destination] = anchors(destination.read_text())
            check(fragment in cache[destination], f'{p.name}: missing anchor {target}')

report = {'mode': 'final' if args.final else 'in_progress', 'selected_nodes': 234,
          'new_nodes': 222, 'delivered_new_nodes': len(ready), 'reviewed_new_nodes': len(reviews),
          'source_counts': source_counts, 'authors': dict(authors), 'first_draft_sha256': first_hashes,
          'unchanged_trees': unchanged, 'legacy_prose_preserved': legacy_unchanged, 'local_links_checked': link_count, 'planned_links_not_yet_built': planned_links,
          'errors': errors, 'warnings': warnings,
          'limitations': ['Structural validation does not replace the recorded full-text editorial reviews or independently replicate all cited research.',
                          'Evidence cutoffs differ by page; the editing date is not a real-time market-data cutoff.']}
if args.write:
    (out / ('VALIDATION.json' if args.final else 'STRUCTURE_CHECK_IN_PROGRESS.json')).write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('source_counts', 'authors', 'first_draft_sha256')}, ensure_ascii=False, indent=2))
raise SystemExit(bool(errors))
