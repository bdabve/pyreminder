<link rel="stylesheet" href="style.css">

## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)


### Getting Started

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help='display a square of a given number', type=int)
args = parser.parse_args()
print(args.square ** 2)
```

### Optional arguments

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

### Combining Positional and Optional Arguments

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('square', type=int, help='display a square of a given number')
parser.add_argument('-v', '--verbosity', action='store_true', help='increase output verbosity')   # sotre_true == True | False
args = parser.parse_args()
answer = args.square ** 2
if args.verbosity:
    print('the square of {} equals {}'.format(args.square, answer))
else:
    print(answer)
```

### Restrict with choice

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int, help='display a square of a given number')
# parser.add_argument('-v', '--verbose', type=int, choices=[0, 1, 2], help='increase output verbosity')
# The count vaule of action is to use the scipt like : ./script 4 -v | -vv | -vvv | ...
# set the default value to 0
parser.add_argument('-v', '--verbose', action='count', default=0, help='increase output verbosity')
args = parser.parse_args()
answer = args.square ** 2
if args.verbose >= 2:
    print("the squre of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
    print('{}² = {}'.format(args.square, answer))
else:
    print(answer)
```

### Add a group

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponenet')

# add group
# this will prevent using -vq, and produce an error
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true', help='verbose mode')
group.add_argument('-q', '--quit', action='store_true', help='quit mode')

args = parser.parse_args()
answer = args.x ** args.y
if args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
elif args.quit:
    print(answer)
else:
    print('{}^{} = {}'.format(args.x, args.y, answer))
```

- The following program takes a list of integers and produces either the sum or the max.

- metavar : used when generating help messages.
- nargs   : multiple argument (ex: multiple file name to work with)

    ```python
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers')
    parser.add_argument('integer', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, defaul=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.accumulate(args.integers))
    ```

    ```bash
    $ python testing_argparse.py 1 2 3 10 5                 # 10
    $ python testing_argparse.py 1 2 3 10 5 --sum           # 21
    ```

### More options for <parser.ArgumentParser>

- the programe name, is available to help messages using the '%(prog)s' format specifier
- usage='usage', override the default message of usage
- epilog='Examples', display additional description.

    ```python
    import argparse

    parser = argparse.ArgumentParser(
        prog='myprogram',
        usage='%(prog)s [options]',
        description='Process some integers',
        epilog='Example: %(prog)s --foo foo. For more information see https://example.com')
    parser.add_argument('--foo', help='foo of the %(prog)s program')
    args = parser.parse_args()
    ```

- Passing <RawDescriptionHelpFormatter> as <formatter_class=> indicates that description and epilog are already correctly
  formatted and should not be line-wrapped:

    ```python
    parser = argparse.ArgumentParser(prog='MYPROG', formatter_class=argparse.RawDescriptionHelpFormatter,
        description=('''
    Please do not mess up the text!
    -------------------------------
        I have indented it
        exactly the way
        i want it'''),
        epilog='''
    Example: %(prog)s --foo foo.
    For more information see https://example.com'''
    )
    ```

### More options for <parser.add_argument>

```python
parser = argparse.ArgumentParser()
# store_const: this stores the value specified by the const keyword argument.
parser.add_argument('--foo', action='store_const', const=42)
# store_true and store_false: create a default values of False and True
parser.add_argument('--bar', action='store_true')
# append: This stores a list, and appends each argument value to the list.
parser.add_argument('--colors', action='append')
args = parser.parse_args()
print(args.foo, args.bar)                   # foo=42 True
```

### nargs=?

```python
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args()
print(args.infile)
print(args.outfile)
$ ./prog input.txt output.txt   # open file 'input.txt', mode 'r' at 0x...>, outfile=<open file 'output.txt', mode 'w' at 0x...>
$ ./prog
<_io.TextIOWrapper name='<stdin>' mode='r' encoding='cp65001'>
<_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp65001'>
```

| option    | Meaning   | 
|-----------|-----------|
| nargs='*' | all command-line arguments present are gathered into a list.
| nargs='+' | just like '*' additionally, an error msg will be generated if there wasn't at least one argument
| type      | The type to which the command-line argument should be converted. ex(int, str, file, argparse.FileType('w'), float..)
| default   | default value
| choices   | select from a restrected set of values. choices=['rock', 'paper', 'scissors']
| required  | Whether or not the command-line option may be omitted (optionals only).
| metavar   | A name for the argument in usage messages.
| dest      | The name of the attribute to be added to the object returned by parse_args().

