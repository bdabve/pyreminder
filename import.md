<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)
- [Jupyter Notebook](https://mybinder.org/v2/gh/wilfredinni/python-cheatsheet/master?filepath=jupyter_notebooks)

## Table of Content

- [Making a Hierarchical Package of Modules](#making-a-hierarchical-package-of-modules)
- [Making Separate Directories of Code Import Under a Common Namespace](#making-separate-directories-of-code-import-under-a-common-namespace)
- [Reloading Modules](#reloading-modules)
- [Reading Datafiles Within a Package](#reading-datafiles-within-a-package)
- [Adding Directories to sys path](#adding-directories-to-sys-path)

***

- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)
- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)

### Making a Hierarchical Package of Modules

- Just organize your code as you wish on the filesystem and make sure that every directory defines an < __init__.py > file.
- Suppose that we have this structure
    ```
    graphics/
        __init__.py
        primitive/
            __init__.py
             line.py
             fill.py
             text.py
        formats/
             __init__.py
             png.py
             jpg.py
    ```
- Now we shold be able to perform various import statements, such as the following:

    ```python
    >>> import graphics.primitive.line
    >>> from graphics.primitive import line
    >>> import graphics.formats.jpg as jpg
    ```

[*Return to the Top*](#table-of-content)

### Making Separate Directories of Code Import Under a Common Namespace

- A namespace package is a special kind of package designed for merging different dirs of code together under a common namespace

    ```
    foo-package/
        spam/
            blah.py
    bar-package/
        spam/
        grok.py
    ```

- From python
    ```python
    >>> import sys
    >>> sys.path.extend(['foo-package', 'bar-package'])
    >>> import spam.blah
    >>> import spam.grok
    ```

[*Return to the Top*](#table-of-content)

### Reloading Modules

- You want to reload an already loaded module because you’ve made changes to its source.

    ```python
    >>> import spam
    >>> import imp
    >>> imp.reload(spam)                # <module 'spam' from './spam.py'>
    ```

[*Return to the Top*](#table-of-content)

### Reading Datafiles Within a Package

- Your package includes a datafile that your code needs to read.

    ```
    mypackage/
        __init__.py
        somedata.dat
        spam.py
    ```

- spam.py

    ```python
    >>> import pkgutil
    >>>data = pkgutil.get_data(__package__, 'somedata.dat')

    ```

[*Return to the Top*](#table-of-content)

### Adding Directories to sys path

```python
>>> print(sys.path)
>>> import sys

# add path to PYTHONPATH
  >>> sys.path.insert(0, '/some/dir')
  >>> sys.path.insert(0, '/other/dir')

# The hardcode
  >>> from os.path import abspath, join, dirname
  >>> sys.path.insert(0, abspath(dirname('__file__'), 'src'))
```
