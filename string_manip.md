<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content
- [Escape Characters](#escape-characters)
- [Raw Strings](#raw-strings)
- [Multiline Strings with Triple Quotes](#multiline-strings-with-triple-quotes)
- [Indexing and Slicing Strings](#indexing-and-slicing-strings)
- [The in and not in Operators with Strings](#the-in-and-not-in-operators-with-strings)
- [The in and not in Operators with list](#the-in-and-not-in-operators-with-list)
- [The upper(), lower(), isupper(), and islower() String Methods](#the-upper-lower-isupper-and-islower-string-methods)
- [The isX String Methods](#the-isx-string-methods)
- [The startswith() and endswith() String Methods](#the-startswith-and-endswith-string-methods)
- [Find and Replace string](#find-and-replace-string)
- [The join() and split() String Methods](#the-join-and-split-string-methods)
- [Justifying Text with rjust(), ljust(), and center()](#justifying-text-with-rjust-ljust-and-center)
- [Removing Whitespace with strip(), rstrip(), and lstrip()](#removing-whitespace-with-strip-rstrip-and-lstrip)
- [Copying and Pasting Strings with the pyperclip Module (need pip install)](#copying-and-pasting-strings-with-the-pyperclip-module-need-pip-install)
- [Reformatting Text With textwrap](#reformatting-text-with-textwrap)
- [Performing I/O Operations on a string](#performing-io-operations)

## Manipulating Strings

### Escape Characters

| Escape character | Prints as            |
| ---------------- | -------------------- |
| `\'`             | Single quote         |
| `\"`             | Double quote         |
| `\t`             | Tab                  |
| `\n`             | Newline (line break) |
| `\\`             | Backslash            |

- Example:

  ```python
  >>> print("Hello there!\nHow are you?\nI\'m doing fine.")
  Hello there!
  How are you?
  I'm doing fine.
  ```

[*Return to the Top*](#table-of-content)

### Raw Strings

- A raw string completely ignores all escape characters and prints any backslash that appears in the string.

  ```python
  >>> print(r'That is Carol\'s cat.')
  That is Carol\'s cat.
  ```

- Note: mostly used for regular expression definition (see `re` package)

[*Return to the Top*](#table-of-content)

### Multiline Strings with Triple Quotes

  ```python
  >>> print('''Dear Alice,
  >>>
  >>> Eve's cat has been arrested for catnapping, cat burglary, and extortion.
  >>>
  >>> Sincerely,
  >>> Bob''')
  Dear Alice,

  Eve's cat has been arrested for catnapping, cat burglary, and extortion.

  Sincerely,
  Bob
  ```

- To keep a nicer flow in your code, you can use the `dedent` function from the `textwrap` standard package.

  ```python
  >>> from textwrap import dedent
  >>>
  >>> def my_function():
  ...     print('''
  ...         Dear Alice,
  ...
  ...         Eve's cat has been arrested for catnapping, cat burglary, and extortion.
  ...
  ...         Sincerely,
  ...         Bob
  ...         ''').strip()
  ```

This generates the same string than before.

[*Return to the Top*](#table-of-content)

### Indexing and Slicing Strings

    H   e   l   l   o       w   o   r   l   d    !
    0   1   2   3   4   5   6   7   8   9   10   11

```python
>>> spam = 'Hello world!'

>>> spam[0]             # 'H'
>>> spam[4]             # 'o'
>>> spam[-1]            # '!'
```

- Slicing:

  ```python
  >>> spam[0:5]             # 'Hello'
  >>> spam[:5]              # 'Hello'
  >>> spam[6:]              # 'world!'
  >>> spam[6:-1]            # 'world'
  >>> spam[:-1]             # 'Hello world'
  >>> spam[::-1]            # '!dlrow olleH'
  
  >>> spam = 'Hello world!'
  >>> fizz = spam[0:5]
  >>> fizz                  # 'Hello'
  ```

[*Return to the Top*](#table-of-content)

### The in and not in Operators with Strings

```python
>>> 'Hello' in 'Hello World'            # True
>>> 'Hello' in 'Hello'                  # True
>>> 'HELLO' in 'Hello World'            # False
>>> '' in 'spam'                        # True
>>> 'cats' not in 'cats and dogs'       # False
```

### The in and not in Operators with list

```python
>>> a = [1, 2, 3, 4]
>>> 5 in a              # False
>>> 2 in a              # True
```

[*Return to the Top*](#table-of-content)

### The upper(), lower(), isupper(), and islower() String Methods

- `upper()` and `lower()`:

  ```python
  >>> spam = 'Hello world!'
  >>> spam = spam.upper()
  >>> spam                      # 'HELLO WORLD!'
  
  >>> spam = spam.lower()
  >>> spam                      # 'hello world!'
  ```

- `isupper()` and `islower()`:

  ```python
  >>> spam = 'Hello world!'
  >>> spam.islower()                # False
  >>> spam.isupper()                # False
  >>> 'HELLO'.isupper()             # True
  >>> 'abc12345'.islower()          # True
  >>> '12345'.islower()             # False
  >>> '12345'.isupper()             # False
  ```

[*Return to the Top*](#table-of-content)

### The isX String Methods

- **isalpha()** returns `True` if the string consists only of letters and is not blank.
- **isalnum()** returns `True` if the string consists only of lettersand numbers and is not blank.
- **isdecimal()** returns `True` if the string consists only ofnumeric characters and is not blank.
- **isspace()** returns `True` if the string consists only of spaces,tabs, and new-lines and is not blank.
- **istitle()** returns `True` if the string consists only of wordsthat begin with an uppercase letter followed by onlylowercase letters.


- Usefull script to validate age and passwd

  ```python
  >>> while True:
  ...     age = input('Enter your age: ')
  ...     if age.isdecimal():
  ...         break
  ...     print('Please enter a number for your age.')

  >>> while True:
  ...     password = input('Select a new password(letters and numbers only): ')
  ...     if password.isalnum():
  ...         break
  ...     print('Passwords can only have letters and numbers.')
  ```

[*Return to the Top*](#table-of-content)

### The startswith() and endswith() String Methods

```python
>>> 'Hello world!'.startswith('Hello')                  # True
>>> 'Hello world!'.endswith('world!')                   # True
>>> 'abc123'.startswith('abcdef')                       # False
>>> 'abc123'.endswith('12')                             # False
>>> 'Hello world!'.startswith('Hello world!')           # True
>>> 'Hello world!'.endswith('Hello world!')             # True

>>>  choices = ['http:', 'ftp:', 'https:']
>>> url = 'http://www.python.org'
>>> url.startswith(choices)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: startswith first arg must be str or a tuple of str, not list
startswith first arg must be str or a tuple of str, not list

# you must convert the choices list or declare it as a tuple
>>> url.startswith(tuple(choices))                          # True
```

[*Return to the Top*](#table-of-content)

### Find and Replace string

```python
>>> text = 'yeah, but no, but yeah, but no, but yeah'
>>> text.find('no')                       # 10
>>> text.replace('yeah', 'yep')           # yep, but no, but yep, but no, but yep
```

[*Return to the Top*](#table-of-content)

### The join() and split() String Methods

- `join()`: called on a string value and passed a list value

  ```python
  >>> ', '.join(['cats', 'rats', 'bats'])             # 'cats, rats, bats'
  >>> ' '.join(['My', 'name', 'is', 'Simon'])         # 'My name is Simon'
  >>> 'ABC'.join(['My', 'name', 'is', 'Simon'])       # 'MyABCnameABCisABCSimon'
  ```
- The problem `str.join()` is that it only works with strings.

  ```python
  >>> row = ('ACME', 50, 91.5)
  >>> ', '.join(str(x) for x in row)          # ACME, 50, 91.5
  >>> print(*row, sep=',')                    # ACME,50,91.5
  >>> '{}'.format(','.join(map(str, row)))    # ACME,50,91.5
  ```

- `split()`: is called on a string and return a list

  ```python
  >>> 'My name is Simon'.split()              # ['My', 'name', 'is', 'Simon']
  >>> 'MyABCnameABCisABCSimon'.split('ABC')   # ['My', 'name', 'is', 'Simon']
  >>> 'My name is Simon'.split('m')           # ['My na', 'e is Si', 'on']
  ```

[*Return to the Top*](#table-of-content)

### Justifying Text with rjust(), ljust(), and center()

rjust() and ljust():

```python
>>> 'Hello'.rjust(10)           # '     Hello'
>>> 'Hello'.rjust(20)           # '               Hello'
>>> 'Hello World'.rjust(20)     # '         Hello World'
>>> 'Hello'.ljust(10)           # 'Hello     '
```

- An optional second argument to `rjust()` and `ljust()` will specify a fill character other than a space character. 

  ```python
  >>> 'Hello'.rjust(20, '*')    # '***************Hello'
  >>> 'Hello'.ljust(20, '-')    # 'Hello---------------'
  ```

- center():

  ```python
  >>> 'Hello'.center(20)        # '       Hello       '
  >>> 'Hello'.center(20, '=')   # '=======Hello========'
  ```

- Example:

  ```python
  >>> def printPicnic(items_dict, left_width, right_width):
  ...     print('PICNIC ITEMS'.center(left_width + right_width, '-'))
  ...     for k, v in items_dict.items():
  ...         print(k.ljust(left_width, '.') + str(v).rjust(right_width))

  >>> picnic_item = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
  ... printPicnic(picnic_item, 12, 5)
  ... printPicnic(picnic_item, 20, 6)
  [OUT]
  ---PICNIC ITEMS--
  sandwiches..    4
  apples......   12
  cups........    4
  cookies..... 8000
  -------PICNIC ITEMS-------
  sandwiches..........     4
  apples..............    12
  cups................     4
  cookies.............  8000
  ```

[*Return to the Top*](#table-of-content)

### Removing Whitespace with strip(), rstrip(), and lstrip()

```python
>>> spam = '    Hello World     '
>>> spam.strip()                                # 'Hello World'
>>> spam.lstrip()                               # 'Hello World '
>>> spam.rstrip()                               # '    Hello World'
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')                          # 'BaconSpamEggs'
>>>
>>> s = ' Hello       World  '
>>> re.sub('\s+', ' ', s)                       # ' Hello World '
>>> re.sub('\s+', ' ', s).strip()               # 'Hello World'
```

[*Return to the Top*](#table-of-content)

### Copying and Pasting Strings with the pyperclip Module (need pip install)

```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()               # 'Hello world!'
```

[*Return to the Top*](#table-of-content)

### Reformatting Text With textwrap

```python
>>> s = '''Look into my eyes, look into my eyes, the eyes, the eyes, the eyes,
..        not around the eyes, don't look around the eyes, look into my eyes, you're under. '''

>>> import textwrap
>>> textwrap.fill(s, 70)
>>> textwrap.fill(s, 40)

>>> textwrap.fill(s, 40, initial_indent='    ')              # will add spaces in the begining
>>> textwrap.fill(s, 40, subsequent_indent='    ')           # will add spaces to all line except the first line

>>> textwrap.indent(s, '> ')                                 # Add > to the beggining of each line
>>> textwrap.indent(textwrap.fill(s, width=50), '> ')        # Combining options

>>> textwrap.fill(s, initial_indent='', subsequent_indent=' ' * 4, width=50)
>>> textwrap.shorten(s, 100)                                # Truncate text, and add [...] to the end
```

[*Return to the Top*](#table-of-content)

<a name="performing-io-operations">

### Performing I/O Operations on a string

- To feed a text or binary string to cide that's been written to operate on
- file-like objects instead use the < io.StringIO()> and < io.BytesIO() >

  ```python
  >>> import io
  >>> s = io.StringIO()
  >>> s.write('Hello World, ')
  >>> print('This is a test', file=s)

  # Get all of the data
  >>> s.getvalue()            # 'Hello World, This is a test'

  # work with binary data
  >>> s = io.BytesIO()
  >>> s.write(b'binary data')
  >>> s.getvalue()            # b'binary data'
  ```
[*Return to the Top*](#table-of-content)

### Splitting Strings on Any of Multiple Delimiters

- `re.split`

  ```python
  >>> line = 'python, django;   javascript, mongodb database'
  >>> key_skills = re.split(r'[;,\s]\s*', line)
  >>> key_skills                                  # ['python', 'django', 'javascript', 'mongodb', 'database']
  ```

[*Return to the Top*](#table-of-content)

### Matching Strings Using Shell Wildcard Patterns

- `from fnmatch import fnmatch`

  ```python
  >>> fnmatch('foo.txt', '*.txt')           # True
  >>> fnmatch('foo.txt', '*o.txt')          # True
  >>> fnmatch('Dat45.csv', 'Dat[0-9]*')     # True

  >>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
  >>> [name for name in names if fnmatch(name, 'Dat*.csv')]             # ['Dat1.csv', 'Dat2.csv']
  ```

- `from fnmatch import fnmatchcase`: case sensitive

  ```python
  >>> addresses = ['5412 N CLARK ST', '1060 W ADDISON ST', '1039 W GRANVILLE AVE', '2122 N CLARK ST', '4802 N BROADWAY']
  >>> [addr for addr in addresses if fnmatchcase(addr, '* ST')]         # ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
  ```
[*Return to the Top*](#table-of-content)
