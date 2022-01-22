#!/usr/bin/env python3

# """makeproblem.py
#
# Usage:
#  makeproblem.py <book> <chapter> <problem>
#
# Options:
#  -h --help     Show this screen.
#
# """

import argparse
from genericpath import exists
import os
from sys import stderr

dir_mode = 0o755
file_mode = 0o644

parser = argparse.ArgumentParser()
parser.add_argument("root", help='Root document', type=ascii)
parser.add_argument('-b', "--book", help='Textbook name', type=ascii)
parser.add_argument('-c', "--chapter", help='Chapter number', type=int)
parser.add_argument('-s', "--section", help="Section number", type=int)
parser.add_argument("problem", help='Problem number', type=int)


def make_file(root, book, chapter, section, problem):

    title = ""
    if (book):
        title += f'{book} '

    name = f'prob'

    if (chapter):
        name += f'_{int(args.chapter):02d}'
        title += str(chapter)

        if (section):
            title += f'.{section}'
            name += f'_{int(args.section):02d}'

        title += f' \#{problem}'
    else:
        title = problem

    name += f'_{int(args.problem):02d}'

    fname = name + ".tex"
    os.mkdir(name, dir_mode)  # May fail
    path = os.path.join(name, fname)
    with open(os.open(path, os.O_CREAT | os.O_WRONLY, file_mode), 'x') as fh:
        fh.write(f"""\\documentclass[../{root}]{{subfiles}}

\\begin{{document}}
\\section{{{title}}}



\\end{{document}}
""")


if __name__ == '__main__':
    args = parser.parse_args()

    root = args.root.strip("\'\"")
    if not exists(root):
        print("Root file '%s' does not exist." % root, file=stderr)
        exit(1)

    book = args.book
    if (args.book):
        book = book.strip("\'\"")

    make_file(root, book, args.chapter, args.section, args.problem)
