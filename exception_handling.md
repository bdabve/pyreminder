<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Basic exception handling](#basic-exception-handling)
- [Multiple Exceptions](#multiple-exceptions)
- [The else statement](#the-else-statement)
- [Final code in exception handling](#final-code-in-exception-handling)
- [Exception Hierarchy](#exception-hierarchy)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)


## Exception Handling

### Basic exception handling

```python
>>> def spam(divideBy):
>>>     try:
>>>         return 42 / divideBy
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>>
>>> print(spam(2))
>>> print(spam(12))
>>> print(spam(0))
>>> print(spam(1))
21.0
3.5
Error: Invalid argument: division by zero
None
42.0
```

[*Return to the Top*](#table-of-content)

### Multiple Exceptions

```python
>>> try:
...     '2' + 2
...     4 + spam
...     10 / 0
... except (ZeroDivisionError, TypeError, NameError) as err:
...     print('[-] Error: {}'.format(err))

>>> import sys
>>> try:
...     f = open('myfile.txt')
...     s = f.readline()
...     i = int(s.strip())
... except OSError as err:
...     print("OS error: {0}".format(err))
... except ValueError:
...     print("Could not convert data to an integer.")
... except:
...     print("Unexpected error:", sys.exc_info()[0])
...     raise

>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
... # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
# OUTPUT
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

[*Return to the Top*](#table-of-content)

### The else statement

- if all go right the else will be excuted

    ```python
    >>> try:
    ...     f = open('test.txt')
    ... except:
    ...     print("Sorry, This file does not exist")
    ... else:
    ...     print(f.read())
    ...     f.close()
    ```

[*Return to the Top*](#table-of-content)

### Final code in exception handling

Code inside the `finally` section is always executed, no matter if an exception has been raised or
not, and even if an exception is not caught.

```python
>>> def spam(divideBy):
>>>     try:
>>>         return 42 / divideBy
>>>     except ZeroDivisionError as e:
>>>         print('Error: Invalid argument: {}'.format(e))
>>>     finally:
>>>         print("-- division finished --")
>>> print(spam(12))
>>> print(spam(0))
21.0
-- division finished --
3.5
-- division finished --
Error: Invalid argument: division by zero
-- division finished --
None
-- division finished --
42.0
-- division finished --
```

[*Return to the Top*](#table-of-content)

### Exception Hierarchy

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```
