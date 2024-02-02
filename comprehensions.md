<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [List comprehension](#list-comprehension)
- [Set comprehension](#set-comprehension)
- [Dict comprehension](#dict-comprehension)


## Comprehensions

### List comprehension

- Getting Started

  ```python
  >>> a = [1, 3, 5, 7, 9, 11]
  >>> lst = [i - 1 for i in a]    # [0, 2, 4, 6, 8, 10]

  >>> doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
  >>> even_squares = [i**2 for i in range(1, 11) if (i**2) % 2 == 0]
  >>> my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

  >>> divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]                 # multiple if condition
  >>> lst = list(reversed([0 if x % 2 == 0 else 1 for x in numberList]))            # if else condition
  >>> lst = [n if n > 0 else 0 for n in my_list]

  >>> list_of_list = [[1, 2, 3], [4, 5, 6]]
  >>> print([y for x in list_of_list for y in x])                         # nested list

  >>> txt_file = [name for name in os.listdir('.') if name.endswith(('.txt'))]
  ```

- Comprehension Like SQL

  ```python
  >>> class Person:
  ...     def __init__(self, name, age, pay=0, job=None):
  ...         self.name = name
  ...         self.age = age
  ...         self.pay = pay
  ...         self.job = job
  >>> bob = Person('Bob Smith', 42, 30000, 'software')
  >>> sue = Person('Sue Jones', 45, 40000, 'hardware')
  >>> persone = [bob, sue]

  >>> [(person.name, person.pay) for person in persone]     # [('Bob Smith', 30000), ('Sue Jones', 40000)]
  >>> [rec.name for rec in persone if rec.age >= 45]        # ['Sue Jones']

  >>> give_rase = 0.3
  >>> [(rec.pay * give_rase) for rec in persone]            # [9000.0, 12000.0]

  >>> [(rec.pay * 0.5 if rec.job == 'hardware' else rec.pay * 0.3) for rec in persone]    # [9000.0, 20000.0]
  ```

***

### Set comprehension

- Getting Started

  ```python
  >>> b = {"abc", "def"}
  >>> {s.upper() for s in b}
  ```

***

### Dict comprehension

- Getting Started

  ```python
  >>> c = {'name': 'Pooka', 'age': 5}
  >>> {v, k for k, v in c.items()}
  ```

- A List comprehension can be generated from a dictionary:

  ```python
  >>> c = {'name': 'Pooka', 'first_name': 'Oooka'}
  >>> ["{}:{}".format(k.upper(), v.upper()) for k, v in c.items()]
  ```

- More on dict comprehension

  ```python
  >>> prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
  >>> p1 = {key: value for key, value in prices.items() if value > 200}
  >>> print(p1)

  >>> tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
  >>> p2 = {key:value for key, value in prices.items() if key in tech_names}
  >>> print(p2)

  >>> fname = ['dabve', 'meziane', 'znanada', 'halim']
  >>> lname = ['band', 'halal', 'chalba', 'awdSahra']
  >>> fullname = {key:value for key, value in zip(fname, lname)}
  >>> print(fullname)
  ```
