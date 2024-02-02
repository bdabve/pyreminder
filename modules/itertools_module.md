<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content
- [Process items in an iterable](#process-items-in-an-iterable)
- [accumulate()](#accumulate)
- [combinations()](#combinations)
- [combinations_with_replacement()](#combinationswithreplacement)
- [count()](#count)
- [cycle()](#cycle)
- [chain()](#chain)
- [compress()](#compress)
- [dropwhile()](#dropwhile)
- [filterfalse()](#filterfalse)
- [groupby()](#groupby)
- [islice()](#islice)
- [permutations()](#permutations)
- [product()](#product)
- [repeat()](#repeat)
- [starmap()](#starmap)
- [takewhile()](#takewhile)
- [tee()](#tee)
- [zip_longest()](#zip_longest)
- [Tracking line numbers in a file](#tracking-line-numbers-in-a-file)
- [Generator](#generator)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## itertools Module

- The *itertools* module is a colection of tools intented to be fast and use memory efficiently when handling iterators (like [lists](#lists) or [dictionaries](#dictionaries-and-structuring-data)).

- From the official [Python 3.x documentation](https://docs.python.org/3/library/itertools.html):

> The module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python.

- The *itertools* module comes in the standard library and must be imported.

- The [operator](https://docs.python.org/3/library/operator.html) module will also be used. This module is not necessary when using itertools, but needed for some of the examples below.

[*Return to the Top*](#table-of-content)

### Process items in an iterable

```python
>>> with open('/etc/passwd') as f:
...     try:
...         while True:
...             line = next(f)
...             print(line, end='')
...     except StopIteration:
...         pass
```

### accumulate()

- Makes an iterator that returns the results of a function.

    ```python
    itertools.accumulate(iterable[, func])
    ```

- Example:

    ```python
    >>> data = [1, 2, 3, 4, 5]
    >>> result = itertools.accumulate(data, operator.mul)
    >>> for each in result:
    ...    print(each)
    1
    2
    6
    24
    120
    ```

- The operator.mul takes two numbers and multiplies them:

    ```python
    >>> operator.mul(1, 2)          # 2
    >>> operator.mul(2, 3)          # 6
    >>> operator.mul(6, 4)          # 24
    >>> operator.mul(24, 5)         # 120
    ```

- Passing a function is optional:

    ```python
    >>> data = [5, 2, 6, 4, 5, 9, 1]
    >>> result = itertools.accumulate(data)
    >>> for each in result:
    ...    print(each)
    5
    7
    13
    17
    22
    31
    32
    ```

- If no function is designated the items will be summed:

    ```python
    5
    5 + 2 = 7
    7 + 6 = 13
    13 + 4 = 17
    17 + 5 = 22
    22 + 9 = 31
    31 + 1 = 32
    ```

[*Return to the Top*](#table-of-content)

### combinations()

- Takes an iterable and a integer. This will create all the unique combination that have r members.

    ```python
    itertools.combinations(iterable, r)
    ```

- Example:

    ```python
    >>> shapes = ['circle', 'triangle', 'square',]
    >>> result = itertools.combinations(shapes, 2)
    >>> for each in result:
    >>>    print(each)
    ('circle', 'triangle')
    ('circle', 'square')
    ('triangle', 'square')
    ```

[*Return to the Top*](#table-of-content)

### combinations_with_replacement()

- Just like combinations(), but allows individual elements to be repeated more than once.

    ```python
    itertools.combinations_with_replacement(iterable, r)
    ```

- Example:

    ```python
    >>> shapes = ['circle', 'triangle', 'square']
    >>> result = itertools.combinations_with_replacement(shapes, 2)
    >>> for each in result:
    >>>    print(each)
    ('circle', 'circle')
    ('circle', 'triangle')
    ('circle', 'square')
    ('triangle', 'triangle')
    ('triangle', 'square')
    ('square', 'square')
    ```

[*Return to the Top*](#table-of-content)

### count()

- Makes an iterator that returns evenly spaced values starting with number start.

    ```python
    itertools.count(start=0, step=1)
    ```

- Example:

    ```python
    >>> for i in itertools.count(10,3):
    ...    print(i)
    ...    if i > 20:
    ...        break
    10
    13
    16
    19
    22
    ```

[*Return to the Top*](#table-of-content)

### cycle()

- This function cycles through an iterator endlessly.

    ```python
    itertools.cycle(iterable)
    ```

- Example:

    ```python
    >>> colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
    >>> for color in itertools.cycle(colors):
    ...    print(color)
    red
    orange
    yellow
    green
    blue
    violet
    red
    orange
    ```

    > When reached the end of the iterable it start over again from the beginning.

[*Return to the Top*](#table-of-content)

### chain()

- Take a series of iterables and return them as one long iterable.

    ```python
    itertools.chain(*iterables)
    ```

- Example:

    ```python
    >>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
    >>> shapes = ['circle', 'triangle', 'square', 'pentagon']
    >>> result = itertools.chain(colors, shapes)
    >>> for each in result:
    ...    print(each)
    red
    orange
    yellow
    green
    blue
    circle
    triangle
    square
    pentagon
    ```

- Iterate on Items in Separate Containers

    ```python
    >>> from itertools import chain
    >>> a = [1, 2, 3]
    >>> b = ['x', 'y', 'z']
    >>> for x in chain(a, b):
    ...     print(x, end='')
    1, 2, 3, x, y, z
    ```

[*Return to the Top*](#table-of-content)

### compress()

- Filters one iterable with another.

    ```python
    itertools.compress(data, selectors)
    ```

- Example:

    ```python
    >>> shapes = ['circle', 'triangle', 'square', 'pentagon']
    >>> selections = [True, False, True, False]
    >>> result = itertools.compress(shapes, selections)
    >>> for each in result:
    >>>    print(each)
    circle
    square
    ```

[*Return to the Top*](#table-of-content)

### dropwhile()

- Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element.

    ```python
    itertools.dropwhile(predicate, iterable)
    ```

- Example:

    ```python
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    >>> result = itertools.dropwhile(lambda x: x<5, data)
    >>> for each in result:
    ...    print(each)
    5
    6
    7
    8
    9
    10
    1
    ```

- Skipping the First Part of an Iterable

    ```python
    >>> with open('/etc/passwd') as f:
    ...     # skip line that starts with #
    ...     lines = (line for line in f if not line.startswith('#'))
    ...     for line in lines:
    ...         print(line)

    >>> from itertools import dropwhile
    >>> with open('/etc/passwd') as f:
    ...     # the returned iterator discards the first items in the sequence as long as the supplied function returns True
    ...     for line in dropwhile(lambda line: line.startswith('#'), f):
    ...         print(line, end='')
    ```

[*Return to the Top*](#table-of-content)

### filterfalse()

- Makes an iterator that filters elements from iterable returning only those for which the predicate is False.

    ```python
    itertools.filterfalse(predicate, iterable)
    ```

- Example:

    ```python
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> result = itertools.filterfalse(lambda x: x<5, data)
    >>> for each in result:
    ...    print(each)
    5
    6
    7
    8
    9
    10
    ```

[*Return to the Top*](#table-of-content)

### groupby()

- Simply put, this function groups things together.

    ```python
    itertools.groupby(iterable, key=None)
    ```

- Example:

    ```python
    >>> robots = [{
        'name': 'blaster',
        'faction': 'autobot'
    }, {
        'name': 'galvatron',
        'faction': 'decepticon'
    }, {
        'name': 'jazz',
        'faction': 'autobot'
    }, {
        'name': 'metroplex',
        'faction': 'autobot'
    }, {
        'name': 'megatron',
        'faction': 'decepticon'
    }, {
        'name': 'starcream',
        'faction': 'decepticon'
    }]
    >>> for key, group in itertools.groupby(robots, key=lambda x: x['faction']):
    ...    print(key)
    ...    print(list(group))
    autobot
    [{'name': 'blaster', 'faction': 'autobot'}]
    decepticon
    [{'name': 'galvatron', 'faction': 'decepticon'}]
    autobot
    [{'name': 'jazz', 'faction': 'autobot'}, {'name': 'metroplex', 'faction': 'autobot'}]
    decepticon
    [{'name': 'megatron', 'faction': 'decepticon'}, {'name': 'starcream', 'faction': 'decepticon'}]
    ```

[*Return to the Top*](#table-of-content)

### islice()

- This function is very much like slices. This allows you to cut out a piece of an iterable.

    ```python
    itertools.islice(iterable, start, stop[, step])
    ```

- Example:

    ```python
    >>> colors = ['red', 'orange', 'yellow', 'green', 'blue',]
    >>> few_colors = itertools.islice(colors, 2)
    >>> for each in few_colors:
    ...    print(each)
    red
    orange
    ```

- if you happen to know the exact number of items you want to skip

    ```python
    >>> from itertools import islice
    >>> items = ['a', 'b', 'c', 1, 4, 10, 15]
    >>> for x in islice(items, 3, None):
    ...     # The None argument to slice() is required, to indicate that you want everything beyond the first three items.
    ...     print(x)
    ```

[*Return to the Top*](#table-of-content)

### permutations()

    ```python
    itertools.permutations(iterable, r=None)
    ```

- Example:

    ```python
    >>> alpha_data = ['a', 'b', 'c']
    >>> result = itertools.permutations(alpha_data)
    >>> for each in result:
    ...    print(each)
    ('a', 'b', 'c')
    ('a', 'c', 'b')
    ('b', 'a', 'c')
    ('b', 'c', 'a')
    ('c', 'a', 'b')
    ('c', 'b', 'a')
    ```

- iterate over all of the possible combinations.

    ```python
    >>> items = [1, 2, 3]
    >>> from itertools import permutations
    >>> for p in permutations(items):
    ...     print(p, ', ', end='')
    (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

    >>> for p in permutations(items, 2):
    ...     print(p, ', ', end='')
    ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')
    ```

[*Return to the Top*](#table-of-content)

### product()

- Creates the cartesian products from a series of iterables.

    ```python
    >>> num_data = [1, 2, 3]
    >>> alpha_data = ['a', 'b', 'c']
    >>> result = itertools.product(num_data, alpha_data)
    >>> for each in result:
    ...     print(each)
    (1, 'a')
    (1, 'b')
    (1, 'c')
    (2, 'a')
    (2, 'b')
    (2, 'c')
    (3, 'a')
    (3, 'b')
    (3, 'c')
    ```

[*Return to the Top*](#table-of-content)

### repeat()

- This function will repeat an object over and over again. Unless, there is a times argument.

    ```python
    itertools.repeat(object[, times])
    ```

- Example:

    ```python
    >>> for i in itertools.repeat("spam", 3):
    ...     print(i)
    spam
    spam
    spam
    ```

[*Return to the Top*](#table-of-content)

### starmap()

- Makes an iterator that computes the function using arguments obtained from the iterable.

    ```python
    itertools.starmap(function, iterable)
    ```

- Example:

    ```python
    >>> data = [(2, 6), (8, 4), (7, 3)]
    >>> result = itertools.starmap(operator.mul, data)
    >>> for each in result:
    ...    print(each)
    12
    32
    21
    ```

[*Return to the Top*](#table-of-content)

### takewhile()

- The opposite of dropwhile(). Makes an iterator and returns elements from the iterable as long as the predicate is true.

    ```python
    itertools.takewhile(predicate, iterable)
    ```

- Example:

    ```python
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    >>> result = itertools.takewhile(lambda x: x<5, data)
    >>> for each in result:
    ...    print(each)
    1
    2
    3
    4
    ```

[*Return to the Top*](#table-of-content)

### tee()

- Return n independent iterators from a single iterable.

    ```python
    itertools.tee(iterable, n=2)
    ```

- Example:

    ```python
    >>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
    >>> alpha_colors, beta_colors = itertools.tee(colors)
    >>> for each in alpha_colors:
    ...    print(each)
    red
    orange
    yellow
    green
    blue
    ```

    ```python
    >>> colors = ['red', 'orange', 'yellow', 'green', 'blue']
    >>> alpha_colors, beta_colors = itertools.tee(colors)
    >>> for each in beta_colors:
    ...    print(each)
    red
    orange
    yellow
    green
    blue
    ```

[*Return to the Top*](#table-of-content)

### zip_longest()

- Makes an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted.

    ```python
    itertools.zip_longest(*iterables, fillvalue=None)
    ```

- Example:

    ```python
    >>> colors = ['red', 'orange', 'yellow', 'green', 'blue',]
    >>> data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
    >>> for each in itertools.zip_longest(colors, data, fillvalue=None):
    >>>    print(each)
    ('red', 1)
    ('orange', 2)
    ('yellow', 3)
    ('green', 4)
    ('blue', 5)
    (None, 6)
    (None, 7)
    (None, 8)
    (None, 9)
    (None, 10)
    ```

- Another Example

    ```python
    >>> from itertools import zip_longest
    >>> a = [1, 2, 3]
    >>> b = ['a', 'b', 'c', 'd', 'e']
    >>> for i in zip_longest(a, b):
    ...     print(i)
    (1, 'a'), (2, 'b'), (3, 'c'), (None, 'd'), (None, 'e')

    >>> for i in zip_longest(a, b, fillvalue=0):
    ...     print(i)
    (1, 'a'), (2, 'b'), (3, 'c'), (0, 'd'), (0, 'e')
    ```

[*Return to the Top*](#table-of-content)

### Tracking line numbers in a file 

- This is like (cat -n) in bash

    ```python
    >>> with open('filename') as f:
    ...     for lineno, line in enumerate(f, 2):
    ...         print(lineno, line)
    ```

[*Return to the Top*](#table-of-content)

### Generator

```python
>>> def countdown(n):
...     print('Starting to count from', n)
...     while n > 0:
...         yield n
...         n -= 1
...     print('Done!')

>>> counter = (x * 2 for x in range(1, 20))
>>> counter             # <generator object <genexpr> at 0x7fafd2fa9ba0>
```

[*Return to the Top*](#table-of-content)
