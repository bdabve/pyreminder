<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Backslash on Windows and Forward Slash on OS X and Linux](#backslash-on-windows-and-forward-slash-on-os-x-and-linux)
- [The Current Working Directory](#the-current-working-directory)
- [Creating New Folders](#creating-new-folders)
- [Handling Absolute and Relative Paths](#handling-absolute-and-relative-paths)
- [Checking Path Validity](#checking-path-validity)
- [Finding File Sizes and Folder Contents](#finding-file-sizes-and-folder-contents)
- [Copying Files and Folders](#copying-files-and-folders)
- [Moving and Renaming Files and Folders](#moving-and-renaming-files-and-folders)
- [Permanently Deleting Files and Folders](#permanently-deleting-files-and-folders)
- [Safe Deletes with the send2trash Module](#safe-deletes-with-the-send2trash-module)
- [Walking a Directory Tree](#walking-a-directory-tree)
- [The glob Module](#the-glob-module)


## Handling File and Directory Paths

- There are two main modules in Python that deals with path manipulation.
- One is the **_os.path_** module and the other is the **_pathlib_**  module.
- The **_pathlib_** module was added in Python 3.4, offering an object-oriented way to handle file system paths.

### Backslash on Windows and Forward Slash on OS X and Linux

- On Windows, paths are written using backslashes (`\`) as the separator between folder names. 
- On Unix based operating system such as macOS, Linux, and BSDs, the forward slash (`/`) is used as the path separator. 
- Joining paths can be a headache if your code needs to work on different platforms.

- Fortunately, Python provides easy ways to handle this. 
- We will showcase how to deal with this with both **_os.path.join_** and **_pathlib.Path.joinpath_**


  ```python
  >>> import os
  >>> from pathlib2 import Path
  >>>
  >>> os.path.join('usr', 'bin', 'spam')                            # windows: 'user\\bin\\spam'
  >>> print(Path('usr').joinpath('bin').joinpath('spam'))           # windows: user\bin\spam
 
  # pathlib also provides a shortcut to joinpath using the `/` operator:
  >>> print(Path('usr') / 'bin' / 'spam')                           # windows: user\bin\spam 

  >>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
  >>> for filename in my_files:
  ...     print(os.path.join('C:\\Users\\asweigart', filename))
  C:\Users\UP4\account.txt
  C:\Users\UP4\details.csv
  C:\Users\UP4\invite.docx

  # pathlib
  >>> my_files = ['accounts.txt', 'details.csv', 'invite.docx']
  >>> home = Path.home()
  >>> for filename in my_files:
  ...     print(home / filename)
  C:\Users\UP4\account.txt
  C:\Users\UP4\details.csv
  C:\Users\UP4\invite.docx
  ```

### The Current Working Directory

```python
>>> import os
>>> os.getcwd()

>>> from pathlib2 import Path
>>> print(Path.cwd())
```

### Creating New Folders

```python
>>> import os
>>> os.makedirs('C:\\delicious\\walnut\\waffles')

>>> from pathlib2 import Path
>>> cwd = Path.cwd()
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir()              # Error: delicious does not exist
>>> (cwd / 'delicious' / 'walnut' / 'waffles').mkdir(parents=True)
```

### Handling Absolute and Relative Paths

- To see if a path is an absolute path:

  ```python
  >>> import os
  >>> os.path.isabs('/')        # True
  >>> os.path.isabs('..')       # False

  >>> from pathlib2 import Path
  >>> Path('/').is_absolute()       # False
  >>> Path('..').is_absolute()      # False
  ```

- You can extract an absolute path with both `os.path` and `pathlib`

  ```python
  >>> import os
  >>> os.path.abspath('..')                     # 'D:\\my_Folder\\backups\\python'

  >>> from pathlib2 import Path
  >>> print(Path('..').resolve())               # WindowsPath('D:/my_Folder/backups/python')
  ```

- You can get a relative path from a starting path to another path.

  ```python
  >>> import os
  >>> os.path.relpath('/etc/passwd', '/')

  >>> from pathlib2 import Path
  >>> print(Path('/etc/passwd').relative_to('/'))
  ```

### Checking Path Validity

- Checking if a file/directory exists:

  ```python
  >>> import os
  >>> os.path.exists('.')                       # True
  >>> os.path.exists('setup.py')                # True
  >>> os.path.exists('/etc')                    # True
  >>> os.path.exists('nonexistentfile')         # False

  >>> from pathlib2 import Path
  >>> Path('.').exists()                        # True
  >>> Path('setup.py').exists()                 # True
  >>> Path('/etc').exists()                     # True
  >>> Path('nonexistentfile').exists()          # False
  ```

- Checking if a path is a file:

  ```python
  >>> import os
  >>> os.path.isfile('setup.py')            # True
  >>> os.path.isfile('/home')               # False
  >>> os.path.isfile('nonexistentfile')     # False

  >>> from pathlib2 import Path
  >>> Path('setup.py').is_file()            # True
  >>> Path('/home').is_file()               # False
  >>> Path('nonexistentfile').is_file()     # False
  ```

- Checking if a path is a directory:

  ```python
  >>> import os
  >>> os.path.isdir('/')            # True
  >>> os.path.isdir('setup.py')     # False
  >>> os.path.isdir('/spam')        # True

  >>> from pathlib2 import Path
  >>> Path('/').is_dir()            # True
  >>> Path('setup.py').is_dir()     # False
  >>> Path('/spam').is_dir()        # True
  ```

### Basename, and files manipulations

  ```python
  >>> import os
  >>> os.path.basename('C:\Users\UP4\file.py')            # 'file.py'

  >>> os.path.dirname('/home/dabve/calc.exe')             # return /home/dabve
  >>> os.path.split('/home/dabve/calc.exe')               # return ('/home/dabve', 'calc.exe')
  >>> os.path.splitext('/home/dabve/calc.exe')            # return ('/home/dabve/calc', '.exe')
  ```

### Finding File Sizes and Folder Contents

- Getting a file's size in bytes:

  ```python
  >>> import os
  >>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
  >>> os.stat('filename').st_size                                   # File Size
  >>> os.stat('file_name')                                          # File information
  >>> os.stat('filename').st_mtime                                  # Modification time
  >>> datetime.fromtimestamp(os.stat('filename').st_mtime)          # Modification time human readable

  >>> from pathlib import Path
  >>> stat = Path('/bin/python3.6').stat()
  >>> print(stat)                         # stat contains some other information about the file as well
  >>> print(stat.st_size)                 # size in bytes
  ```

- Listing directory contents using `os.listdir` on Windows:

  ```python
  >>> import os
  >>> os.listdir('C:\\Windows\\System32')

  >>> from pathlib import Path
  >>> for f in Path('/usr/bin').iterdir():
  ...     print(f)
  ```

- To find the total size of all the files in this directory:

  > **WARNING**: Directories themselves also have a size! So you might want to check for whether a path is a file or directory using the methods in the methods discussed in the above section!

  ```python
  >>> import os

  >>> total_size = 0
  >>> for filename in os.listdir('C:\\Windows\\System32'):
  ...     total_size = total_size + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
  >>> print(total_size)

  >>> from pathlib import Path
  >>> total_size = 0
  >>> for sub_path in Path('/usr/bin').iterdir():
  ...     total_size += sub_path.stat().st_size
  >>> print(total_size)
  ```

***

### Copying Files and Folders

- The *_shutil_* (shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.
- [shutil doc]()

  ```python
  >>> import shutil

  >>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
  
  # Copying and renaming file
  >>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')       # Out: 'C:\\delicious\\eggs2.txt'
  ```

- While *_shutil.copy()_* will copy a single file, *_shutil.copytree()_* copy an entire folder and every folder and file contained in it:

  ```python
  >>> import shutil
  
  # Copy the folder along with all of its files and subfolders, to the folder at the path destination.
  >>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
  ```

### Moving and Renaming Files and Folders

```python
>>> import shutil
>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
```

- The destination path can also specify a filename. In the following example, the source file is moved and renamed:

  ```python
  # Move and rename
  >>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')         # Out: 'C:\\eggs\\new_bacon.txt'
  ```

- If there is no eggs folder, then move() will rename bacon.txt to a file named eggs.

  ```python
  # Rename bacon.txt to a file named eggs.
  >>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
  ```

***

### Permanently Deleting Files and Folders

- Calling **_os.unlink(path)_** or **_Path.unlink()_** will delete the file at path.
- Calling **_os.rmdir(path)_** or **_Path.rmdir()_** will delete the folder at path. This folder must be empty of any files or folders.
- Calling **_shutil.rmtree(path)_** will remove the folder at path, and all files and folders it contains will also be deleted.

### Safe Deletes with the send2trash Module

- You can install this module by running `pip install send2trash` from a Terminal window.
- [send2trash doc]()

  ```python
  >>> import send2trash

  >>> with open('bacon.txt', 'a') as bacon_file:        # creates the file
  ...     bacon_file.write('Bacon is not a vegetable.')

  >>> send2trash.send2trash('bacon.txt')
  ```

### Walking a Directory Tree

  ```python
  >>> import os

  >>> for folder_name, subfolders, filenames in os.walk('C:\\delicious'):
  ...     print('The current folder is {}'.format(folder_name))
  ...     for subfolder in subfolders:
  ...         print('SUBFOLDER OF {}: {}'.format(folder_name, subfolder))
  ...     for filename in filenames:
  ...         print('FILE INSIDE {}: {}'.format(folder_name, filename))
  ```


___

### The 'glob' Module

- Glob is used to retrieve files/pathnames matching a specified pattern.
- for more information see [glob doc](https://docs.python.org/3/library/glob.html)

  ```python
  >>> import os, glob
  >>> for name in glob.glob('/home/*.py'):
  ..     print(name)

  # `/**/`: will match any files or directory
  >>> for fname in glob.glob('/home/username/python/**/*.txt', recursive=True):
  ..     print(fname)

  # rename files
  >>> dirname = 'dataScience'
  >>> for file in glob.glob(dirname + '/*'):
  ..     head, tail = os.path.split(file)
  ..     print('from: {}/{:<35} => {}'.format(head, tail, ('./data_science/' + tail)))

  # OUT:
  from: ./dataScience/matplotlib_coreySchafer.ipynb       => ./data_science/matplotlib_coreySchafer.ipynb
  from: ./dataScience/matplotlib_pythonCrashCourse.ipynb  => ./data_science/matplotlib_pythonCrashCourse.ipynb
  from: ./dataScience/numpy.ipynb                         => ./data_science/numpy.ipynb
  from: ./dataScience/starting_pandas.ipynb               => ./data_science/starting_pandas.ipynb
  ```
