#!/usr/bin/env python
#
# Author  : el3arbi
# Created :
# Contact : bdabve@gmail.com
# Desc    :
# ----------------------------


def nice_printing(sep: str, msg: str):
    print(sep * 30)
    print(f'## {msg}')
    print(sep * 30)


def hello(name):
    """
    declare a function with parameter name
    this function will print in terminal
    """
    return f'hello {name}'


def calcule(num1: int, num2: int):
    """
    this function will return a num1 + num2 as type int
    :return: return an int sum of 2 nums
    """
    return num1 + num2


name = input('Your name: ')
hello = hello(name)
nice_printing('#', hello)

#
num = int(input('Num 1: '))
num2 = int(input('Num 2: '))
result = f'Your result is: {calcule(num, num2)}'
nice_printing('#', result)

