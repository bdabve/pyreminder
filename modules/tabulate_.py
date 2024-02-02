#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =========================================
#  FILE     :tabulate_.py
#  CREATED  : 10-août-2020
#  AUTHOR   : daBve, dabve@outlook.fr
#  DESC     :
#  USAGE    : ./tabulate_.py
# =========================================


from tabulate import tabulate

print("""
# -------------------------------
# => How to use tabulate Module
# -------------------------------
        """)
headers = ['Name', 'Job', 'Age', 'Salarie']
table = [
    ['Dabve', 'Magasinier', 35, 35000],
    ['Dave', 'Python Dev', 60, 40000],
    ['John', 'None', 55, 55000],
]

print(tabulate(table, headers=headers))

# headers = first row
print()
print('-' * 100)
table = [
    ['Name', 'Job', 'Age', 'Salarie'],
    ['Dabve', 'Magasinier', 35, 35000],
    ['Dave', 'Python Dev', 60, 40000],
    ['John', 'None', 55, 55000],
]
print(tabulate(table, headers='firstrow'))

# if headers = keys; then the keys of a dict are used
print()
print('-' * 100)
names = {'Name': ['Alice', 'Bob'], 'Age': [45, 50]}
print(tabulate(names, headers='keys'))

# Table format
table_fmt = ['plain', 'simple', 'github', 'grid', 'fancy_grid', 'pipe', 'orgtbl', 'jira', 'presto', 'pretty', 'psql', 'rst',
             'mediawiki', 'moinmoin', 'youtrack', 'html', 'latex', 'latex_row', 'latex_booktabs', 'textile']
print()
print('# tablefmt: defines how the table is formatted')
for fmt in table_fmt:
    print('\n# {0} {1} {0}\n'.format(('_' * 3), 'tablefmt=' + fmt))
    names = {'Name': ['Alice', 'Bob'], 'Age': [45, 50]}
    print(tabulate(names, headers='keys', tablefmt=fmt))


# column alignment
table = [[1.2345], [1234.45], [12.3456], [123456], [123456789], [12345.6]]
print()
print('# numalign: override the default alignment')
print('# Possible alignement are: right, center, left, decimal')
print('# ___ Default alignement ___')
print(tabulate(table))
print()
print('# ___ numalign="right" ___')
print(tabulate(table, numalign="right"))
print()
print('# ___ numalign="left" ___')
print(tabulate(table, numalign="left"))

# custom column alignment
table = [['one', 'two'], ['three', 'four']]
print()
print('# custom column alignement; the colalign can be a list or a tuple')
print('# Possible alignement are: right, center, left, decimal')
print('# ___ colalign=("right",) ___')
print(tabulate(table, colalign=('right', )))

# Number formatting
table = [['pi', 3.141593], ['e', 2.718282]]
print()
print('# custom number formatting applied to all columns of decimal numbers.')
print('# ___ floatfmt=".4f" ___')
print(tabulate(table, floatfmt='.4f'))

table = [[0.123456, 0.123456, 0.123456]]
print()
print('# floatfmt can be a list or tuple of format strings.')
print('# ___ floatfmt=(".1f", ".3f") ___')
print(tabulate(table, floatfmt=('.1f', '.3f')))
