"""Mechanical delivery and arithmetic checks; no semantic-review claim."""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
OUT = HERE.parent
WORK = OUT.parent.parent
evidence = json.loads((OUT / 'evidence.json').read_text(encoding='utf-8'))
checks = []

def require(name, condition, detail):
    checks.append({'check': name, 'passed': bool(condition), 'detail': detail})
    if not condition:
        raise AssertionError(name)

required = ['reading_map.md', 'change_proposal.md', 'evidence.json', 'brief_feedback.md',
            'drafts/经常账户.md', 'drafts/资本流动与资本管制_更新片段.md']
require('minimum_delivery', all((OUT / p).is_file() for p in required), required)
for field, digest_field in [('file', 'sha256'), ('text_file', 'text_sha256')]:
    actual = sha256((WORK / evidence['source'][field]).read_bytes()).hexdigest()
    require('source_hash_' + field, actual == evidence['source'][digest_field], actual)

ids = [row['id'] for row in evidence['claims']]
require('unique_evidence_ids', len(ids) == len(set(ids)), ids)
for row in evidence['claims']:
    pages = row['pdf_pages']
    require('evidence_' + row['id'],
            (WORK / row['source_file']).is_file()
            and all(1 <= p <= 12 for p in pages)
            and pages == row['original_page_numbers']
            and bool(row['attribute']),
            {'pages': pages, 'attribute': row['attribute']})
require('original_page_images',
        all((HERE / f'page-{n:02d}.png').is_file() for n in range(1, 13)),
        '12 rendered source pages; these files do not prove actual visual reading')

link_records = []
for path in sorted(OUT.rglob('*.md')):
    content = path.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', content):
        if target.startswith(('https://', 'http://', '#')):
            continue
        target_path = target.split('#', 1)[0]
        resolved = (path.parent / target_path).resolve()
        link_records.append({'from': str(path.relative_to(OUT)), 'target': target,
                             'exists': resolved.exists()})
    for item in set(re.findall(r'\bE\d{2}\b', content)):
        require('referenced_id_' + path.name + '_' + item, item in ids, item)
require('markdown_local_links', all(item['exists'] for item in link_records), link_records)

def path_values(b0, r, trade):
    b = b0
    path = []
    for t, tb in enumerate(trade, 1):
        next_b = (1 + r) * b + tb
        ca = next_b - b
        require(f'account_identity_{b0}_{t}', ca == r * b + tb, str(ca))
        path.append({'period': t, 'TB': str(tb), 'B': str(next_b), 'CA': str(ca)})
        b = next_b
    pv = sum(tb / (1 + r) ** t for t, tb in enumerate(trade, 1))
    require('finite_terminal_' + str(b0), b == 0 and pv == -b0,
            {'terminal': str(b), 'discounted_TB_sum': str(pv)})
    require('finite_CA_sum_' + str(b0),
            sum(F(row['CA']) for row in path) == -b0, str(-b0))
    return path

debtor = path_values(F(-100), F(1, 10), [F(0), F(121)])
creditor = path_values(F(100), F(1, 10), [F(-60), F(-55)])
require('two_period_first_period_discount_base',
        (1 + F(1, 10)) * F(-100) == -F(0) - F(121) / (1 + F(1, 10)),
        'Source page 5 expression agrees with date-zero discounting')

r, g, debt = F(5, 100), F(2, 100), F(100)
growth_path = []
for t in range(1, 3):
    ca, tb = -g * debt, (r - g) * debt
    next_debt = (1 + g) * debt
    require('growth_identity_' + str(t),
            next_debt == (1 + r) * debt - tb and ca == debt - next_debt,
            {'CA': str(ca), 'TB': str(tb), 'D': str(next_debt)})
    growth_path.append({'period': t, 'CA': float(ca), 'TB': float(tb),
                        'interest': float(r * debt), 'D': float(next_debt)})
    debt = next_debt
require('growth_terminal_ratio', F(0) < (1 + g) / (1 + r) < F(1),
        {'ratio': str((1 + g) / (1 + r)), 'limit_basis': 'positive geometric ratio below one'})
require('constant_positive_B_trade_deficit',
        (1 + F(5, 100)) * F(100) - F(5) == F(100),
        'B=100, r=5%, TB=-5 gives CA=0 and unchanged B')

result = {
    'status': 'all_mechanical_checks_passed',
    'checks_count': len(checks),
    'checks': checks,
    'computed_examples': {'finite_debtor': debtor, 'finite_creditor': creditor,
                          'infinite_growth_first_two_periods': growth_path},
    'limits': ['No independent content review',
               'File presence does not prove semantic support or reading',
               'Infinite-horizon examples verify compatibility under explicit assumptions only']
}
(HERE / 'check_results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'checks_count': result['checks_count'],
                  'examples': result['computed_examples']}, ensure_ascii=False, indent=2))
