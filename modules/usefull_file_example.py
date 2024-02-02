#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : usefull_file_example.py
|      CREATED : 14-oct.-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC :
|        USAGE : ./usefull_file_example.py
====================================================================================================
"""

import os
import fnmatch
import re


def gen_find(pattern, dirname):
    """
    Find all filenames in a directory tree that match a shell wildcard pattern
    Example:
        for f in gen_find('*.md', '.'):
            print(f)
    """
    for path, dirlist, filelist in os.walk(dirname):
        for name in fnmatch.filter(filelist, pattern):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration
    """
    # from collections import namedtuple
    for filename in filenames:
        with open(filename, 'rt', encoding='utf-8') as f:
            yield f


def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence
    '''
    # import itertools
    # lines = itertools.chain(*iterators)
    # yield lines
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    Look for a regex pattern in a sequence of lines
    """
    pat = re.compile(pattern)
    for lineno, line in enumerate(lines, 1):
        if pat.search(line):
            yield (lineno, line)


# TODO: return filename. remember namedtuple

python_files = gen_find('*.py', '.')            # all python files.
files = gen_opener(python_files)                # yield all content of *.py files.
lines = gen_concatenate(files)                  # concatenate contents of all files.
pattern = gen_grep('(?i)enumerate', lines)      # search for our pattern

for line in pattern:
    print(line)
