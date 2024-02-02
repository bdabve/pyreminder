#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------
FILE     : zip_map_filter.txt
CREATED  : 11-August-2020
AUTHOR   : daBve, dabve@outlook.fr
USAGE    : ./zip_map_filter.txt
----------------------------------
DESC     :
--------------------------------------------------------
"""
from terminaltables import AsciiTable


def main():
    title = ' Zip, Map, Filter '

    zip_ = """
# take a series of iterable and aggregates the element from each of them.
  >> names = ['name', 'age', 'pay', 'job']
  >> values = ['Sue Jones', 45, 4000, 'hdw']
  >> sueList = list(zip(names, values))         # [('name', 'Sue Johnes'), ('Job', 'Software'), ('Pay', 35000), ('Age', 45)]
  >> sueDict = dict(zip(names, values))         # {'name': 'Sue Johnes', 'Job': 'Software', 'Pay': 35000, 'Age': 45}

# Useful with sqlite database
  >> curs.execute('select * from table_name')
  >> desc = [desc[0] for desc in curs.description]
  >> rowdict = [dict(zip(desc, row)) for row in curs.fetchall()]

# use zip to sort values
  >> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.75}
  >> prices_sorted = sorted(zip(prices.values(), prices.keys()))
  >> print(prices_sorted)            # [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

# use zip to loop through two list values, faster and readable.
  >> for index, name in zip(name, heros):
  ..     print(f'{name} is actualy {hero}')

# zip can be passed more than two sequences as input
  >> a = [1, 2, 3]
  >> b = [11, 12, 13]
  >> c = ['x', 'y', 'z']
  >> for i in zip(a, b, c):
  ..     print(i, end='')            # (1, 11, 'x')(2, 12, 'y')(3, 13, 'z')
    """

# ------------------------------------------------------------------------
    zip_longest = """
# With < zip >, Iteration stops whenever one of the input sequences is exhausted.
# If this behavior is not desired, use < itertools.zip_longest() > instead.

  >> from itertools import zip_longest
  >> a = [1, 2, 3]
  >> a = ['x', 'y', 'z', 'w']
  >> for i in zip_longest(a, b):
  ..     print(i)                        # ('x', 11), ('y', 12), ('z', 13), ('w', None)

# fillvalue.
  >> for i in zip_longest(a, b, fillvalue=0):
  ..     print(i)                        # ('x', 11), ('y', 12), ('z', 13), ('w', 0)
    """

# ------------------------------------------------------------------------

    map_ = """
# used to apply a function on all the elements of specified iterable and return map object.
  >> def to_upper(s):
  ..     return str(s).upper()

  >> map_iterator = map(to_upper, 'abc')
  >> for s in map_iterator:
  ..     print(s, end='')                        # A B C

  >> map_carre = map(lambda n: n**2, [1, 2, 3, 4])
  >> print(list(map_carre))                      # [1, 4, 9, 6]
  >> m_list = ['Dabve', 33, 4500]
  >> print(', '.join(map(str, m_list)))          # Dabve, 33, 4500
    """
# ------------------------------------------------------------------------

    filter_ = """>> languages = ["HTML", "JavaScript", "Python", "Ruby"]
>> print(list(filter(lambda x: x == "Python", languages)))       # 'Python'

>> lst_files = ['file.txt', 'file.csv', 'file.xlsx', 'file1.csv', 'etat.csv']
>> from fnmatch import fnmatch
>> print(list(filter(lambda x: fnmatch(x, '*.csv'), lang)))  # ['file.csv', 'file1.csv', 'etat.csv']

>> squares = [i**2 for i in range(1, 11)]
>> print(list(filter(lambda x: x >= 30 and x <= 70, squares)))   # [16, 25, 36, 49, 64]

>> garbled = "IXXX aXXmX aXXnXoXXXXtXhXeXXXrX sXXXeXcXXrXeXt mXXeXsXXsXaXXXgXeX!XX"
>> message = filter(lambda x: x != "X", garbled)                      # <filter object at 0x7f0d3ab547b8>
>> msg = ''.join(map(str, list(filter(lambda x: x!= 'X', garbled))))  # 'I am another secret message!'
    """
    table_data = [
        ['zip(iterable1, iterable2, ...)', zip_],
        ['zip_longest(iterable1, iterable2, ...)', zip_longest],
        ['map(callback, iterable, ...)', map_],
        ['filter(callback, iterable, ...)', filter_],
    ]
    table = AsciiTable(table_data, title)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    return table.table


def generate_content(func):
    """
    Generate Souce
    - This should yield prompt_toolkit `(style_string, text)` tuples.
    """
    main_app = func()
    for line in main_app:
        yield [('', line)]


if __name__ == '__main__':
    from pypager.source import GeneratorSource
    from pypager.pager import Pager
    p = Pager()                                         # create the pager
    source = GeneratorSource(generate_content(main))    # generate the source
    p.add_source(source)                                # add the content to the source
    p.run()
