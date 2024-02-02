<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Initializing a set](#initializing-a-set)
- [sets: unordered collections of unique elements](#sets-unordered-collections-of-unique-elements)
- [set add() and update()](#set-add-and-update)
- [set remove() and discard()](#set-remove-and-discard)
- [set union()](#set-union)
- [set intersection](#set-intersection)
- [set difference](#set-difference)
- [set symetric_difference](#set-symetricdifference)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## sets

- From the Python 3 [documentation](https://docs.python.org/3/tutorial/datastructures.html)

> A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

[*Return to the Top*](#table-of-content)

### Initializing a set

- There are two ways to create sets: using curly braces `{}` and the bult-in function `set()`

    ```python
    >>> s = {1, 2, 3}
    >>> s = set([1, 2, 3])
    ```

- When creating an empty set, be sure to not use the curly braces `{}`  or you will get an empty dictionary instead.

    ```python
    >>> s = {}
    >>> type(s)         # <class 'dict'>
    ```

[*Return to the Top*](#table-of-content)

### sets: unordered collections of unique elements

- A set automatically remove all the duplicate values.

    ```python
    >>> s = {1, 2, 3, 2, 3, 4}
    >>> s                       # {1, 2, 3, 4}
    ```

- And as an unordered data type, they can't be indexed.

    ```python
    >>> s = {1, 2, 3}
    >>> s[0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing
    >>>
    ```

[*Return to the Top*](#table-of-content)

### set add() and update()

- Using the `add()` method we can add a single element to the set.

    ```python
    >>> s = {1, 2, 3}
    >>> s.add(4)
    >>> s               # {1, 2, 3, 4}
    ```

- And with `update()`, multiple ones .

    ```python
    >>> s = {1, 2, 3}
    >>> s.update([2, 3, 4, 5, 6])
    >>> s                           # {1, 2, 3, 4, 5, 6}  # remember, sets automatically remove duplicates
    ```

[*Return to the Top*](#table-of-content)

### set remove() and discard()

- Both methods will remove an element from the set, but `remove()` will raise a `key error` if the value doesn't exist.

    ```python
    >>> s = {1, 2, 3}
    >>> s.remove(3)
    >>> s                       # {1, 2}
    >>> s.remove(3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 3
    ```

- `discard()` won't raise any errors.

    ```python
    >>> s = {1, 2, 3}
    >>> s.discard(3)
    >>> s                       # {1, 2}
    >>> s.discard(3)
    ```

[*Return to the Top*](#table-of-content)

### set union()

- `union()` or `|` will create a new set that contains all the elements from the sets provided.

    ```python
    >>> s1 = {1, 2, 3}
    >>> s2 = {3, 4, 5}
    >>> s1.union(s2)  # or 's1 | s2'            # {1, 2, 3, 4, 5}
    ```

[*Return to the Top*](#table-of-content)

### set  intersection

- `intersection`  or `&`  will return a set containing only the elements that are common to all of them.

    ```python
    >>> s1 = {1, 2, 3}
    >>> s2 = {2, 3, 4}
    >>> s3 = {3, 4, 5}
    >>> s1.intersection(s2, s3)  # or 's1 & s2 & s3'
    {3}
    ```

[*Return to the Top*](#table-of-content)

### set  difference

- `difference` or `-` will return only the elements that are in one of the sets.

    ```python
    >>> s1 = {1, 2, 3}
    >>> s2 = {2, 3, 4}
    >>> s1.difference(s2)  # or 's1 - s2'
    {1}
    ```

[*Return to the Top*](#table-of-content)

### set symetric_difference

- `symetric_difference` or `^` will return all the elements that are not common between them.

    ```python
    >>> s1 = {1, 2, 3}
    >>> s2 = {2, 3, 4}
    >>> s1.symmetric_difference(s2)  # or 's1 ^ s2'
    {1, 4}
    ```
[*Return to the Top*](#table-of-content)
