<link rel="stylesheet" href="style.css">

## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Basic Operations](#basic-operations)
- [os.path](#os.path)
- [Workig with files](#workig-with-files)
- [Using Environement Variable](#using-environement-variable)
- [Commonly used os module tools](#commonly-used-os-module-tools)
- [sys module](#the-sys-module)
- [Subprocess call and run command](#subprocess-call-and-run-command)
- [Subprocess popen command](#subprocess-popen-command)
- [The platform module](#the-platform-module)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

### Basic operations

```python
>>> os.system('pip install colorama')           # Runs a shell command from a Python script
>>> os.system('pip install colorama')           # Runs a shell command from a Python script

>>> os.system('cls' if os.name == 'nt' else 'clear')

>>> os.getcwd()                                  # Current directory(pwd)
>>> os.chdir('/home/dabve')                      # Changing directory
>>> os.listdir()                                 # Listing working dir.
>>> os.mkdir('/home/dabve/documents/pytest')     # Create a single folder
>>> os.makedirs('/home/dabve/test/pytest')       # Create all the intermediate folders in a path if they don’t already exist.
>>> os.rename('python', 'bash')                  # Rename python to bash
>>> os.rmdir('python')                           # Remove  a folder.
>>> os.removedirs('python/sub-dir1')             # Remove nested empty directories recursively.
>>> os.remove('./python/test_file')              # Remove a file
```

[*Return to the Top*](#table-of-content)

### os.path

```python
>>> os.path.abspath('.')                      # 'D:\\my_Folder\\programming\\python'.
>>> os.path.isabs('.')                        # Return True or False
>>> os.path.relpath('.')                      # Return String of a relative path ex: ../../
>>> os.path.exists('/home/')                  # True or false
>>> os.path.isdir('/home/')                   # True or false
>>> os.path.dirname('/home/dabve/calc.exe')   # return /home/dabve
>>> os.path.split('/home/dabve/calc.exe')     # return ('/home/dabve', 'calc.exe')
>>> os.path.splitext('/home/dabve/calc.exe')  # return ('/home/dabve/calc', '.exe')
>>> os.path.join('usr', 'bin', 'spam')        # usr/bin/spam
>>>
>>> my_file = ['acount.txt', 'details.csv', 'invite.docx']
>>> for filename in my_file:
...     print(os.path.join('/home/dabve/bin', filename))
```

[*Return to the Top*](#table-of-content)

### Workig with files

```python
>>> os.path.getsize('file_name')              # Return the size in bytes
>>> os.path.isfile('/home/')                  # True or false
>>> os.path.basename('/home/dabve/calc.exe')  # return calc.exe
>>> os.stat('file_name')                      # File information
>>> os.stat('filename').st_size               # File Size
>>> os.stat('filename').st_mtime              # Modification time

>>> datetime.fromtimestamp(os.stat('filename').st_mtime)       # Modification time human

>>> os.chmod('spam.txt', 0777)                # chmod
```

[*Return to the Top*](#table-of-content)

### Using Environement Variable

```python
>>> os.environ                                          # Return a dict of all environement vars
>>> os.environ.get('home')                              # Printing Home Variable
>>> os.path.join(os.environ.get('home'), 'test.txt')    # Join two path
>>> os.environ['TEMP'] = r'c:\temp'                     # Change Value
>>> os.environ['USERNAME']                              # UP4
>>> os.environ['USERNAME'] = 'Dabve'                    # Changing value of username

>>> for k,v in os.environ.items():
...     print('{{:50}}: {{}}'.format(k, v))

>>> for dirname in os.environ['path'].split(os.pathsep):
...     print(dirname)

>>> os.system('echo %USERNAME%')                        # Dabve (outside python idle)
```

NB:

- Values assigned to 'os.environ' keys in this fashion are automatically exported to other parts of the application.
- That is, key assignments change both theos. environ object in the Python program as well as the associated variable
  in the enclosing shell environment of the running program's process.
- Internally, key assignments to 'os.environ' call 'os.putenva' function that changes the shell variable outside the
  boundaries of the Python interpreter.

[*Return to the Top*](#table-of-content)

### Commonly used os module tools

| Tasks                   | Tools
|-------------------------|---------------------------------------------------------------------
| Shell variables         | os.environ
| Running programs        | os.system, os.popen, os.popen2/3/4, os.startfile
| Spawning processes      | os.fork, os.pipe, os.exec, os.waitpid, os.kill
| Descriptor files, locks | os.open, os.read, os.write
| File processing         | os.remove, os.rename, os.mkfifo, os.mkdir, os.rmdir
| Administrative tools    | os.getcwd, os.chdir, os.chmod, os.getpid,os.listdir
| Portability tools       | os.sep, os.pathsep, os.curdir, os.path.split, os.path.join
| Pathname tools          | os.path.exists('path'), os.path.isdir('path'), os.path.getsize('path')

[*Return to the Top*](#table-of-content)

## The sys module

- The sys and os modules form the core of much of Python's system-related tool set.

    ```python
    >>> sys.platform      # 'win32'
    >>> sys.version       # 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)]
    >>> sys.system('cls' if sys.platform[:3] == 'win' else 'clear')

    >>> sys.path.append(r'C:\\mydir')
    ```

> Changing `sys.path` directly is an alternative to setting your `PYTHONPATH` shell variable. But not a very permanent one.

```python
>>> sys.path                              # ['', 'C:\\PP4thEd\\Examples', ..., 'C:\\mydir']
>>> sys.exit()

>>> sys.modules                               # All loaded modules
>>> list(sys.modules.keys())                  # modules is a dict of name:module
>>> sys.modules['sys']                        # information about the loaded module sys
>>> sys.argv                                  # Command-line arguments show up as a list of strings.
>>> sys.stdin, sys.stdout, and sys.stderr     # Standard streams are available as .
>>> sys.getdefaultencoding()                  # default encoding
```

- `sys.exc_info` function returns the latest exception's type, value, and traceback object

    ```python
    >>> try:
    ...     raise IndexError
    ... except:
    ...     print(sys.exc_info())          # (<class 'IndexError'>, IndexError(), <traceback object at 0x03080378>)
    ```

[*Return to the Top*](#table-of-content)

### Subprocess call and run command

- `call()` and `run()` are convenience functions and should be used for simpler cases.

    ```python
    >>> subprocess.call(['ls', '-lha'])
    ```

- unlike subprocess.call, this throws a CalledProcessError
- if the underlying process errors out

    ```python
    subprocess.check_call(["./bash-script-with-bad-syntax"])
    ```

- errors in the created process are raised here too

    ```python
    output = subprocess.check_output(["ls","-lha"],universal_newlines=True)
    ```

- run() returns a CompletedProcess object if it was successful
- errors in the created process are raised here too

    ```python
    p = subprocess.run(['ls', '-lha'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
    out = process.stdout

    p = subprocess.run(['ls', '-lha'])
    p           # CompletedProcess(args=['ls', '-lha'], returncode=0)
    ```

- `check=True`: force the python method to throw an exception if encounters errors

    ```python
    subprocess.run(['ls', 'bad_file'], check=True)
    ```

- stderr, stdout

    ```python
    from subprocess import run, PIPE
    cp = run(['ls', '-lha'], universal_newlines=True, stdout=PIPE, stderr=PIPE)
    cp.stdout
    cp.stderr
    cp.returncode
    ```

- catch exceptions

    ```python
    try:
        cp = subprocess.run(['./badfile', ' file.py'], universal_newlines=True, stdout=PIPE, stderr=PIPE)
    except FileNotFoundError as e:
        print(e)
    ```

[*Return to the Top*](#table-of-content)

### Subprocess popen command

- `Popen()` is much more powerful and handles all cases, not just simple ones.

    ```python
    from subprocess import Popen, PIPE
    p = subprocess.Popen(['ls', '-lha'])
    ```

- The `poll()` method will return None if the process is still running at the time `poll()` is called.
- if the program has terminated, it will return the process's ineger exit code

    ```python
    p.poll() == None          # True

    p.wait()                # will block until the launched process has terminated.
                            # The return value of wait() is the process's integer exit code.
    ```

- stdout, stderr

    ```python
    p = Popen(['ls', '-lha'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    output, errors = p.communicate()
    ```

- redirect output to a file

    ```python
    output_file = '/tmp/myoutput.txt'
    myoutput = open(output_file, 'w+')
    p = Popen(['ls', '-lha'], stdout=myoutput, stderr=PIPE, universal_newlines=True)
    output, errors = p.communicate()
    ```

- redirect output and errors to a file

    ```python
    output_file = '/tmp/myoutput.txt'
    myoutput = open(output_file, 'w+')
    p = Popen(['ls', '-lha'], stdout=myoutput, stderr=myoutput, universal_newlines=True)
    output, errors = p.communicate()
    ```


- this is equivalent to 'ls -lha | grep "foo bar"'

    ```python
    p1 = Popen(["ls","-lha"], stdout=PIPE)
    p2 = Popen(["grep", "foo bar"], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()

    output = p2.communicate()[0]
    ```

[*Return to the Top*](#table-of-content)

### The platform module

- Used to access the underlying platform’s data: hardware, operating system, and interpreter version information.

    ```python
    >>> import platform

    >>> platform.system()           # Get current platform: Linux, Windows, Darwin(mac)
    >>> platform.architecture()     # Architecture: 32bit | 64bit
    >>> platform.machine()          # x86 | x64
    >>> platform.version()          # Version
    >>> platform.platform()         # Output from windows: Windows-7-6.1.7600
    >>> platform.processor()        # Output from windows: 'x86 Family 6 Model 42 Stepping 7, GenuineIntel'
    >>> platform.python_version()   # Python version
    >>> platform.uname()            # All information like the uname command in linux
    ```

[*Return to the Top*](#table-of-content)
