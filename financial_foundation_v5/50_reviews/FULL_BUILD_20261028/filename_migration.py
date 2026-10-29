"""Resolve frozen pre-migration paths without rewriting historical evidence."""
import json
import re
from pathlib import Path

record_path = Path(__file__).resolve().parent.parent / 'FILENAME_MIGRATION_20261029.json'
record = json.loads(record_path.read_text())
filenames = {Path(n['old_path']).name: Path(n['new_path']).name for n in record['nodes']}
pattern = re.compile(r'(?<![\w-])(' + '|'.join(re.escape(n) for n in sorted(filenames, key=len, reverse=True)) + r')(?![\w.-])')


def rewrite_paths(text):
    return pattern.sub(lambda m: filenames[m.group(1)], text)


def original_path(node):
    return next(n['old_path'] for n in record['nodes'] if n['id'] == node)


def current_input_hash(rel, original_hash):
    return record.get('updated_inputs', {}).get(rel, {}).get('after_sha256', original_hash)


def markdown_target(path):
    """Keep title spaces intact and render valid Markdown link destinations."""
    return '<' + path + '>' if any(c.isspace() for c in path) else path
