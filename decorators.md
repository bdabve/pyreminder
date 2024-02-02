<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Understandind decorators](#understanding-decorators)
- [Decorator Functions that Accept Arguments](#decorator-functions-that-accept-arguments)
- [Write Debuggable Decorators](#write-debuggable-decorators)

***

- [LINUX Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [WINDOWS Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/windows_main.md)

### Understanding decorators

- Decorator: 'decorate' or 'wrap' another function and let you execute code before and after the wrapped function runs.
- Decorators: allow you to define reusable building blocks that can change or extend the behavior of other functions.
- And, they let you do that without permanently modifying the wrapped function itself.
- The function’s behavior changes only when it’s decorated.

    ```python
    >>> def strong(func):
    ...     def wrapper():
    ...         return '<storng>' + func() + '</strong>'
    ...     return wrapper

    ... def emphasis(func):
    ...     def wrapper():
    ...         return '<em>' + func() + '</em>'
    ...     return wrapper

    ... @strong
    ... @emphasis
    ... def greet():
    ...     return 'Hello HTML!'            # <strong><em>Hello HTML!</em></strong>
    ```

- This is equal to: strong(emphasis(greet))
- The order from bottom to top

    ```python
    >>> @emphasis
    >>> @strong
    >>> def greet():
    ...     return 'Hello HTML!'            # OUT: <em><strong>Hello HTML!</strong></em>
    ```

[*Return to the Top*](#table-of-content)

## Decorator Functions that Accept Arguments

```python
>>> def trace(func):
...     def wrapper(*args, **kwargs):
...         print('TRACE: calling {} with {}, {}'.format(func.__name__, args, kwargs))
...         original_result = func(*args, **kwargs)
...         print('TRACE: {} returning {!r}'.format(func.__name__, original_result))
...         return original_result
...     return wrapper

>>> @trace
>>> def say(name, line):
...     return f'{name}: {line}'
```

[*Return to the Top*](#table-of-content)

### Write 'Debuggable' Decorators

- You can use < functools.wraps > in your own decorators to copy over the lost metadata from the undecorated function to the decorator closure.

    ```python
    >>> @strong
    >>> def greet():
    ...    '''Return a friendly greeting'''
    ...    return 'Hello!'

    >>> print(greet.__name__)         # wrapper
    >>> print(greet.__doc__)          # None

    >>> import functools
    >>> def strong(func):
    ...     @functools.wraps(func)
    ...     def wrapper():
    ...         return '<storng>' + func() + '</strong>'
    ...     return wrapper

    >>> @strong
    >>> def greet():
    ...     '''Return a friendly greeting'''
    ...     return 'Hello!'

    >>> print(greet.__name__)             # greet
    >>> print(greet.__doc__)              # Return a friendly greeting
    ```
