<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [ChainMap](#chainmap)
- [OrderedDict](#ordereddict)
- [counter](#counter)
- [namedtuple](#namedtuple)
- [deque](#deque)
- [defaultdict](#defaultdict)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

### ChainMap

- Accept any number of mappings or dictionaries and turn them into a single view that you can update.

    ```python
    >>> from collections import ChainMap
    >>> car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
    >>> car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
    >>> car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
    >>> car_pricing = ChainMap(car_accessories, car_options, car_parts)
    >>> car_pricing['hood']                 # 500
    >>> print(car_pricing)
    [OUT]
     ChainMap({'seat_cover': 99, 'cover': 100, 'hood_ornament': 150},
              {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300},
              {'hood': 500, 'engine': 5000, 'front_door': 750})
    ```

- Continue on ChainMap

    ```python
    >>> a = {'a': 'A', 'c': 'C'}
    >>> b = {'b': 'B', 'c': 'D'}
    >>> m = ChainMap(a, b)
    >>> m.maps                # [{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
    >>> m['c']                # 'C'
    >>> m.get('c')            # 'C'
    >>> m.maps = list(reversed(m.maps))
    >>> m.get('c')            # 'D'
    >>> a['a'] = 'E'          # Update a ChainMap
    >>> m['a']                # E
    >>> m['b'] = 'ZZ'         # This will add key 'b' to a because a dont have a b key
    >>> a                     # {'a': 'Z', 'c': 'E', 'b': 'ZZ'}

    >>> a = {'a': 'A', 'c': 'C'}
    >>> b = {'b': 'B', 'c': 'D'}
    >>> m = collections.ChainMap(a, b)
    >>> m_2 = m.new_child()
    >>> m_2                   # ChainMap({}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
    >>> m                     # ChainMap({'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
    >>> m_2                   # ChainMap({'c': 'E'}, {'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'})
    ```

[*Return to the Top*](#table-of-content)

- Example with argparse

    ```python
    >>> import argparse, os
    >>> from collections import ChainMap

    >>> def main():
    ...     app_defaults = {'username': 'admin', 'password': 'admin'}
    ...
    ...     parser = argparse.ArgumentParser()
    ...     parser.add_argument('-u', '--username')
    ...     parser.add_argument('-p', '--password')
    ...     args = parser.parse_args()
    ...
    ...     # vars(args) equals args.__dict__.
    ...     command_line_arguments = {key: value for key, value in vars(args).items() if value}
    ...
    ...     # if username is not given; then use the defaults values
    ...     chain = ChainMap(command_line_arguments, app_defaults)
    ...
    ...     # you can pass os.environ as second proposition like:
    ...     # chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    ...     print(chain['username'])

    >>> if __name__ == '__main__':
    ...     main()
    ```

[*Return to the Top*](#table-of-content)

### OrderedDict

- Remember the Order Keys Are Added to a Dictionary

    ```python
    >>> person = OrderedDict()
    >>> person['first'] = 'Dabve'
    >>> person['last'] = 'Band'
    >>> person['age'] = 33
    >>> print(person)           # OrderedDict([('first', 'Dabve'), ('last', 'Band'), ('age', 33)])
    ```

- Reordering

    ```python
    >>> d = OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
    >>> print(d)                # OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
    >>> d.move_to_end('b')
    >>> print(d)                # OrderedDict([('a', 'A'), ('c', 'C'), ('b', 'B')])
    >>> d.move_to_end('b', last=False)      # last=False == Move first
    >>> print(d)                # OrderedDict([('b', 'B'), ('a', 'A'), ('c', 'C')])
    ```

[*Return to the Top*](#table-of-content)

### counter

```python
>>> from collections import Counter
>>> languageCounter = Counter()

>>> person1 = ['Python', 'C++']
>>> person2 = ['Python', 'PHP', 'HTML/CSS', 'Javascript']
>>> person3 = ['C++']
>>> person4 = ['Python']
>>> person5 = ['Bash', 'C#', 'R']

>>> for person in (person1, person2, person3, person4, person5)
...     languageCounter.update(person)

>>> print(languageCounter)                          # print all
>>> print(languageCounter.most_common(3))           # first three
>>> print(language.elements())
```

- Counter with numbers

    ```python
    >>> c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    >>> c2 = Counter('alphabet')
    >>> print(c1 + c2)
    >>> print(c1 - c2)
    >>> print(c1 & c2)      # Taking positive minimums
    >>> print(c1 | c2)      # Taking maximums
    ```

[*Return to the Top*](#table-of-content)

### namedtuple

- When it comes to memory usage, namedtuple are also 'better' than regular classes and just as memory efficient as regular tuples.
- One of the benefits of using a namedtuple over a regular tuple is that you no longer have to keep track of each item’s index,
- Because now each item is named and accessed via a class property.

- Access like a class

    ```python
    >>> from collections import namedtuple
    >>> Parts = namedtuple('Parts', 'id_num desc cost amount')
    >>> auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200.00, amount=10)
    >>> print(auto_parts.id_num)        # 1234
    >>> print(auto_parts)               # Parts(id_num='1234', desc='Ford Engine', cost=1200.0, amount=10)

    >>> print(auto_parts._fields)                       # (id_num, desc, cost, amount)
    >>> print(auto_parts._asdict)                       # return orderedDict
    >>> auto_parts2 = auto_parts._replace(cost=1300.0)  # replace
    ```

- From dict to named tuple

    ```python
    >>> Parts = {'id_num': '1234', 'desc': 'Ford Engine', 'cost': 1200.00, 'amount': 10}
    >>> parts = namedtuple('Parts', Parts.keys())(**Parts)  # arguments name, keys, values
    >>> parts                       # Parts(cost=1200.0, desc='Ford Engine', id_num='1234', amount=10)
    ```

- Example from python tricks

    ```python
    >>> Car = namedtuple('Car', 'color mileage')
    >>> myCar = Car('red', 123456)
    >>> print('car color: {0.color}, mileage: {0.mileage}'.format(myCar))   # car color: red, mileage: 12345
    >>> print(myCar[0])         # red
    >>> color, mileage = myCar
    >>> print(color, mileage)   # red, 123456

    >>> ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
    >>> electric_car = ElectricCar('Blue', 123456789, 45.0)
    >>> print(electric_car)     # ElectricCar(color='Blue', meleage=123456, charge=45.0)
    ```

- `_replace(field=value)`

    ```python
    # you must re asign it again
    >>> electric_car = ElectricCar('Blue', 123456789, 45.0)
    >>> electric_car = electric_car._replace(color='Green')
    >>> print(electric_car)                 # ElectricCar(color='Green', meleage=123456, charge=45.0)
    ```

- `_asdict()`

    ```python
    >>> electric_car = electric_car._asdict()
    >>> print(electric_car)             # {'color': 'Blue', 'meleage': 123456, 'charge': 45.0}
    ```

- namedtuple with CSV files

    ```python
    >>> with open('project/gs_pyqt/initial_etats.csv') as csv_f:
    ...     reader = csv.reader(csv_f, delimiter=';')
    ...     headers = next(reader)
    ...     Row = namedtuple('Row', headers)
    ...     rows = [Row(*row) for row in reader]
    ```

- namedtuple with SQLite

    ```python
    >>> conn = sqlite3.connect('somedatabase')
    >>> curs = conn.cursor()
    >>> curs.execute('SELECT designation, code, qte, prixU FROM magasin_pdr')
    >>> Articles = namedtuple('Articles', 'designation, code, qte, prix_unitaire')
    >>> articles = list(map(Articles._make, curs.fetchall()))         # as a list
    >>> articles = (map(Articles._make, curs.fetchall()))             # as a map object (iterable)
    ```

[*Return to the Top*](#table-of-content)

### deque

- Keep a limited history of the last few items seen during iteration or during some other kind of processing.

    ```python
    >>> from collections import deque
    >>> q = deque(maxlen=3)
    >>> q.append(1)
    >>> q.append(2)
    >>> q.append(3)
    >>> q                           # deque([1, 2, 3], maxlen=3)
    >>> q.append(4)
    >>> q                           # deque([2, 3, 4], maxlen=3)
    ```

[*Return to the Top*](#table-of-content)

### defaultdict

- Is a subclass of Python’s dict that accepts a default_factory as its primary argument.
- Understending dicts

    ```python
    >>> d = {}
    >>> for key, value in pairs:
    ...     if key not in d:
    ...         d[key] = []
    ...     d[key].append(value)
    ```

- With default dict

    ```python
    >>> d = defaultdict(list)
    ... for key, value in pairs:
    ...     d[key].append(value)
    ```

- The default_factory is usually a Python type, such as int or list, but you can also use a function or a lambda too.

    ```python
    >>> from collections import defaultdict
    >>> sentence = "The red for jumped over the fence and ran to the zoo for food"
    >>> words = sentence.split(' ')
    >>> d = defaultdict(int)
    >>> for word in words:
    ...     d[word] += 1
    >>> print(d)
    defaultdict(<class 'int'>,
    {'The': 1, 'and': 1, 'fence': 1, 'food': 1, 'for': 2,
     'jumped': 1, 'over': 1, 'ran': 1, 'red': 1, 'the': 2, 'to': 1,'zoo': 1})

    >>> d = defaultdict(list)
    >>> my_list = [(1234, 100.23),
    ...            (345, 10.45),
    ...            (1234, 75.00),
    ...            (345, 222.66),
    ...            (678, 300.25),
    ...            (1234, 35.67)]

    >>> for acct_num, value in my_list:
    ...     d[acct_num].append(value)
    >>> print(d)
    [OUT] defaultdict(<class 'list'>, {345: [10.45, 222.66], 678: [300.25], 1234: [100.23, 75.0, 35.67]})
    ```

- Create a defaultdict that will assign ‘Monkey’ as the default value to any key.

    ```python
    >>> animal = defaultdict(lambda: "Monkey")
    >>> animal['Sam'] = 'Tiger'
    >>> print (animal['Nick'])   # Monkey
    >>> animal
    [OUT] defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})
    ```

- Make a dictionary that maps keys to more than one value (a so-called 'multidict').
  - Use a list if you want to preserve the insertion order of the items.
  - Use a set if you want to eliminate duplicates (and don’t care about the order).

- values == list

    ```python
    >>> d = defaultdict(list)
    >>> d['a'].append(1)
    >>> d['a'].append(2)
    >>> d['b'].append(4)
    >>> d                  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
    ```

- values == set

    ```python
    >>> d = defaultdict(set)
    >>> d['a'].add(1)
    >>> d['a'].add(2)
    >>> d['b'].add(4)
    >>> d                  # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})
    ```
