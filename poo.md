<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content
- [Property Decorator](#property-decorator)
- [Creating Managed Attributes](#creating-managed-attributes)
- [Inheritance](#inheritance)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

### Inheritance

```python
>>> class Car():
...     def __init__(self, make, model, year):
...         """Initialize attributes to describe a car."""
...         self.make = make
...         self.model = model
...         self.year = year
...         self.odometerReading = 0
... 
...     def getDescriptiveName(self):
...         """Return a neatly formated descriptive name."""
...         longName = str(self.year) + ' ' + self.make + ' ' + self.model
...         return longName.title()
... 
...     def read_odometer(self):
...         """Print a statement showing the car's mileage"""
...         print('This car has ' + str(self.odometerReading) + ' miles on it.')
... 
...     def update_odometer(self, mileage):
...         """
...         Set the odometer reading to the given value.
...         Refect the change if it attempts to roll the odometer back.
...         """
...         if mileage >= self.odometerReading:
...             self.odometerReading = mileage
...         else:
...             print('[-] Error: You can\'t roll back an odometer!')
... 
...     def increment_odometer(self, miles):
...         """Add the given amount to the odometer reading"""
...         self.odometerReading += miles
... 
...     def fill_gas_tank(self, gas):
...         """Method to fill gas"""
...         print('Filling gas to: {}'.format(gas))
```

- Inheritance

```python
>>> class ElectricCar(Car):
...     """
...     Initialize attributes of the parent class.
...     Then initialize attributes specific to an electric car.
...     """
...     def __init__(self, make, model, year):
...         """Initialize attributes of the parent class."""
...         super().__init__(make, model, year)
...         self.battery = Battery()
... 
...     def fill_gas_tank(self, gas):
...         """
...         - Electric cars don't have gas tanks
...         - Override this method
...         """
...         print('This car doesn\'t need a gas tank!')


>>> class Battery():
...     """A simple attempt to model a battery for an electric car"""
... 
...     def __init__(self, batterySize=70):
...         """Initialize the battery's attributes."""
...         self.batterySize = batterySize
... 
...     def describe_battery(self):
...         """Print a statement describing the battery size."""
...         print('This car has a ' + str(self.batterySize) + '-kWh battery.')
... 
...     def get_range(self):
...         """Print a statement about the range this battery provides."""
...         if self.batterySize == 70:
...             range = 240
...         elif self.batterySize == 85:
...             range = 270
... 
...         msg = 'This car can go approcimately ' + str(range) + ' Miles on a full charge.'
...         print(msg)

# Creating Classes
>>> myCar = Car('audi', 'a4', 2016)
>>> myCar.getDescriptiveName()              # 2016 audi a4

>>> myCar.odometerReading = 200             # modify the value of odometerReading
>>> myCar.read_odometer()                   # This car has 200 miles on it.
>>> myCar.update_odometer(30)               # [-] Error: You can't roll back odometer!
>>> myCar.update_odometer(300)              
>>> myCar.read_odometer()                   # This car has 300 miles on it.

>>> myCar.odometerReading = 5               # this will work
>>> myCar.update_odometer(5)                # this wont work
>>> myCar.increment_odometer(100)            
>>> myCar.read_odometer()                   # This car has 105 miles on it.
>>> myCar.fill_gas_tank(60)                 # Filling gaz to 60
 
>>> myTesla = ElectricCar('tesla', 'model s', 2016)
>>> print(myTesla.getDescriptiveName())         # '2016 Tesla Model S'
>>> myTesla.fill_gas_tank(30)                   # This car doesn't need a gas tank!

>>> myTesla.battery.describe_battery()          # This car has a 70-kWh battery.
>>> myTesla.battery.get_range()                 # This car can go approcimately 240 Miles on a full charge.

>>> myTesla.battery.batterySize = 80
>>> myTesla.battery.get_range()                 # This car can go approcimately 270 Miles on a full charge.
```

[*Return to the Top*](#table-of-content)

### Property Decorator

```python
>>> class Employee:
... 
...     def __init__(self, first, last):
...         self.first = first
...         self.last = last
... 
...     @property           # Define a methode but access it like an atribute
...     def email(self):
...         return '{}.{}@email.com'.format(self.first, self.last)
... 
...     @property
...     def fullname(self):
...         # return the first and last name as fullname
...         return '{} {}'.format(self.first, self.last)
... 
...     @fullname.setter
...     def fullname(self, name):
...         first, last = name.split(' ')
...         # Modify first and last name from fullname method
...         self.first = first
...         self.last = last
... 
...     @fullname.deleter
...     def fullname(self):
...         """We can delete from this function"""
...         print('delete employee {}'.format(self.first))
...         self.first = self.last = None


>>> dabve = Employee('Dabve', 'Band')

>>> print(dabve.first)          # Dabve, Access it like an atribute
>>> print(dabve.fullname)       # Dabve Band
>>> print(dabve.email)          # Dabve.Band@email.com

>>> dabve.first = 'Meziane'
>>> print(dabve.first)          # Meziane
>>> print(dabve.fullname)       # Meziane Band
>>> print(dabve.email)          # Meziane.Band@email.com

>>> del dabve.fullname          # Delete Employee
>>> print(dabve.fullname)       # None, None
```

[*Return to the Top*](#table-of-content)

### Creating Managed Attributes

- Don’t write properties that don’t actually add anything extra like this.
- Properties should only be used in cases where you actually need to perform extra processing on attribute access.

    ```python
    >>> class Person:
    ...     def __init__(self, first_name):
    ...         self.first_name = first_name

    ...     @property                                   # Getter function.
    ...     def first_name(self):
    ...         return self._first_name

    ...     @first_name.setter                          # Setter function.
    ...     def first_name(self, value):
    ...         if not isinstance(value, str):
    ...             raise TypeError('Expected a string')
    ...         self._first_name = value

    ...     @first_name.deleter                         # Deleter function.
    ...     def first_name(self):
    ...         raise AttributeError("Can't delete attribute")

    >>> a = Person('Guido')
    >>> a.first_name            # Guido, Notice lack of ()
    >>> a.first_name = 42       # TypeError: Expected a string
    >>> a.first_name = 'dabve'  # OK
    >>> del a.first_name        # AttributeError: can't delete attribute
    ```

[*Return to the Top*](#table-of-content)
