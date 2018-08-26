#!/usr/bin/env python

import argparse
import enum
import json
import re
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


class CellType(enum.IntEnum):
    SLIDE = enum.auto()
    SUBSLIDE = enum.auto()
    FRAGMENT = enum.auto()
    NORMAL = enum.auto()
    SKIP = enum.auto()


class _Token:
    def __init__(self, _type, line=None, **kwargs):
        self.type = _type
        self.line = line
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        args = []
        if self.line is not None:
            args.append(repr(self.line))
        for key, value in self.params.items():
            args.append(f'{key}={value!r}')

        return f"{self.type}({', '.join(args)})"


class Token(enum.Enum):
    def __call__(self, *args, **kwargs):
        return _Token(self, *args, **kwargs)

    LINE = enum.auto()
    FILE = enum.auto()
    TITLE = enum.auto()
    AFTER_TITLE = enum.auto()
    SPLIT = enum.auto()
    START_CODE = enum.auto()
    END_CODE = enum.auto()


def iter_file(filename):
    code = False

    with open(filename) as f:
        for line in f:
            if code:
                if line.startswith('```'):
                    code = False
                    yield Token.END_CODE(line)
                else:
                    yield Token.LINE(line)
                continue

            match = re.match(r'(#+) ', line)
            if match:
                level = len(match.group(1))
                yield Token.TITLE(line, level=level)
                yield Token.AFTER_TITLE(level=level)
            elif line.startswith('---'):
                yield Token.SPLIT(line)
            elif line.startswith('```'):
                code = True
                args = line[3:].split()
                skip = 'skip' in args
                yield Token.START_CODE(line, language=args[0], skip=skip)
            else:
                yield Token.LINE(line)


def iter_files(filenames):
    for filename in filenames:
        yield from iter_file(filename)
        yield Token.FILE()


cells = [make_cell('markdown', [], 'slide')]

# Produce a list of cells and separators
# A cell is a list of lines with a type (markdown/python)
# A separator indicates the slide-type of the next cell (slide, subslide, fragment, etc.)
# The list will then be filtered to remove empty cells and separator will apply on the cell just after
for token in iter_files(args.files):
    if token.type is Token.FILE:
        pass
    elif token.type is Token.TITLE:
        if token.level == 1 and (args.title_page or args.title_split):
            cells.append(make_cell('markdown', [token.line], 'slide'))
        else:
            cells[-1]['source'].append(token.line)
    elif token.type is Token.AFTER_TITLE:
        if token.level == 1 and args.title_page:
            cells.append(make_cell('markdown', [], 'slide'))
    elif token.type is Token.SPLIT:
        cells.append(make_cell('markdown', [], 'slide'))
    elif token.type is Token.START_CODE:
        cells.append(make_cell('code', [], 'skip' if token.skip else '-'))
    elif token.type is Token.END_CODE:
        cells.append(make_cell('code', []))
    elif token.line is not None:
        cells[-1]['source'].append(token.line)


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
