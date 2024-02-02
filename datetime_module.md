<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content
- [Date](#date)
- [DateTime](#datetime)
- [Pytz](#pytz)
- [timestamp to datetime](#timestamp-to-datetime)
- [Comparing Dates](#comparing-dates)
- [Time Delta](#time-delta)
- [Datetime to String](#datetime-to-string)
- [String to Datetime](#string-to-datetime)
- [Measure Run Code](#measure-run-code)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

### Date

```python
>>> from datetime import date
>>> tday = date.today()
>>> print(tday)                               # 2019-10-21
>>> print(tday.day, tday.month, tday.year)    # 21 10 2019
>>> print(tday.weekday())                     # 0
>>> print(tday.isoweekday())                  # 1
>>> print(tday.isoformat())                   # '2019-10-21'
>>> print('{:%d-%m-%Y}'.format(today))        # 21-10-2019

>>> birthday = datetime.datetime(1986, 11, 18)
>>> print('[+] You have {} age old.'.format(today.year - birthday.year))
```

[*Return to the Top*](#table-of-content)

### DateTime

```python
>>> import datetime
>>> print(datetime.datetime.now())                              # 2019-10-21 12:43:46.608518
>>> today = datetime.datetime.now()
>>> print(today.day, today.month, today.year, sep='-')          # 21-10-2019
>>> print(today.hour, today.minute, today.second, sep=':')      # 12:44:14
>>> print('{:%Y-%m-%d %H:%M}'.format(today))                    # 21-10-2019 12:44:14
>>> print(today.timetuple())                                    # get time in tuple
time.struct_time(tm_year=2019, tm_mon=10, tm_mday=21, tm_hour=12, tm_min=44, tm_sec=14, tm_wday=0, tm_yday=294, tm_isdst=-1)

>>> print(datetime.datetime.utcnow())                           # time in utc
```

[*Return to the Top*](#table-of-content)

### Pytz

```python
>>> import datetime
>>> import pytz

>>> dt = datetime.datetime(2017, 4, 25, 12, 30, 45, tzinfo=pytz.UTC)        # using pytz
>>> dt_now = datetime.datetime.now(tz=pytz.UTC)                             # Preferable.
>>> print(dt_now)                                                           # 2019-10-21 11:52:16.259420+00:00

>>> dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
>>> dt_ustimezone = dt_now.astimezone(pytz.timezone('US/Mountain'))
>>> dt_dztimezone = dt_now.astimezone(pytz.timezone('Africa/Algiers'))
>>> print(datetime.datetime.now(tz=pytz.timezone('Africa/Algiers')))        # 2019-10-21 12:53:23.763150+01:00

# get all timezones
>>> timezones = [tz for tz in pytz.all_timezones]
```

[*Return to the Top*](#table-of-content)

### timestamp to datetime

```python
>>> print(datetime.datetime.fromtimestamp(1000000))       # 1970-01-12 13:46:40
>>> import time                                           # time.time() give a timestamp
>>> print(datetime.datetime.fromtimestamp(time.time()))   # 2019-10-21 13:36:57.601109
```

[*Return to the Top*](#table-of-content)

### Comparing Dates

```python
>>> halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
>>> newYear2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
>>> oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
>>> print(halloween2015 == oct31_2015)                    # True
>>> print(halloween2015 > newYear2016)                    # False
>>> print(newYear2016 > oct31_2015)                       # True
>>> print(newYear2016 != halloween2015)                   # True
```

[*Return to the Top*](#table-of-content)

### Time Delta

- Difference between two datetime values

    ```python
    >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    >>> print(delta)                                              # 11 days, 10:09:08
    >>> print(delta.days, delta.seconds, delta.microseconds)      # 11 36548 0
    >>> print(delta.total_seconds())                              # 986948.0

    >>> thousandDays = datetime.timedelta(days=1000)
    >>> print(datetime.date.today() + thousandDays)               # 2022-07-17

    >>> mybirthday = datetime.date(1986, 11, 18)
    >>> till_birthday = tday - mybirthday                 # will return timedelta object

    >>> # Pausing until a specific date
    >>> pause = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3)  # afteer 3 seconds
    >>> while datetime.datetime.now() < pause:
    ...     time.sleep(1)
    ```

[*Return to the Top*](#table-of-content)

### Datetime to String

- Use the <strftime()> method to displey a datetime object as a string.

|strftime  | directive Meaning
|:--------:|-------------------------------------------------
|   `%Y`     | Year with century, as in '2014'
|   `%y`     | Year without century, '00' to '99' (1970 to 2069)
|   `%m`     | Month as a decimal number, '01' to '12'
|   `%B`     | Full month name, as in 'November'
|   `%b`     | Abbreviated month name, as in 'Nov'
|   `%d`     | Day of the month, '01' to '31'
|   `%j`     | Day of the year, '001' to '366'
|   `%w`     | Day of the week, '0' (Sunday) to '6' (Saturday)
|   `%A`     | Full weekday name, as in 'Monday'
|   `%a`     | Abbreviated weekday name, as in 'Mon'
|   `%H`     | Hour (24-hour clock), '00' to '23'
|   `%I`     | Hour (12-hour clock), '01' to '12'
|   `%M`     | Minute, '00' to '59'
|   `%S`     | Second, '00' to '59'
|   `%p`     | 'AM' or 'PM'
|   `%%`     | Literal '%' character


```python
>>> tday = datetime.datetime.now()
>>> print(tday.strftime('%Y/%m/%d %H:%M:%S'))
>>> print(tday.strftime('%I:%M %p'))
>>> print(tday.strftime("%B of '%y"))
```

[*Return to the Top*](#table-of-content)

### String to Datetime

- The < strptime() > function is the inverse of the < strftime() > method.

    ```python
    >>> print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))                # 2015-10-21 00:00:00
    >>> print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))     # 2015-10-21 16:29:00
    >>> print(datetime.datetime.strptime("November of '63", "%B of '%y"))                 # 2063-11-01 00:00:00
    ```

[*Return to the Top*](#table-of-content)

### Measure Run Code

```python
>>> import time
>>> import datetime
>>> separator = ('-' * 50)
>>> def calcProd():
...     # Calculate the product of the first 100,000 numbers.
...     product = 1
...     for i in range(1, 1000):
...         product = product * i
...     return product

>>> startTime = time.time()
>>> product = calcProd()
>>> endTime = time.time()
>>> print('The resutl is {:d} digits long'.format(len(str(product))))
>>> print('Took {} second to calculate.'.format(endTime - startTime))
```

- Pressing ctrl-c will not interrupt time.sleep() calls in IDLE.
- To work around this problem, instead of having a single < time.sleep(30) > call to pause for 30 seconds, use a for loop to make 30 calls to < time.sleep(1) >

    ```python
    >>> for i in range(30): time.sleep(1)
    ```

- Using the < round() > function

    ```python
    >>> now = time.time()
    >>> print('now          : ', now)
    >>> print('round(now, 2): ', round(now, 2))
    >>> print('round(now, 4): ', round(now, 4))
    >>> print('round(now)   : ', round(now))
    >>> print('with format  : {:.2f}'.format(now))
    ```
[*Return to the Top*](#table-of-content)
