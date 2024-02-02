#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# FILE     : cli_helpers.py
# CREATED  : 11-August-2020
# AUTHOR   : daBve, dabve@outlook.fr
# USAGE    : ./cli_helpers.py
# ---------------------------------------
# DESC     : CLI Helpers provides a simple way to display your tabular data
#            (columns/rows) in a visually-appealing manner
# --------------------------------------------------------------------------

from cli_helpers import tabular_output
from cli_helpers.tabular_output import TabularOutputFormatter

print("""
# ---------------------------------------------------
# THIS FILE DEMONSTRATE HOW TO USE cli_helpers MODULE
# ---------------------------------------------------
""")
formatter = TabularOutputFormatter()
formats = formatter.supported_formats

data = [
    [1, 'Asgard', True],
    [2, 'Camelot', False],
    [3, 'El Dorado', True]
]
headers = ['id', 'city', 'visited']

# Truncate string
# This functions return a tuple(data, headers)
# data, headers = tabular_output.preprocessors.truncate_string(data, headers, max_field_width=20)   # truncate text
# data, headers = tabular_output.preprocessors.escape_newlines(data, headers)                       # escape newline char


for format_ in formats:
    print()
    print('(+) FORMAT = ' + format_)
    print()
    for row in tabular_output.format_output(data, headers, format_name=format_):
        print(row)
