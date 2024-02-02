<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)
- [Jupyter Notebook](https://mybinder.org/v2/gh/wilfredinni/python-cheatsheet/master?filepath=jupyter_notebooks)

## Table of Content

- [Classes](#classes)
- [Defining Your Own Exception Classes](#defining-your-own-exception-classes)
- [Class vs Instance Variable Pitfalls](#class-vs-instance-variable-pitfalls)
- [Copying Arbitrary Objects](#copying-arbitrary-objects)
- [Instance Class and Static Methods Demystified](#instance-class-and-static-methods-demystified)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

### Classes

- `__str__` : gets called when you try to convert an object into a string through the various means that are available like:
    - print(myCar)
    - str(myCar)
    - ''.format(myCar)

    ```python
    >>> class Car:
    ...     def __init__(self, color, mileage):
    ...         self.color = color
    ...         self.mileage = mileage

    >>> myCar = Car('red', 37281)
    >>> print(myCar)
    >>> myCar

    >>> class Car:
    ...     def __init__(self, color, mileage):
    ...         self.color = color
    ...         self.mileage = mileage
    ...
    ...     def __str__(self):
    ...         return f'a {self.color} car'
    ...
    ... myCar = Car('red', 37281)
    ... print(myCar)
    ... myCar                         # here we need __repr__
    ```

[*Return to the Top*](#table-of-content)

- `__repr__`: Inspecting an object in a Python interpreter session simply prints the result of the object’s __repr__.

    ```python
    >>> class Car:
    ...     def __init__(self, color, mileage):
    ...         self.color = color
    ...         self.mileage = mileage
    ...
    ...     def __repr__(self):
    ...         """
    ...         __class__.__name__: return the name of the class.
    ...         !r conversion flag: the output string uses repr(self.color) and repr(self.mileage)
    ...         instead of str(self.color) and str(self.mileage).
    ...         """
    ...         return (f'__repr__: {self.__class__.__name__}({self.color!r}, {self.mileage!r})')
    ...
    ...     def __str__(self):
    ...         return f'__str__: a {self.color} car.'
    ...
    ... myCar = Car('red', 37281)
    ... print(myCar)
    ... print(str(myCar))
    ... myCar              # Since we have __repr__: this will print usefull information.
    ```

[*Return to the Top*](#table-of-content)

- We'll Create a datetime.date object and find out how it uses `__repr__` and `__str__` to control string conversion.

    ```python
    >>> import datetime

    >>> today = datetime.date.today()
    >>> today                   #  datetime.date(2020, 8, 27)
    >>> print(today)            # 2020-08-27
    ```

#### Key Takeaways
    - You can control to-string conversion in your own classes using the '__str__' and '__repr__'
    - The result of '__str__' should be readable.
    - The result of '__repr__' should be unambiguous.
    - Always add a '__repr__' to your classes.
    - The default implementation for __str__ just calls __repr__.

[*Return to the Top*](#table-of-content)

### Defining Your Own Exception Classes

```python
>>> class NameTooShortError(ValueError):
...     """
...     Class that extends the built-in ValueError
...     Generally, you’ll want to either derive your custom exceptions from the root Exception class
...     or the other built-in Python exceptions like ValueError or TypeError.
...     """
...     def __str__(self):
...         return 'Name must be greater than 5 chars'

>>> def validate_name(name):
...     if len(name) < 6:
...         raise NameTooShortError(name)

>>> validate_name('dabve')
[OUT] NameTooShortError: Name must be greater than 5 chars
```

[*Return to the Top*](#table-of-content)

### Copying Arbitrary Objects

```python
>>> class Point:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
... 
...     def __repr__(self):
...         return f'{__class__.__name__}({self.x!r}, {self.y!r})'
 

>>> class Rectangle:
...     def __init__(self, topLeft, bottomRight):
...         self.topLeft = topLeft
...         self.bottomRight = bottomRight
 
...     def __repr__(self):
...         return f'{__class__.__name__}({self.topLeft!r}, {self.bottomRight!r})'


>>> import copy
>>> rect = Rectangle(Point(0, 1), Point(5, 6))
>>> c_rect = copy.copy(rect)
>>> print('rect  : {}'.format(rect))            # rect: Rectangle(Point(0, 1), Point(5, 6))
>>> print('crect : {}'.format(c_rect))          # c_rect: Rectangle(Point(0, 1), Point(5, 6))
 
# Shallow Copy
>>> rect.topLeft.x = 999
>>> print('rect  : {}'.format(rect))            # rect: Rectangle(Point(999, 1), Point(5, 6))
>>> print('crect : {}'.format(c_rect))          # c_rect: Rectangle(Point(999, 1), Point(5, 6))
 
>>> print('Deep Copy')
>>> rect = Rectangle(Point(0, 1), Point(5, 6))
>>> d_rect = copy.deepcopy(rect)
>>> rect.topLeft.x = 999
>>> print('rect  : {}'.format(rect))            # rect: Rectangle(Point(999, 1), Point(5, 6))
>>> print('crect : {}'.format(d_rect))          # rect: Rectangle(Point(0, 1), Point(5, 6))
```

[*Return to the Top*](#table-of-content)

### Class vs Instance Variable Pitfalls

- **Class variables** are declared inside the class definition (but outside of any instance methods).
- **Instance variables** are always tied to a particular object instance.

- Class variables are for data shared by all instances of a class.
- They belong to a class, not a specific instance and are shared among all instances of a class.


- Instance variables are for data that is unique to each instance.
- They belong to individual object instances and are not shared among the other instances of a class.
- Each instance variable gets a unique backing store specific to the instance.
- Because class variables can be “shadowed” by instance variables of the same name, it’s easy to (accidentally) override class variables in a way that introduces bugs and odd behavior.

```python
>>> class Dog:
...     num_legs = 4                # <- Class Variable
... 
...     def __init__(self, name):
...         self.name = name        # <- Instance Variable


>>> jack = Dog('Jack')
>>> jill = Dog('Jill')
>>> print(f'{jack.name}, {jill.name}')                              # jack, jill
>>> print(f'{jack.num_legs}, {jill.num_legs}, {Dog.num_legs}')      # 4, 4, 4

>>> jack.num_legs = 6
>>> print(f'{jack.num_legs}, {jill.num_legs}, {Dog.num_legs}')      # 6, 4, 4
>>> print(f'{jack.num_legs}, {jack.__class__.num_legs}')            # 6, 4
```

```python
>>> class CountedObject:
...     num_instance = 0
... 
...     def __init__(self):
...         self.__class__.num_instance += 1
...         # self.num_instance += 1        # this is a wrong code
...         # because this will shadow the num_instance class variable by creating an
...         # instance variable of the same name in the constructor.

>>> print(CountedObject.num_instance)       # 0
>>> CountedObject().num_instance            # 1
>>> CountedObject().num_instance            # 2
>>> CountedObject().num_instance            # 3
>>> print(CountedObject.num_instance)       # 3
```

[*Return to the Top*](#table-of-content)

### Instance, Class, and Static Methods Demystified

- Instance methods need a class instance and can access the instance through self.
- Class methods don-t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
- Static methods don't have access to cls or self.
- They work like regular functions but belong to the class's namespace.
- Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have definite maintenance benefits.

```python
>>> class MyClass:
...     def method(self):
...         return 'Instance Method Called:', self
 
...     @classmethod
...     def classmethod(cls):
...         return 'Class Method Called:', cls
 
...     @staticmethod
...     def staticmethod():
...         return 'Static Method Called'
 
>>> obj = MyClass()
>>> print(obj.method())             # ('Instance Method Called:', <__main__.MyClass object at 0x7f58854b0bb0>)
>>> print(obj.classmethod())        # ('Class Method Called:', <class '__main__.MyClass'>)
>>> print(obj.staticmethod())       # Static Method Called
```

```python
>>> class Pizza:
...     def __init__(self, ingredient):
...         self.ingredient = ingredient
 
...     def __repr__(self):
...         return f'{self.__class__.__name__}({self.ingredient})'
 
...     @classmethod
...     def margherita(cls):
...         return cls(['mozzarella', 'tomatoes'])
 
...     @classmethod
...     def prosciutto(cls):
...         return cls(['mozzarella', 'tomatoes', 'ham'])
 
>>> pizza = Pizza(['cheeze', 'tomatos'])        
>>> print(pizza)                            # Pizza(['cheeze', 'tomatos'])
>>> print(pizza.margherita())               # Pizza(['mozzarella', 'tomatoes'])
>>> print(pizza.prosciutto())               # Pizza(['mozzarella', 'tomatoes', 'ham'])
```

[*Return to the Top*](#table-of-content)
