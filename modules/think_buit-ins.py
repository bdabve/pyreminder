#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : built-ins.py
#      CREATED : 14-October-2019
#       AUTHOR : daBve, dabve@outlook.fr
#
#         DESC : how to think built-in
#        USAGE : ./built-ins.py
# ====================================================================================================


import csv
import re
from collections import Counter

divider = ('-' * 50)
with open('./think_builtin_example.csv') as csv_f:
    rows = list(csv.DictReader(csv_f, delimiter=';'))

print('[+] len rows and how a row is look like\n'.title())
print(len(rows))
print(rows[0])
print(divider)

# set will give us the unique code
codes = {re.sub(r'-.*', '', row['code']) for row in rows}
article_par_code = Counter(re.sub(r'-.*', '', row['code']) for row in rows)
print('[+] all code in our database\n'.title())
print(codes)
print()
print('{:<8} {}'.format('Code', 'Article'))
print('-------|----------------------------')
for code, counts in article_par_code.items():
    print('{:<7}: {} Articles'.format(code, counts))
print(divider)

# article whos qte == 0
# zero_qte = [row['code'] for row in rows if row['qte'] == '0']    # get only the code
zero_qte = [row for row in rows if row['qte'] == '0']
print('Articles with ZERO qte in stock: {}\n'.format(len(zero_qte)))

code_most_zero = Counter(re.sub(r'-.*', '', row['code']) for row in zero_qte)
print('[+] Article that have zero qte order by code')
print('{:<8} {}'.format('Code', 'Article'))
print('-------|----------------------------')
for code, counts in code_most_zero.items():
    print('{:<7}: {} Articles'.format(code, counts))
print(divider)

# Get BHS articles
aro = [row for row in rows if row['code'].lower().startswith('aro')]
print(aro)
