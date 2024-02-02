<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Return Values and return Statements](#return-values-and-return-statements)
- [The None Value](#the-none-value)
- [Keyword Arguments and print()](#keyword-arguments-and-print)
- [Local and Global Scope](#local-and-global-scope)
- [The global Statement](#the-global-statement)

***
- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## Functions

```python
>>> def hello(name):
>>>     print('hello {}'.format(name))
>>>
>>> hello('alice')
>>> hello('bob')
hello alice
hello bob
```

[*Return to the Top*](#table-of-content)

### Return Values and return Statements

When creating a function using the def statement, you can specify what the return value should be with a return statement. A return statement consists of the following:

- The return keyword.

- The value or expression that the function should return.

    ```python
    import random
    def getAnswer(answerNumber):
        if answerNumber == 1:
            return 'It is certain'
        elif answerNumber == 2:
            return 'It is decidedly so'
        elif answerNumber == 3:
            return 'Yes'
        elif answerNumber == 4:
            return 'Reply hazy try again'
        elif answerNumber == 5:
            return 'Ask again later'
        elif answerNumber == 6:
            return 'Concentrate and ask again'
        elif answerNumber == 7:
            return 'My reply is no'
        elif answerNumber == 8:
            return 'Outlook not so good'
        elif answerNumber == 9:
            return 'Very doubtful'

    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)
    ```

[*Return to the Top*](#table-of-content)

### The None Value

```python
>>> spam = print('Hello!')
Hello!
```

```python
>>> spam is None
True
```

Note: never compare to `None` with the `==` operator. Always use `is`.

[*Return to the Top*](#table-of-content)

### Keyword Arguments and print()

```python
>>> print('Hello', end='')
>>> print('World')
HelloWorld
```

```python
>>> print('cats', 'dogs', 'mice')
cats dogs mice
```

```python
>>> print('cats', 'dogs', 'mice', sep=',')
cats,dogs,mice
```

[*Return to the Top*](#table-of-content)

### Local and Global Scope

- Code in the global scope cannot use any local variables.

- However, a local scope can access global variables.

- Code in a function’s local scope cannot use variables in any other local scope.

- You can use the same name for different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.

[*Return to the Top*](#table-of-content)

### The global Statement

If you need to modify a global variable from within a function, use the global statement:

```python
>>> def spam():
>>>     global eggs
>>>     eggs = 'spam'
>>>
>>> eggs = 'global'
>>> spam()
>>> print(eggs)
spam
```

There are four rules to tell whether a variable is in a local scope or global scope:

1. If a variable is being used in the global scope (that is, outside of all functions), then it is always a global variable.

1. If there is a global statement for that variable in a function, it is a global variable.

1. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable.

1. But if the variable is not used in an assignment statement, it is a global variable.

[*Return to the Top*](#table-of-content)


- calculation with the decimal numbers. Prevent the small ERRORS that naturaly occur with floats.

    ```python
    >>> from decimal import Decimal, localcontext
    >>> def tva(valeur:Decimal, tva:Decimal=1.7) -> Decimal:
    ...     '''
    ...     - This function claculate TVA, default TVA value = 17%
    ...     - Type of parameter decimal.
    ...     '''
    ...     with localcontext() as ctx:
    ...         ctx.prec = 3
    ...         return valeur * tva
    ```

### `*args` and `**kwargs`.

- `*args`    : collects extra positional arguments as a tuple.
- `**kwargs` : collects the extra keyword arguments as a dictionary.

    ```python
    >>> def build_profile(first, last, **user_info):
    ...     '''Build a dictionary containing everthing we know about a user.'''
    ...     profile = {}
    ...     profile['first_name'] = first
    ...     profile['last_name'] = last
    ...     return profile

    >>> user_profile = build_profile('username', 'email', 'phone', job='pricceton', address='physics')
    ```
