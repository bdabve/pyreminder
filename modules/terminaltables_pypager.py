#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  FILE     : dicts.py
#  CREATED  :
#  AUTHOR   : daBve, dabve@outlook.fr
#  DESC     : this file demonstrate how to use pypager and terminal tables
#  USAGE    : ./dicts.py
# ----------------------------------------------------------

from terminaltables import AsciiTable


def main():
    title = ' Python Dicts '

    # getting started
    sorting_a_list_of_dictionaries_by_common_key = """>> rows = [
..     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
..     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
..     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
..     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
..     ]
>> from operator import itemgetter
>> by_fname = sorted(rows, key=itemgetter('fname'))
>> for row in by_fname:
..     print(row)

# The itemgetter() function can also accept multiple keys.
  >> by_lname_fname = sorted(rows, key=itemgetter('lname', 'fname'))
  >> for row in by_lname_fname:
  ..     print(row)
    """
    # ----------------------------------------------------------
    sorting_with_lambda = """>> by_lname_fname = sorted(rows, key=lambda x: (x['lname'], x['fname']))
>> for row in by_lname_fname:
..     print(row)

# This will work also with min, and max
  >> max_uid = max(rows, key=itemgetter('uid'))
  >> print(max_uid)
    """
    # -----------------------------------------------------------
    calculating_with_dicts = """>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.75}
>> print(prices)
>> print('Minimum value: {}'.format(min(zip(prices.values(), prices.keys()))))
>> print('Maximum value: {}'.format(max(zip(prices.values(), prices.keys()))))
>> print('Sum of all prices: {}'.format(sum(prices.values())))

# The hard way
>> minimum_price = min(prices, key=lambda x: prices[x])
>> print('Minimum Price: {}: {}'.format(minimum_price, prices[minimum_price]))
    """
    # --------------------------------------------------------------------
    finding_commonalities_in_two_dictionaries = """>> a = {'x': 2, 'y': 2, 'z': 3}
>> b = {'w': 10, 'x': 11, 'y': 2}
>> print(a.keys() & b.keys())       # find key in common
>> print(a.keys() - b.keys())       # key in a not in b
>> print(a.items() & b.items())     # key, value pairs in common
    """
    # --------------------------------------------------------------------
    dictionary_comprehension = """>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
>> p1 = {key: value for key, value in prices.items() if value > 200}
>> print(p1)

>> tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
>> p2 = {key:value for key, value in prices.items() if key in tech_names}
>> print(p2)

>> fname = ['dabve', 'meziane', 'znanada', 'halim']
>> lname = ['band', 'halal', 'chalba', 'awdSahra']
>> fullname = {key:value for key, value in zip(fname, lname)}
>> print(fullname)
    """
    # --------------------------------------------------------------------
    other_way_to_make_dicts = """>> bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
>> sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
>> dabve = dict(name='Dabve', age=33, pay=35000, job='dev')

>> people = [bob, sue, dabve]
>> names = [person['name'] for person in people]     # with list comprehension
>> print('people names: {}'.format(names))

>> job = list(map(lambda x: x['job'], people))       # with map and lambda
>> print('People\' job: {}'.format(job))

>> sum_pay = sum(person['pay'] for person in people)
>> print('The sum of all employee: {}'.format(sum_pay))

>> payGreat = [rec['name'] for rec in people if rec['pay'] > 30000]
>> print(payGreat)

# Usefult example to build SQL Query
  >> fields = ['name', 'age', 'job', 'pay']
  >> sue_jones = dict.fromkeys(fields, '%s')
  >> print(sue_jones)
    """
    # --------------------------------------------------------------------
    using_sum_min_max = """>> s = ('ACME', 50, 123.45)
>> print(','.join(str(x) for x in s))                  # ACME,50,123.45

>> portfolio = [{'name': 'GOOG', 'shares': 50},
..              {'name': 'YHOO', 'shares': 75},
..              {'name': 'AOL', 'shares': 20}]

>> sum(x['shares'] for x in portfolio)             # 145
>> min(x['shares'] for x in portfolio)             # 20
>> max(x['shares'] for x in portfolio)             # 75
    """
    # --------------------------------------------------------------------
    # main table data
    table_data = [
        ['Sorting list of dict by common key', sorting_a_list_of_dictionaries_by_common_key],
        ['Sorting with lambda', sorting_with_lambda],
        ['Calculating with dicts', calculating_with_dicts],
        ['Commonalities in Two Dicts', finding_commonalities_in_two_dictionaries],
        ['Dictionary Comprehension', dictionary_comprehension],
        ['Other way to make dicts', other_way_to_make_dicts],
        ['<sum()>, <min()> and <max()>', using_sum_min_max],
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
