<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [The keys(), values(), and items() Methods](#the-keys-values-and-items-methods)
- [Checking Whether a Key or Value Exists in a Dictionary](#checking-whether-a-key-or-value-exists-in-a-dictionary)
- [The get() Method](#the-get-method)
- [The setdefault() Method](#the-setdefault-method)
- [Delete from Dicts](#delete-from-dicts)
- [Sort Dicts](#sort-dicts)
- [Calculating with Dicts](#calculating-with-dicts)
- [Finding Commonalities in two Dicts](#finding-commonalities-in-two-dicts)
- [Pretty Printing](#pretty-printing)
- [Merge two dictionaries](#merge-two-dictionaries)
- [Other Way to Make Dicts](#other-way-to-make-dicts)
- [Usefult example to build SQL Query](#usefult-example-to-build-sql-query)


- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)


## Dictionaries and Structuring Data

- Example Dictionary:

    ```python
    >>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

    >>> my_dict = dict()            # empty dict
    >>> my_dict = {}                # empty dict
    ```

### The keys(), values(), and items() Methods

- **_values()_**:

    ```python
    >>> spam = {'color': 'red', 'age': 42}
    >>> for v in spam.values():
    >>>     print(v)
    red
    42
    ```

- **_keys()_**:

    ```python
    >>> for k in spam.keys():
    >>>     print(k)
    color
    age
    ```

- **_items()_**:

    ```python
    >>> for i in spam.items():
    ...     print(i)
    ('color', 'red')
    ('age', 42)
    ```

- use **_keys()_** **_values()_** **_items()_** with **_for_** loop

    ```python
    >>> spam = {'color': 'red', 'age': 42}
    >>> for k, v in spam.items():
    ...     print('Key: {} Value: {}'.format(k, str(v)))
    Key: age Value: 42
    Key: color Value: red
    ```

[*Return to the Top*](#table-of-content)

### Checking Whether a Key or Value Exists in a Dictionary

```python
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()                   # True
>>> 'Zophie' in spam.values()               # True

# You can omit the call to keys() when checking for a key
>>> 'color' in spam                     # False
>>> 'color' not in spam                 # True
```

[*Return to the Top*](#table-of-content)

### The get() Method

```python
>>> picnic_items = {'apples': 5, 'cups': 2}
>>> 'I am bringing {} cups.'.format(str(picnic_items.get('cups', 0)))       # 'I am bringing 2 cups.'
>>> 'I am bringing {} eggs.'.format(str(picnic_items.get('eggs', 0)))       # 'I am bringing 0 eggs.'
```

[*Return to the Top*](#table-of-content)

### The setdefault() Method

- Let's consider this code:

    ```python
    >>> spam = {'name': 'Pooka', 'age': 5}
    >>> if 'color' not in spam:
    ...     spam['color'] = 'black'
    ```

- Using `setdefault` we could write the same code more succinctly:

    ```python
    >>> spam = {'name': 'Pooka', 'age': 5}
    >>> spam.setdefault('color', 'black')           # 'black'
    >>> spam                                        # {'color': 'black', 'age': 5, 'name': 'Pooka'}

    >>> spam.setdefault('color', 'white')           # 'black'
    >>> spam                                        # {'color': 'black', 'age': 5, 'name': 'Pooka'}
    ```
- Character counter:

    ```python
    >>> msg = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    >>> char_counter = {}
    >>> for char in msg:
    ...     char_counter.setdefault(char, 0)
    ...     char_counter[char] = char_counter[char] + 1
    ```

[*Return to the Top*](#table-of-content)

### Delete from Dicts

    ```python
    >>> del birthdays['Alice']
    >>> print(birthdays)
    >>> popped = birthdays.pop('Meziane')           # return the value of deleted item
    >>> print(popped)
    ```

[*Return to the Top*](#table-of-content)

### Sort Dicts

- Loop through the dict in order

    ```python
    >>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.75}
    >>> for key in sorted(prices.keys()):
    ...     print(key, ':', prices[key])
    AAPL :  612.78
    ACME :  45.23
    FB :  10.75
    HPQ :  37.2
    IBM :  205.55
    ```

- Sorting by keys, this will return a list of tuples

    ```python
    >>> mydict_sorted = sorted(zip(prices.keys(), prices.values()))
    >>> print(type(mydict_sorted), mydict_sorted)
    list
    [('AAPL', 612.78),
     ('ACME', 45.23),
     ('FB', 10.75),
     ('HPQ', 37.2),
     ('IBM', 205.55)]
    ```

- Sorting by values.

    ```python
    >>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.75}
    >>> prices_sorted = sorted(zip(prices.values(), prices.keys()))
    >>> print(prices_sorted)
    [(10.75, 'FB'),
     (37.2, 'HPQ'),
     (45.23, 'ACME'),
     (205.55, 'IBM'),
     (612.78, 'AAPL')]
    ```

- Sorting a list of dictionaries by common key

    ```python
    >>> rows = [
    ...     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    ...     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    ...     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    ...     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ...     ]
    >>> from operator import itemgetter
    >>> by_fname = sorted(rows, key=itemgetter('fname'))
    >>> for row in by_fname:
    ...     print(row)
    [{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}]
    ```

- The itemgetter() function can also accept multiple keys.

    ```python
    >>> by_lname_fname = sorted(rows, key=itemgetter('uid', 'fname'))
    >>> for row in by_lname_fname:
    ...     print(row)
    [{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
     {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
    ```

- Sorting with Lambda 

    ```python
    >>> by_lname_fname = sorted(rows, key=lambda x: (x['lname'], x['fname']))
    >>> for row in by_lname_fname:
    ...     print(row)
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
     {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
     {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
     {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}]
    ```

- This will work also with min, and max

    ```python
    >>> max_uid = max(rows, key=itemgetter('uid'))
    >>> print(max_uid)              # {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ```

[*Return to the Top*](#table-of-content)

### Calculating with dicts

```python
>>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB':10.75}
>>> print(prices)
>>> print('Min value: {}'.format(min(zip(prices.values(), prices.keys()))))         # Min value: (10.75, 'FB')
>>> print('Max value: {}'.format(max(zip(prices.values(), prices.keys()))))         # Max value: (612.78, 'AAPL')
>>> print('Sum of all prices: {}'.format(sum(prices.values())))                 # Sum of all prices: 911.51
```

- The hard way

    ```python
    >>> minimum_price = min(prices, key=lambda x: prices[x])
    >>> print('Min Price: {}: {}'.format(minimum_price, prices[minimum_price]))     # Min Price: FB, 10.75
    ```
- Using **_''.join()_**, **_sum()_**, **_min()_**, **_max()_**

    ```python
    >>> s = ('ACME', 50, 123.45)
    >>> print(','.join(str(x) for x in s))                  # ACME,50,123.45

    >>> portfolio = [{'name': 'GOOG', 'shares': 50},
    ...              {'name': 'YHOO', 'shares': 75},
    ...              {'name': 'AOL', 'shares': 20}]

    >>> sum(x['shares'] for x in portfolio)             # 145
    >>> min(x['shares'] for x in portfolio)             # 20
    >>> max(x['shares'] for x in portfolio)             # 75
    ```

[*Return to the Top*](#table-of-content)

### Finding Commonalities in two Dicts 

```python
>>> a = {'x': 2, 'y': 2, 'z': 3}
>>> b = {'w': 10, 'x': 11, 'y': 2}
>>> print(a.keys() & b.keys())       # find key in common:          {'y', 'x'}
>>> print(a.keys() - b.keys())       # key in a not in b:           {'z'}
>>> print(a.items() & b.items())     # key, value pairs in common:   {('y', 2)}
```

[*Return to the Top*](#table-of-content)

### Pretty Printing

```python
>>> import pprint

>>> message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
>>> count = {}

>>> for character in message:
>>>     count.setdefault(character, 0)
>>>     count[character] = count[character] + 1

>>> pprint.pprint(count)
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 3,
 'd': 3,
 'e': 5,
 'g': 2,
 'h': 3,
 'i': 6,
 'k': 2,
 'l': 3,
 'n': 4,
 'o': 2,
 'p': 1,
 'r': 5,
 's': 3,
 't': 6,
 'w': 2,
 'y': 1}
```

[*Return to the Top*](#table-of-content)

### Merge two dictionaries

```python
# in Python 3.5+:
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = {**x, **y}
>>> z                   # {'c': 4, 'a': 1, 'b': 3}

# in Python 2.7
>>> z = dict(x, **y)
>>> z                   # {'c': 4, 'a': 1, 'b': 3}
```

[*Return to the Top*](#table-of-content)

## Other Way to Make Dicts 

```python
>>> bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
>>> sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
>>> dabve = dict(name='Dabve', age=33, pay=35000, job='dev')

>>> people = [bob, sue, dabve]
>>> names = [person['name'] for person in people]     # with list comprehension
>>> print('people names: {}'.format(names))

>>> job = list(map(lambda x: x['job'], people))       # with map and lambda
>>> print('People\' job: {}'.format(job))

>>> sum_pay = sum(person['pay'] for person in people)
>>> print('The sum of all employee: {}'.format(sum_pay))

>>> payGreat = [rec['name'] for rec in people if rec['pay'] > 30000]
>>> print(payGreat)
```

### Usefult example to build SQL Query

```python
>>> fields = ['name', 'age', 'job', 'pay']
>>> sue_jones = dict.fromkeys(fields, '%s') # MySQL
>>> print(sue_jones)                        # {'name': '%s', 'age': '%s', 'job': '%s', 'pay': '%s'}

>>> sue_jones = dict.fromkeys(fields, '?')  # SQLite
>>> sue_jones                               # {'name': '?', 'age': '?', 'job': '?', 'pay': '?'}
```

- Or with slicing:

    ```python
    >>> fields = ['name', 'age', 'job', 'pay']
    >>> bind = ('?, ' * len(fields))[:-2]                 # SQLite
    >>> bind = ('%s, ' * len(fields))[:-2]                # MySQL
    ```

[*Return to the Top*](#table-of-content)
