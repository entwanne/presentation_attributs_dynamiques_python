#!/usr/bin/env python

import argparse
import json
import sys


parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='file', nargs='+', help='Files to compute')
parser.add_argument('-t', '--title-split', action='store_true')
parser.add_argument('-p', '--title-page', action='store_true')
parser.add_argument('-o', '--output', default=None)
args = parser.parse_args()

title_split = args.title_page or args.title_split


def make_cell(cell_type, source, slide_type='-'):
    cell = {
        'cell_type': cell_type,
        'metadata': {
            'slideshow': {
                'slide_type': slide_type,
            },
        },
        'source': source,
    }

    if cell_type == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None

    return cell


def cell_is_empty(cell):
    source = cell['source']
    if not source:
        return True
    return not any(line.rstrip('\r\n') for line in source)


def iter_files(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield from f


cells = [make_cell('markdown', [], 'slide')]

for line in iter_files(args.files):
    if title_split and line.startswith('# '):
        cells.append(make_cell('markdown', [line], 'slide'))
        if args.title_page:
            cells.append(make_cell('markdown', [], 'slide'))
    elif line.startswith('---'):
        cells.append(make_cell('markdown', [], 'slide'))
    elif line.startswith('```python'):
        cells.append(make_cell('code', []))
    elif line.startswith('```') and cells[-1]['cell_type'] == 'code':
        cells.append(make_cell('markdown', []))
    else:
        cells[-1]['source'].append(line)

cells = [cell for cell in cells if not cell_is_empty(cell)]
doc = {
    'cells': cells,
    'metadata': {
        'celltoolbar': 'Slideshow',
        'kernelspec': {
            'display_name': 'Python 3',
            'language': 'python',
            'name': 'python3'
        },
        'language_info': {
            'codemirror_mode': {
                'name': 'ipython',
                'version': 3
            },
            'file_extension': '.py',
            'mimetype': 'text/x-python',
            'name': 'python',
            'nbconvert_exporter': 'python',
            'pygments_lexer': 'ipython3',
            'version': '3.6.5'
        },
    },
    'nbformat': 4,
    'nbformat_minor': 2,
}


if args.output:
    f = open(args.output, 'w')
else:
    f = sys.stdout

with f:
    json.dump(doc, f, indent=4)