#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi el3arbi_@email.com
# created       : 08-June-2022
#
# description   : how to use terminaltables
#                 for more usefull tables and more control see cli_helpers module
# -------------------------------------------------------------------------------

import terminaltables

headers = ['id', 'code', 'designation', 'quantity', 'prix', 'valeur']
data = [
    ['1', 'aro-001', 'Joint Torique', 10, 650, 6500],
    ['2', 'aro-002', 'Filtre D\'Ai Comprime Dd 150', 12, 12000, 144000],
    ['3', 'aro-003', 'Sonde de Temperature', 2, 15357.14, 30714.28],
    ['4', 'aro-004', 'Kit Pour Separateur', 6, 5714.29, 34285.74],
    ['5', 'aro-005', 'Purgeur', 4, 55000, 220000],
    ['6', 'aro-006', 'Pressostat', 6, 13000, 78000],
    ['7', 'aro-007', 'Kit Valve de Secheur', 1, 106543.21, 106543.21],
    ['8', 'aro-008', 'Pressure Transmitteur', 1, 40000, 40000],
    ['9', 'aro-009', 'Lame ( Couteau Circulaire )', 23, 7000, 161000],
    ['10', 'aro-010', 'Raccordeur (Connection de Gamme)', 1, 100000, 100000],
]

# AsciiTable
table_data = [list(row.title() for row in headers)]
for row in data:
    table_data.append(list(map(str, row)))

asci_table = terminaltables.AsciiTable(table_data)
print(asci_table.table)

# GithubFlavoredMarkdownTable
print()
github_table = terminaltables.GithubFlavoredMarkdownTable(table_data)
print(github_table.table)

# PorcelaineTable
print()
porcelain_table = terminaltables.PorcelainTable(table_data)
porcelain_table.inner_heading_row_border = True                 # add a line between rows
# porcelain_table.inner_footing_row_border = True               # this is usefull if a total row is present
# porcelain_table.outer_border                                  # True to add outer border
print(porcelain_table.table)

# DoubleTable
print()
double_table = terminaltables.DoubleTable(table_data)
print(double_table.table)

# SingleTable
print()
single_table = terminaltables.SingleTable(table_data)
single_table.justify_columns = {3: 'center', 4: 'right', 5: 'right'}        # Justify Columns By Index Start From 0
single_table.title = 'Aro Products'                                         # Add a Title
single_table.padding_left = 2                                               # Padding Left
single_table.padding_right = 2                                              # Padding Right
single_table.inner_row_border = True                                        # add a line between rows
print('(+) Table Fits Terminal:', single_table.ok)  # True if the table fits within the terminal width, False if table breaks.
print(single_table.table)
