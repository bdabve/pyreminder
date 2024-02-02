<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of content

- [Ternary Conditional Operator](#ternary-conditional-operator)

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## Lambda Functions

- This function:

    ```python
    >>> def add(x, y):
    ...     return x + y
    >>> add(5, 3)       # 8
    ```

- Is equivalent to the *lambda* function:

    ```python
    >>> add = lambda x, y: x + y
    >>> add(5, 3)       # 8
    ```

- It's not even need to bind it to a name like add before:

    ```python
    >>> (lambda x, y: x + y)(5, 3)          # 8
    ```

- Like regular nested functions, lambdas also work as lexical closures:

    ```python
    >>> def make_adder(n):
    ...     return lambda x: x + n

    >>> plus_3 = make_adder(3)
    >>> plus_5 = make_adder(5)

    >>> plus_3(4)       # 7
    >>> plus_5(4)       # 9
    ```

> NOTE: lambda can only evaluate an expression, like a single line of code.

[*Return to the Top*](#table-of-content)

## Ternary Conditional Operator

- Many programming languages have a ternary operator, which define a conditional expression. 
- The most common usage is to make a terse simple conditional assignment statement. 
- In other words, it offers one-line code to evaluate the first expression if the condition is true, otherwise it evaluates the second expression.

    <expression1> if <condition> else <expression2>

- Example:

    ```python
    >>> age = 15
    >>> print('kid' if age < 18 else 'adult')           # kid
    ```

- Ternary operators can be chained:

    ```python
    >>> age = 15
    >>> print('kid' if age < 13 else 'teenager' if age < 18 else 'adult')       # teenager
    ```

- The code above is equivalent to:

    ```python
    >>> if age < 18:
    ...     if age < 13:
    ...         print('kid')
    ...     else:
    ...         print('teenager')
    ... else:
    ...     print('adult')
    ```

- More example

    ```python
    >>> a, b = 10, 20
    >>> print('a and b are equal' if a == b else 'a is greater than b' if a > b else 'b is greater than a')
    >>> b is greater than a
    ```

[*Return to the Top*](#table-of-content)
