<link rel="stylesheet" href="style.css">
## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [JSON](#json)
- [YAML](#yaml)
- [Anyconfig](#anyconfig)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## JSON, YAML and configuration files

### JSON

- Getting Started

  ```python
  >>> json.loads(jsonData)        # from json to python
  >>> json.dumps(pythonValue)     # from python to json

  >>> import json
  >>> jsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
  >>> json_to_python = json.loads(jsonData)

  >>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
  >>> python_to_json = json.dumps(pythonValue)
  ```

- Open a JSON file with:

  ```python
  >>> import json
  >>> with open("filename.json", "r") as f:
  ...     content = json.loads(f.read())
  ```

- Write a JSON file with:

  ```python
  >>> import json

  >>> content = {"name": "Joe", "age": 20}
  >>> with open("filename.json", "w") as f:
  ...     f.write(json.dumps(content, indent=2))
  ```

- The format of JSON encoding is almost identical to Python syntax except for a few minor changes.

  ```python
  >>> d = {'a': True, 'b': 'Hello', 'c': None}
  >>> json.dumps(d)                               # {"b": "Hello", "c": null, "a": true}
  ```

- `pprint()` with JSON

  ```python
  >>> import json, pprint
  >>> with open('json_file', 'rb') as json_f:
  ...     data = json.dumps(json_f)
  >>> pprint.pprint(data[0].keys())
  >>> pprint.pprint(data[0]['key'])
  ```

[*Return to the Top*](#table-of-content)

### YAML

- Compared to JSON, YAML allows a much better humain maintainance and gives ability to add comments.
- It is a convinient choice for configuration files where human will have to edit.

- There are two main librairies allowing to access to YAML files:

- [PyYaml](https://pypi.python.org/pypi/PyYAML)
- [Ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml)

- The first one it easier to use but the second one, Ruamel, implements much better the YAML
specification, and allow for example to modify a YAML content without altering comments.

- Open a YAML file with:

  ```python
  >>> from ruamel.yaml import YAML

  >>> with open("filename.yaml") as f:
  ...     yaml=YAML()
  ...     yaml.load(f)
  ```

[*Return to the Top*](#table-of-content)

### Anyconfig

- [Anyconfig](https://pypi.python.org/pypi/anyconfig) is a very handy package allowing to abstract completly the underlying configuration file format. 
- It allows to load a Python dictionary from JSON, YAML, TOML, and so on.

- Usage:

  ```python
  >>> import anyconfig

  >>> conf1 = anyconfig.load("/path/to/foo/conf.d/a.yml")
  ```

[*Return to the Top*](#table-of-content)
