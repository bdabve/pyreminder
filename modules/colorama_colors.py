#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE     : colorama_colors.py
AUTHOR   : daBve, dabve@gmail.com
CREATED  : 21-August-2020
DESC     : colors in colorama
-----------------------------------------------------
"""

from colorama import init
from colorama import Fore, Back, Style

init(autoreset=True)

color_list = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
style_list = ['DIM', 'NORMAL', 'BRIGHT']

print('|---- Fore Colors ----|')
print('| {}{}'.format(Fore.BLACK, 'black'))
print('| {}{}'.format(Fore.RED, 'red'))
print('| {}{}'.format(Fore.GREEN, 'green'))
print('| {}{}'.format(Fore.YELLOW, 'yellow'))
print('| {}{}'.format(Fore.BLUE, 'blue'))
print('| {}{}'.format(Fore.MAGENTA, 'magenta'))
print('| {}{}'.format(Fore.CYAN, 'cyan'))
print('| {}{}'.format(Fore.WHITE, 'white'))

print('|---- Background Colors ----|')
print('| {}{} Back'.format(Back.BLACK, 'black'))
print('| {}{} Back'.format(Back.RED, 'red'))
print('| {}{} Back'.format(Back.GREEN, 'green'))
print('| {}{}'.format(Back.YELLOW, 'yellow'))
print('| {}{}'.format(Back.BLUE, 'blue'))
print('| {}{}'.format(Back.MAGENTA, 'magenta'))
print('| {}{}'.format(Back.CYAN, 'cyan'))
print('| {}{}'.format(Back.WHITE, 'white'))

print('|---- Style ----|')
print('| {0}Dim Style'.format(Style.DIM))
print('| {0}Normal Style'.format(Style.NORMAL))
print('| {0}Bright Style'.format(Style.BRIGHT))
