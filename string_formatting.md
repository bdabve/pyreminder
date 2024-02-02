<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

# Table of Content

- [% operator](#operator)
- [String Formatting (str.format)](#string-formatting-strformat)
- [Lazy string formatting](#lazy-string-formatting)
- [Formatted String Literals or f-strings (Python 3.6+)](#formatted-string-literals-or-f-strings-python-36)
- [Template Strings](#template-strings)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## String Formatting

### % operator

```python
>>> name = 'Pete'
>>> 'Hello %s' % name           # "Hello Pete"
```

- We can use the `%x` format specifier to convert an int value to a string:

    ```python
    >>> num = 5
    >>> 'I have %x apples' % num            # "I have 5 apples"
    ```

Note: For new code, using [str.format](#string-formatting-strformat) or [f-strings](#formatted-string-literals-or-f-strings-python-36) (Python 3.6+) is strongly recommended over the `%` operator.

[*Return to the Top*](#table-of-content)

### String Formatting (str.format)

- Python 3 introduced a new way to do string formatting that was later back-ported to Python 2.7. This makes the syntax for string formatting more regular.

    ```python
    >>> name = 'John'
    >>> age = 20'

    >>> "Hello I'm {}, my age is {}".format(name, age)          # "Hello I'm John, my age is 20"
    >>> "Hello I'm {0}, my age is {1}".format(name, age)        # "Hello I'm John, my age is 20"
    
    >>> tag = 'h1'
    >>> text = 'This is a headline'
    >>> print('<{0}>{1}</{0}>'.format(tag, text))
    ```

- with dicts:

  ```python
  >>> person = {'name': 'dabve', 'os': 'ubuntu', 'age': 30}
  >>> 'Name is {0} and i am {1}'.format(person['name'], person['age'])      # Name is dabve and i am 30
  >>> 'Name is {0[name]} and i am {0[age]}'.format(person)                  # Name is dabve and i am 30 
  >>> 'Name is {p[name]} and i am {p[age]}'.format(p=person)                # Name is dabve and i am 30 
  >>> 'Name is {name} and i am {age}'.format(**person)                      # Name is dabve and i am 30 
  ```

- with list

  ```python
  >>> my_list = ['Dabve', 33]
  >>> print("My name is {0[0]} and i am {0[1]} years old".format(my_list))
  
  >>> print('Best books for "{language}" is "{book}"'.format(language='Pyhton', book='Python Cookbook'))
  ```

- Classes

  ```python
  >>> class Person():
  ...     def __init__(self, first, last):
  ...        self.first = first
  ...        self.last = last

  >>> dabve = Person('Dabve', 'Band')
  >>> print('Person Details: {0.first} {0.last}'.format(dabve))
  ```

- Align Text

  ```python
  >>> 'Align Right: {:>10}'.format(person['name'])
  >>> '{:<10} Align Left'.format(person['name'])
  >>> '{:_<10} Align Left with padding chars'.format(person['name'])
  >>> '{:^10} Center'.format(person['name'])

  >>> 'Truncate the word "truncating" to 5 chars: "{:.5}"'.format('truncating')
  >>> "Truncating: truncating to 5 chars and padd : {:>10.5}".format('truncating')
  >>> "Parametrized alignment and width: {:{align}{width}}".format('Test', align='^', width='10')
  ```

- Numbers

  ```python
  >>>'Number: {:d}'.format(42)                                      # Number: 42
  >>>'Positiv number: {:+d}'.format(42)                             # Positive Number: +42
  
  >>>'Control the sign: {:=+4d}'.format(42)                         # Control the sign: + 42
  >>>'Control the sign: {:+10d}'.format(42)                         # 'Control the sign:      +42'
  >>>'Control the sign: {:=4d}'.format(-42)                         # Control the sign: - 42
 
  >>>'Add Padding to number: {:10d}'.format(500)                    # Add Padding to number:      500
  >>>'Make it to 6 chars and 2 after comma: {:06.3f}'.format(1.123456789)         # 01.123

  >>> for nb in range(3):
  ...     print('Number: {:02}'.format(nb), end='')   # 00 03 04

  >>> 'PI is equal to: {:.2f}'.format(3.14159265)         # PI is equal to: 3.14
  >>> '1 MB is equal to : {:,} bytes'.format(1000**2)     # 1 MB is equal to: 1,000,000 bytes

  >>> x = 1234.56789            
  >>> format(x, '0.2f')             # 1234.57
  >>> format(x, '>10.1f')           # '    1234.6'
  >>> format(x, ':>10.2f')          # ':::1234.57'
  >>> format(x, '^10.1f')           # '  1234.6  '
  >>> format(x, ',')                # '1,234.56789'
  >>> format(x, '0,.2f')            # '1,234.57'
  ```

The official [Python 3.x documentation](https://docs.python.org/3/library/stdtypes.html?highlight=sprintf#printf-style-string-formatting) recommend `str.format` over the `%` operator:

> The formatting operations described here exhibit a variety of quirks that lead to a number of common errors (such as failing to display tuples and dictionaries correctly). Using the newer formatted string literals or the str.format() interface helps avoid these errors. These alternatives also provide more powerful, flexible and extensible approaches to formatting text.

[*Return to the Top*](#table-of-content)

### Lazy string formatting

- You would only use `%s` string formatting on functions that can do lazy parameters evaluation, the most common being logging:

- Prefer:

    ```python
    >>> name = "alice"
    >>> logging.debug("User name: %s", name)
    ```

- Over:

    ```python
    >>> logging.debug("User name: {}".format(name))
    ```

- Or:

    ```python
    >>> logging.debug("User name: " + name)
    ```

[*Return to the Top*](#table-of-content)

### Formatted String Literals or f-strings (Python 3.6+)

```python
>>> name = 'Elizabeth'
>>> f'Hello {name}!'            # 'Hello Elizabeth!
```

- It is even possible to do inline arithmetic with it:

    ```python
    >>> a = 5
    >>> b = 10
    >>> f'Five plus ten is {a + b} and not {2 * (a + b)}.'          # 'Five plus ten is 15 and not 30.'
    ```

- More examples

    ```python
    >>> var = math.pi
    >>> print(f'Using Numeric {Variable = }')       # Using Numeric Variable 3.141592653589793
    >>> print(f'|{var:25}|')                        # |        3.141592653589793|
    >>> print(f'|{var:<25}|')                       # |3.141592653589793        |
    >>> print(f'|{var:>25}|')                       # |        3.141592653589793|
    >>> print(f'|{var:^25}|')                       # |    3.141592653589793    |
    >>>
    >>> print(f'{var:.^25}')                        # 3.141592653589793========
    >>> print(f'{var:=>25}')                        # ========3.141592653589793
    >>> print(f'{var:.<25}')                        # ....3.141592653589793....
    ```

[*Return to the Top*](#table-of-content)

### Template Strings

- A simpler and less powerful mechanism, but it is recommended when handling format strings generated by users. Due to their reduced complexity template strings are a safer choice.

    ```python
    >>> from string import Template
    >>> name = 'Elizabeth'
    >>> t = Template('Hey $name!')
    >>> t.substitute(name=name)             # 'Hey Elizabeth!'
    ```
[*Return to the Top*](#table-of-content)
