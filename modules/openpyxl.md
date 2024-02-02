<link rel="stylesheet" href="style.css">

## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [](#)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

### Getting Started

```python
>>> import openpyxl

>>> wb = openpyxl.load_workbook('file.xlsx')

>>> wb.sheetnames               # The names of all worksheets of the workbook
>>> ws = wb['sheetName']        # Getting sheet by name
>>> ws = wb.active              # Getting sheet by Active sheet
>>> ws.title                    # Sheet Title
>>> ws.max_rows                 # max rows
>>> ws.max_columns              # max columns

>>> ws1 = wb.create_sheet("Mysheet")                            # insert at the end (default)
>>> ws2 = wb.create_sheet("Mysheet", 0)                         # insert at first position
>>> wb.create_sheet(index=1, title='First Sheet')               # Creating Another sheet at index 1.
>>> wb.remove_sheet(wb.get_sheet_by_name('First Sheet'))        # Removing sheet

>>> ws.title = "New Title"
>>> ws.sheet_properties.tabColor = "1072BA"     # The background color of the tab holding the title
```

- Create copies of worksheets within a single workbook

    ```python
    >>> source = wb.active
    >>> target = wb.copy_worksheet(source)
    ```

### Cells

```python
>>> c = ws['A15']                             # get cell number

# Column informations
>>> c.value, c.data_type, c.coordinate, c.encoding, c.font, c.has_syle, c.style .....
>>> prin('Row {}, Column {} is: {}'.format(c.row, c.column, c.value))

>> ws['A4'] = 4            # This will return the cell at A4, or create one if it does not exist yet.
>>> d = ws.cell(row=4, column=2, value=10)

>>> ws.cell(row=1, column=ws.max_column)                    # Last column
>>> ws.cell(row=ws.max_row, column=ws.max_columns)          # Last column and row

>>> sheet.cell(row=1, column=2)             # <Cell Sheet1.B1>
```

#### Ranges of cells

```python
>>> cell_range = ws['A1':'C2']
>>> col_range = ws['C:D']
>>> row10 = ws[10]
>>> row_range = ws[5:10]

>>> for rows in cell_range:
...     for row in rows:
...         print(row.coordinate, ': ',row.value)
...     print('-' * 20, ' End Of Row', '-' * 20)
```

- You can also use the Worksheet.iter_rows() method:

    ```python
    >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    ...     for cell in row:
    ...         print(cell)
    # Output:
    <Cell 'PDR juin'.A1>
    <Cell 'PDR juin'.B1>
    <Cell 'PDR juin'.C1>
    <Cell 'PDR juin'.A2>
    <Cell 'PDR juin'.B2>
    <Cell 'PDR juin'.C2>
    ```

- All cels

    ```python
    >>> for cells in tuple(ws.rows):        # ws.columns for columns dont forget to convert it to a tuple
    ...     for cell in cells:
    ...         print(cell)                 # You can use cell.value
    ```

- Getting all values

    ```python
    >>> for row in ws.values:
    ...     for value in row:
    ...         print(value)
    ```

- return only the values

    ```python
    >>> for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
    ...     print(row)
    ```

- Saving

    ```python
    >>> wb.save('balances.xlsx')
    ```

### copying a range into a new ws

```python
>>> wb = openpyxl.load_workbook('file.xlsx')
>>> ws = wb.active                              # source sheet
>>> max_cels = ws.cell(row=ws.max_row, column=ws.max_column).coordinate
>>> cell_range = ['A8':max_cels]

>>> ws_n = wb.create_sheet('New')               # target sheet
```

### inserting with the same cordinate as source sheet

```python
>>> for rows in cell_range:
...     for row in rows:
...         ws_n[row.coordinate] = row.value
...         # OR
...         ws_n.cell(row=row.row, column=row.column, value=row.value)
```

### incrementing

```python
>>> for rows in cell_range:
...     for row in rows:
...         ws_n.cell(row=row.row + 14, column=row.column, value=row.value)
... wb.save('file.xlsx')
```

### Formula

```python
>>> ws['A1'] = 200
>>> ws['A2'] = 300
>>> ws['A3'] = '=SUM(A1:A2)'
>>> wb.save('writeFormula.xlsx')

>>> ws['A3'].value              # '=SUM(A1:A2)'
>>> wbDataOnly = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
>>> ws = wbDataOnly.get_active_sheet()
>>> ws['A3'].value              # 500
```

### Working with styles

```python
>>> a1.font = Font(color=colors.RED, italic=True)

>>> from copy import copy

>>> b5 = ws['B5']
>>> b18 = ws['B18']
>>> b18.font = copy(b5.font)
>>> b18.border = copy(b5.border)
>>> b18.alignment = copy(b5.alignment)
```

### Merge and Unmerge Cells

```python
>>> ws.merge_cell('C34:E34')
>>> ws.unmerge_cells('A1:D3')
>>> ws.merge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
>>> ws.unmerge_cells(start_row=2,start_column=1,end_row=2,end_column=4)
```

### Dimensions

```python
>>> ws['A1'] = 'Tall row'
>>> ws['B2'] = 'Wide column'
>>> ws.row_dimensions[1].height = 70
>>> ws.column_dimensions['B'].width = 20
>>> wb.save('dimensions.xlsx')
```

### Freeze

```python
>>> ws.freeze_panes = 'A10'         # Row 1 to 9
>>> sheet.freeze_panes = 'A2'       # Row 1
>>> sheet.freeze_panes = 'B1'       # Column A
>>> sheet.freeze_panes = 'C1'       # Columns A and B
>>> sheet.freeze_panes = 'C2'       # Row 1 and columns A and B
>>> sheet.freeze_panes = 'A1' or
>>> sheet.freeze_panes = None       # No frozen panes
```

### Update Produce - Corrects costs in produce sales spreadsheet.

```python
>>> import openpyxl

>>> wb = openpyxl.load_workbook('fromPython.xlsx')
>>> ws = wb.active

# The produce types and their updated prices
>>> PRICE_UPDATES = {'Fusible 250V 6 x 32 10A': 200, 'courroie T5-940': 300}

# Loop through the rows and update the prices.
>>> try:
...     for row_num in range(1, ws.max_row):
...         product_name = ws.cell(row=row_num, column=2).value
...         if product_name in PRICE_UPDATES:
...             ws.cell(row=row_num, column=3).value = PRICE_UPDATES[product_name]
...     wb.save('fromPython_update.xlsx')
...     print('[+] Done\n[+] New file name: fromPython.xlsx')
... except Exception as e:
...     print('[+] Error: {}'.format(e))
```
