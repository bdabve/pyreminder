<link rel="stylesheet" href="style.css">

## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [The Zen of Python](#the-zen-of-python)
- [Math Operators](#math-operators)
- [Data Types](#data-types)
- [String Concatenation and Replication](#string-concatenation-and-replication)
- [Variables](#variables)
- [Comments](#comments)
- [The print() Function](#the-print-function)
- [The input() Function](#the-input-function)
- [The len() Function](#the-len-function)
- [The str(), int(), and float() Functions](#the-str-int-and-float-functions)
- [The zip Function](#the-zip-function)
- [The map Function](#the-map-function)
- [The filter function](#the-filter-function)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## Documentation

- [Built-in functions](#https://docs.python.org/3/library/functions.html)

## The Zen of Python

- From the [PEP 20 -- The Zen of Python](https://www.python.org/dev/peps/pep-0020/):

> Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for Python's design into 20 aphorisms, only 19 of which have been written down.

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

[*Return to the Top*](#table-of-content)

## Python Basics

### Math Operators

From **Highest** to **Lowest** precedence:

| Operators | Operation        | Example         |
| --------- | ---------------- | --------------- |
| **        | Exponent         | `2 ** 3 = 8`    |
| %         | Modulus/Remainder| `22 % 8 = 6`    |
| //        | Integer division | `22 // 8 = 2`   |
| /         | Division         | `22 / 8 = 2.75` |
| *         | Multiplication   | `3 * 3 = 9`     |
| -         | Subtraction      | `5 - 2 = 3`     |
| +         | Addition         | `2 + 2 = 4`     |

- Examples of expressions in the interactive shell:

  ```python
  >>> 2 + 3 * 6             # 20
  
  >>> (2 + 3) * 6           # 30
  
  >>> 2 ** 8                # 256
  
  >>> 23 // 7               # 3
  
  >>> 23 % 7                # 2
  
  >>> (5 - 1) * ((7 + 1) / (3 - 1))         # 16.0
  ```


[*Return to the Top*](#table-of-content)

### Data Types

| Data Type              | Examples                                  |
| ---------------------- | ----------------------------------------- |
| Integers               | `-2, -1, 0, 1, 2, 3, 4, 5`                |
| Floating-point numbers | `-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25` |
| Strings                | `'a', 'aa', 'aaa', 'Hello!', '11 cats'`   |

[*Return to the Top*](#table-of-content)

### String Concatenation and Replication

- String concatenation:

  > NOTE: Avoid `+` operator for string concatenation. Prefer string formatting.
  
  ```python
  >>> 'Alice' 'Bob'         # 'AliceBob'
  ```


- String Replication:

  ```python
  >>> 'Alice' * 5       # 'AliceAliceAliceAliceAlice'
  ```

[*Return to the Top*](#table-of-content)

### Variables

You can name a variable anything as long as it obeys the following rules:

1. It can be only one word.
1. It can use only letters, numbers, and the underscore (`_`) character.
1. It can’t begin with a number.
1. Variable name starting with an underscore (`_`) are considered as "unuseful`.

- Example:

  ```python
  >>> spam = 'Hello'
  >>> spam              # 'Hello'
  >>> _spam = 'Hello'
  ```

> `_spam` should not be used again in the code.

[*Return to the Top*](#table-of-content)

### Comments

- Inline comment:

  ```python
  # This is a comment
  ```

- Multiline comment:

  ```Python
  # This is a
  # multiline comment
  ```

- Code with a comment:

  ```python
  a = 1  # initialization
  ```

> Please note the two spaces in front of the comment.

- Function docstring:

  ```python
  def foo():
      """
      This is a function docstring
      You can also use:
      ''' Function Docstring '''
      """
  ```

[*Return to the Top*](#table-of-content)

### The print() Function

```python
>>> print('Hello world!')           # Hello world!
>>>
>>> a = 1
>>> print('Hello world!', a)        # Hello world! 1
```

[*Return to the Top*](#table-of-content)

### The input() Function

- Example Code:

  ```python
  >>> print('What is your name?')   # ask for their name
  >>> myName = input()
  >>> print('It is good to meet you, {}'.format(myName))
  What is your name?
  Al
  It is good to meet you, Al
  ```

[*Return to the Top*](#table-of-content)

### The len() Function

- Evaluates to the integer value of the number of characters in a string:

  ```python
  >>> len('hello')      # 5
  ```

- Note: test of emptiness of strings, lists, dictionary, etc, should **not** use len, but prefer direct boolean evaluation.

  ```python
  >>> a = [1, 2, 3]
  >>> if a:
  ...     print("the list is not empty!")
  ```

[*Return to the Top*](#table-of-content)

### The str(), int(), and float() Functions

- Integer to String or Float:

  ```python
  >>> str(29)       # '29'
  >>> print('I am {} years old.'.format(str(29)))       # I am 29 years old.
  
  >>> str(-3.14)                # '-3.14'
  ```

- Float to Integer:

  ```python
  >>> int(7.7)          # 7
  >>> int(7.7) + 1        # 8
  ```

[*Return to the Top*](#table-of-content)

### The zip Function

- take a series of iterable and aggregates the element from each of them.

    ```python
    >>> names = ['name', 'age', 'pay', 'job']
    >>> values = ['Sue Jones', 45, 4000, 'hdw']
    >>> list(zip(names, values))         
    [OUT] [('name', 'Sue Johnes'), ('Job', 'Software'), ('Pay', 35000), ('Age', 45)]
    >>> dict(zip(names, values))         
    [OUT] {'name': 'Sue Johnes', 'Job': 'Software', 'Pay': 35000, 'Age': 45}
    ```

- Useful with sqlite database

    ```python
    >>> curs.execute('select * from table_name')
    >>> desc = [desc[0] for desc in curs.description]
    >>> dict_object = [dict(zip(desc, row)) for row in curs.fetchall()]
    ```

- use `zip()` to sort values

    ```python
    >>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.75}
    >>> prices_sorted = sorted(zip(prices.values(), prices.keys()))
    >>> print(prices_sorted)            
    [OUT] [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]
    ```

- use `zip()` to loop through two list values, faster and readable.

    ```python
    >>> names = ['name', 'age', 'pay', 'job']
    >>> values = ['Sue Jones', 45, 4000, 'hdw']
    >>> for name, value in zip(names, values):
    ...     print(f'{name}: {value}')
    ```

- zip can be passed more than two sequences as input

    ```python
    >>> a = [1, 2, 3]
    >>> b = [11, 12, 13]
    >>> c = ['x', 'y', 'z']
    >>> for i in zip(a, b, c):
    ...     print(i, end='')            # (1, 11, 'x')(2, 12, 'y')(3, 13, 'z')
    ```

[*Return to the Top*](#table-of-content)

### The map function

- used to apply a function on all the elements of specified iterable and return map object.

    ```python
    >>> def to_upper(s):
    ...     return str(s).upper()

    >>> map_iterator = map(to_upper, 'abc')
    >>> for s in map_iterator:
    ...     print(s, end='')                        # A B C

    >>> map_carre = map(lambda n: n**2, [1, 2, 3, 4])
    >>> print(list(map_carre))                      # [1, 4, 9, 6]

    >>> m_list = ['Dabve', 33, 4500]
    >>> print(', '.join(map(str, m_list)))          # Dabve, 33, 4500
    ```

[*Return to the Top*](#table-of-content)

### The filter function

```python
>>> languages = ["HTML", "JavaScript", "Python", "Ruby"]
>>> print(list(filter(lambda x: x == "Python", languages)))       # 'Python'

>>> lst_files = ['file.txt', 'file.csv', 'file.xlsx', 'file1.csv', 'etat.csv']
>>> from fnmatch import fnmatch
>>> print(list(filter(lambda x: fnmatch(x, '*.csv'), lang)))  # ['file.csv', 'file1.csv', 'etat.csv']

>>> squares = [i**2 for i in range(1, 11)]
>>> print(list(filter(lambda x: x >= 30 and x <= 70, squares)))   # [16, 25, 36, 49, 64]

>>> garbled = "IXXX aXXmX aXXnXoXXXXtXhXeXXXrX sXXXeXcXXrXeXt mXXeXsXXsXaXXXgXeX!XX"
>>> message = filter(lambda x: x != "X", garbled)                      # <filter object at 0x7f0d3ab547b8>
>>> msg = ''.join(map(str, list(filter(lambda x: x!= 'X', garbled))))  # 'I am another secret message!'
```
