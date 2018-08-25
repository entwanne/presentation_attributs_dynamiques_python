#!/usr/bin/env python

import argparse
import json
import sys


parser = argparse.ArgumentParser()
parser.add_argument('files', metavar='file', nargs='+', help='Files to compute')
parser.add_argument('-t', '--title-split', action='store_true')
parser.add_argument('-p', '--title-page', action='store_true')
parser.add_argument('-o', '--output', default=None)
# Add argument to split on files
# + choose the type of slide when split (ex: file=slide, title=sub-slide or subtitle=sub-slide)
# Possible splits : split on a ---, split on new file, split on title of level ≤N
# For each split : what is the type of the new cell (slide, sub-slide, fragment)?
# For title splits : Should the title be on a separate cell? What is the type of the next cell? => split on title + split after title
# Each split gives the type of the following cell
# Option to give configuration file
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


def clean_cell(cell):
    lines = cell['source']

    while lines and not lines[0].rstrip('\r\n'):
        lines.pop(0)
    while lines and not lines[-1].rstrip('\r\n'):
        lines.pop()

    if lines:
        lines[-1] = lines[-1].rstrip('\r\n')

    return cell


def iter_files(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield from f


cells = [make_cell('markdown', [], 'slide')]

for line in iter_files(args.files):
    if cells[-1]['cell_type'] == 'code':
        if line.startswith('```'):
            cells.append(make_cell('markdown', []))
        else:
            cells[-1]['source'].append(line)
        continue

    if line.startswith('```python-skip'):
        cells.append(make_cell('code', [], 'skip'))
    elif line.startswith('```python'):
        cells.append(make_cell('code', []))
    elif title_split and line.startswith('# '):
        cells.append(make_cell('markdown', [line], 'slide'))
        if args.title_page:
            cells.append(make_cell('markdown', [], 'slide'))
    elif line.startswith('---'):
        cells.append(make_cell('markdown', [], 'slide'))
    else:
        cells[-1]['source'].append(line)


cells = (clean_cell(cell) for cell in cells)
cells = [cell for cell in cells if cell['source']]
# Cleaning cells will loss informations on split types
# Ex: We split after a title to create a new slide, but a codeblock follow the title (with type '-')
#     The slide cell would be removed (empty) and the code cell keep the type '-' instead of 'slide'
# => Have on arborescent representation of cells: Slides > Sub-slides > Fragments > - = skip

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
