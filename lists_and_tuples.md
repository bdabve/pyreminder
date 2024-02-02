<link rel="stylesheet" href="style.css">
## Read It

- [Official Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Getting Sublists with Slices](#getting-sublists-with-slices)
- [Changing Values in a List with Indexes](#changing-values-in-a-list-with-indexes)
- [List Concatenation and List Replication](#list-concatenation-and-list-replication)
- [Removing Values from Lists](#removing-values-from-lists)
- [Loops with Lists](#loops-with-lists)
- [Largest and Smallest items](#largest-and-smallest-items)
- [The in and not in Operators](#the-in-and-not-in-operators)
- [The Multiple Assignment Trick](#the-multiple-assignment-trick)
- [Augmented Assignment Operators](#augmented-assignment-operators)
- [Adding Values to Lists with the append() and insert() Methods](#adding-values-to-lists-with-the-append-and-insert-methods)
- [Sorting the Values in a List](#sorting-the-values-in-a-list)
- [Shallow and Deep copy](#shallow-and-deep-copy)
- [Tuple Data Type](#tuple-data-type)
- [Converting Types with the list() and tuple() Functions](#converting-types-with-the-list-and-tuple-functions)

***
- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## Lists

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']

>>> spam                # ['cat', 'bat', 'rat', 'elephant']
>>> spam[0]             # 'cat'
>>> spam[1]             # 'bat'
>>> spam[-1]            # 'elephant'
>>> spam[-3]            # 'bat'

>>> 'The {} is afraid of the {}.'.format(spam[-1], spam[-3])    # 'The elephant is afraid of the bat.'

# index()
>>> spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
>>> spam.index('Pooka')                 # 1

# len()
>>> spam = ['cat', 'dog', 'moose']
>>> len(spam)                           # 3
```

[*Return to the Top*](#table-of-content)

### Getting Sublists with Slices

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[0:4]           # ['cat', 'bat', 'rat', 'elephant']

>>> spam[1:3]           # ['bat', 'rat']
>>> spam[0:-1]          # ['cat', 'bat', 'rat']
>>> spam[:2]            # ['cat', 'bat']
>>> spam[1:]            # ['bat', 'rat', 'elephant']
```

- Unpacking a Sequence into Separate Variables

  ```python
  >>> data = ['ACME', 50, 91.1, (2012, 12, 21)]
  >>> name, shares, price, date = data
  >>> name                                  # 'ACME'
  >>> date                                  # (2012, 12, 21)

  >>> name, shares, price, (year, mon, day) = data
  >>> year                                  # 2012
  
  >>> record = ('Dave', 'dave@email.com', '773-555-1212', '847-555-1212')
  >>> name, email, *phone_numbers = record
  >>> phone_numbers                                 # ['773-555-1212', '847-555-1212']
  
  >>> record = ('ACME', 50, 123.45, (12, 18, 2012))
  >>> name, *_, (*_, year) = record
  >>> name                                          # 'ACME'
  >>> year                                          # 2012
  ```

- Naming a slice

    ```python
    >>> items = [0, 1, 2, 3, 4, 5, 6]
    >>> a = slice(2, 4)
    >>> a.start                      # 2
    >>> a.stop                       # 4
    >>> items[a]                     # [2, 3]
    >>> items[a] = [10, 12]
    >>> items                        # [0, 1, 10, 12, 4, 5, 6]
    >>> del items[a]
    >>> items                        # [0, 1, 4, 5, 6]
    ```

- Slicing the complete list will perform a copy:

    ```python
    >>> spam2 = spam[:]             # ['cat', 'bat', 'rat', 'elephant']
    >>> spam.append('dog')
    >>> spam                        # ['cat', 'bat', 'rat', 'elephant', 'dog']
    >>> spam2                       # ['cat', 'bat', 'rat', 'elephant']
    ```

[*Return to the Top*](#table-of-content)

### Changing Values in a List with Indexes

```python
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam[1] = 'aardvark'
>>> spam            # ['cat', 'aardvark', 'rat', 'elephant']

>>> spam[2] = spam[1]
>>> spam            # ['cat', 'aardvark', 'aardvark', 'elephant']
>>> spam[-1] = 12345
>>> spam            # ['cat', 'aardvark', 'aardvark', 12345]
```

[*Return to the Top*](#table-of-content)

### List Concatenation and List Replication

```python
>>> [1, 2, 3] + ['A', 'B', 'C']         # [1, 2, 3, 'A', 'B', 'C']

>>> ['X', 'Y', 'Z'] * 3                 # ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']

>>> spam = [1, 2, 3]
>>> spam = spam + ['A', 'B', 'C']
>>> spam                                # [1, 2, 3, 'A', 'B', 'C']

>>> li = [1, 2, 3]
>>> li.extend([4, 5, 6])                      # [1, 2, 3, 4, 5, 6]
>>> li += [7, 8, 9]                           # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

[*Return to the Top*](#table-of-content)

### Removing Values from Lists:

- **del**

    ```python
    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> del spam[2]
    >>> spam                # ['cat', 'bat', 'elephant']

    >>> del spam[2]
    >>> spam                # ['cat', 'bat']
    ```

- **remove()**

    ```python
    >>> spam = ['cat', 'bat', 'rat', 'elephant']
    >>> spam.remove('bat')
    >>> spam                    # ['cat', 'rat', 'elephant']
    ```

    > If the value appears multiple times in the list, only the first instance of the value will be removed.

- **pop()**: removes the last item in a list, but it lets you work with that item after removing it.

    ```python
    >>> moto = ['honda', 'yamaha', 'suzuki']
    >>> popped_moto = motorcicles.pop()
    >>> print(moto)                       # ['honda', 'yamaha']
    >>> print(popped_moto)                # suzuki
    ```

- Remove duplicate: A set will remove all duplicate,

    ```python
    >>> my_set = {}                            # declaring an empty set

    >>> a = [1, 5, 2, 1, 9, 1, 5, 10]
    >>> print(set(a))                            # {1, 2, 9, 10, 5}
    >>> print(sorted(set(a)))                    # [1, 2, 5, 9, 10]
    ```

[*Return to the Top*](#table-of-content)

### Loops with Lists

- simple **_for_** loop:

    ```python
    >>> files = ['file.txt', 'file.csv', 'file.xlsx']
    >>> for f in files:
    ...     print(f)
    ```

- **_enumerate()_**

    ```python
    >>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
    >>> for i, supply in enumerate(supplies):
    ...     print('Index {} in supplies is: {}'.format(str(i), supply))
    Index 0 in supplies is: pens
    Index 1 in supplies is: staplers
    Index 2 in supplies is: flame-throwers
    Index 3 in supplies is: binders
    ```

- Looping throught two lists with **_enumerate()_**

    ```python
    >>> names = ['ibrahim', 'meziane', 'znanda', 'halim']
    >>> snames = ['dabve', 'halala', 'chalba', '3awd']

    >>>  for index, name in enumerate(names): 
    ...:     print(f'{name}: {snames[index]}') 
    ibrahim: dabve
    meziane: halala
    znanada: chalba
    halim: 3awd
    ```

- Looping through two lists with the **_zip()_**

    ```python
    >>> name = ['Pete', 'John', 'Elizabeth']
    >>> age = [6, 23, 44]
    >>> for n, a in zip(name, age):
    ...     print('{} is {} years old'.format(n, a))
    Pete is 6 years old
    John is 23 years old
    Elizabeth is 44 years old
    ```

- Looping backwards

    ```python
    >>> for color in reversed(colors):
    ...     print(color)
    ```

[*Return to the Top*](#table-of-content)

### Largest and Smallest items

```python
>>> import heapq
>>> nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
>>> print(heapq.nlargest(3, nums))                      # [42, 37, 23]
>>> print(heapq.nsmallest(3, nums))                     # [-4, 1, 2]
```

- With **key** argument

    ```python
    >>> portfolio = [
    ...           {'name': 'IBM', 'shares': 100, 'price':91.1},
    ...           {'name': 'AAPL', 'shares': 50, 'price':543.22},
    ...           {'name': 'FB', 'shares': 200, 'price':21.09},
    ...           {'name': 'HPQ', 'shares': 35, 'price':31.75},
    ...           {'name': 'YHOO', 'shares': 45, 'price':16.35},
    ...           {'name': 'ACME', 'shares': 75, 'price':115.65}
    ... ]
    >>> cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
    >>> cheap               
    # [{'shares': 45, 'name': 'YHOO', 'price': 16.35}, {'shares': 200, 'name': 'FB', 'price': 21.09}]

    >>> expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
    >>> expensive           
    # [{'shares': 50, 'name': 'AAPL', 'price': 543.22}, {'shares': 75, 'name': 'ACME', 'price': 115.65}]
    ```

[*Return to the Top*](#table-of-content)

### The in and not in Operators

```python
>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']        # True
>>> spam = ['hello', 'hi', 'howdy', 'heyas']
>>> 'cat' in spam                                       # False
>>> 'howdy' not in spam                                 # False
>>> 'cat' not in spam                                   # True
```

[*Return to the Top*](#table-of-content)

### The Multiple Assignment Trick

The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code. So instead of doing this:

```python
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]

# You could type this line of code:
>>> size, color, disposition = cat
```

- The multiple assignment trick can also be used to swap the values in two variables:

    ```python
    >>> a, b = 'Alice', 'Bob'
    >>> a, b = b, a
    >>> print(a)                # 'Bob'
    >>> print(b)                # 'Alice'
    ```
- Discard certain values

    ```python
    >>> _, share, price, _ = data
    >>> data = ['Dabve', 'Dabve@email.com', '777-555-888', '888-999-666']
    >>> name, email, *phoneNumbers = data
    >>> phoneNumbers                               # ['777-555-888', '888-999-666']

    >>> *trailing, current = [10, 8, 7, 1, 9, 13, 15, 50]
    >>> current                                    # 50
    ```

- Useful as

    ```python
    >>> def drop_first_last(grades):
    ...     firs, *middle, last = grades
    ...     return avg(middle)
    ```

[*Return to the Top*](#table-of-content)

### Augmented Assignment Operators

| Operator    | Equivalent        |
| ----------- | ----------------- |
| `spam += 1` | `spam = spam + 1` |
| `spam -= 1` | `spam = spam - 1` |
| `spam *= 1` | `spam = spam * 1` |
| `spam /= 1` | `spam = spam / 1` |
| `spam %= 1` | `spam = spam % 1` |

- Examples:

    ```python
    >>> spam = 'Hello'
    >>> spam += ' world!'
    >>> spam                # 'Hello world!'

    >>> bacon = ['Zophie']
    >>> bacon *= 3
    >>> bacon               # ['Zophie', 'Zophie', 'Zophie']
    ```

[*Return to the Top*](#table-of-content)

### Adding Values to Lists with the **append()** and **insert()** Methods

- **append()**:

    ```python
    >>> spam = ['cat', 'dog', 'bat']
    >>> spam.append('moose')
    >>> spam                        # ['cat', 'dog', 'bat', 'moose']
    ```

- **insert()**:

    ```python
    >>> spam = ['cat', 'dog', 'bat']
    >>> spam.insert(1, 'chicken')
    >>> spam                            # ['cat', 'chicken', 'dog', 'bat']
    ```
[*Return to the Top*](#table-of-content)

### Sorting the Values in a List

- **sort()**
    ```python
    >>> spam = [2, 5, 3.14, 1, -7]
    >>> spam.sort()
    >>> spam                # [-7, 1, 2, 3.14, 5]

    >>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
    >>> spam.sort()
    >>> spam                # ['ants', 'badgers', 'cats', 'dogs', 'elephants']
    ```

- You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order:

    ```python
    
    >>> spam.sort(reverse=True)
    >>> spam.reverse()              # [9, 8, 7, 6, 5, 4, 3, 2] le renversement se fait directement dans la liste.
    >>> spam                        # ['elephants', 'dogs', 'cats', 'badgers', 'ants']
    ```

- If you need to sort the values in regular alphabetical order, pass str. lower for the key keyword argument in the sort() method call:

    ```python
    >>> spam = ['a', 'z', 'A', 'Z']
    >>> spam.sort(key=str.lower)
    >>> spam                            # ['a', 'A', 'z', 'Z']
    ```

- **sorted()**: You can use the built-in function `sorted` to return a new list:

    ```python
    >>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
    >>> sorted(spam)                        # ['ants', 'badgers', 'cats', 'dogs', 'elephants'] 
    >>> sorted(spam, key=len)               # sorte by length ['ants', 'cats', 'dogs', 'badgers', 'elephants']
    ```

[*Return to the Top*](#table-of-content)

### Shallow and Deep copy

- Make a shalow copy
    ```python
    >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> copy_xs = list(xs)                        # OR you can do the same: copy_xs = xs[:]
    >>> print(xs == copy_xs)                      # True,  == :means they have the same values
    >>> print(xs is copy_xs)                      # False, is :means that they share the same object
    >>> xs.append([10, 11, 12])
    >>> xs                                        # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    >>> copy_xs                                   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ```

    > Therefore, when you modify one of the child objects in xs,
    > this modification will be reflected in copy_xs as well—that’s because both lists share the same child objects.
    > The copy is only a shallow, one level deep copy

    ```python
    >>> xs[1][0] = 'X'
    >>> xs                                        # [[1, 2, 3], ['X', 5, 6], [7, 8, 9], [10, 11, 12]]
    >>> copy_xs                                   # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
    ```

- Making Deep Copies

    ```python
    >>> import copy
    >>> xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> copy_xs = copy.deepcopy(xs)
    >>> xs[1][0] = 'X'
    >>> xs                                        #  [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
    >>> copy_xs                                   # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ```
[*Return to the Top*](#table-of-content)

***

### Tuple Data Type

```python
>>> eggs = ('hello', 42, 0.5)
>>> eggs[0]                         # 'hello'

>>> eggs[1:3]                       # (42, 0.5)
>>> len(eggs)                       # 3
```

- The main way that tuples are different from lists is that tuples, like strings, are immutable.

[*Return to the Top*](#table-of-content)

### Converting Types with the list() and tuple() Functions

```python
>>> tuple(['cat', 'dog', 5])                # ('cat', 'dog', 5)

>>> list(('cat', 'dog', 5))                 # ['cat', 'dog', 5]
>>> list('hello')                           # ['h', 'e', 'l', 'l', 'o']
```

[*Return to the Top*](#table-of-content)
