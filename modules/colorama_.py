#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE     : colorama_.py
AUTHOR   : daBve, dabve@gmail.com
CREATED  :
UPDATED  : 21-August-2020
-----------------------------------------------------
DESC     : How to use colorama
-----------------------------------------------------
"""

from terminaltables import AsciiTable


def main():
    title = ' Colorama '

    colorama_ = """
from colorama import init
from colorama import Fore, Back, Style

init()          # initialise Colorama

reset = Style.RESET_ALL     # reset colors to normal

print(Fore.RED + 'Red Text' + reset)
print(Back.GREEN + 'Green Background' + reset)
print(Style.DIM + 'Dim Text' + reset)
print('\\033[31mRed text\\033[39m')           # like in bash

# Available formatting constants:
    # Fore and Back:
        BLACK
        RED
        GREEN
        YELLOW
        BLUE
        MAGENTA
        CYAN
        WHITE
        RESET.
    # Style:
        DIM
        NORMAL
        BRIGHT
        RESET_ALL

init(autoreset=True): sending reset sequences to turn off color changes at the end.
    """.format()

    table_data = [
        ['colorama usage', colorama_],
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
    content = func()
    for line in content:
        yield [('', line)]


if __name__ == '__main__':
    from pypager.source import GeneratorSource
    from pypager.pager import Pager

    p = Pager()                                         # create the pager
    source = GeneratorSource(generate_content(main))    # generate the source
    p.add_source(source)                                # add the content to the Pager
    p.run()
