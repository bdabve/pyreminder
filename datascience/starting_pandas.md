```python
import pandas as pd
import sqlite3 as sqdb
import matplotlib.pyplot as plt

divider = ('-' * 50)
# getting started
# A Series is a one-dimensional array-like object containing an array of data (of anyNumPy data type)
# and an associated array of data labels, called its index.
obj = pd.Series([4, 7, -5, 3])
print(obj)
print('object.values:', obj.values)
obj_ = pd.Series([4, 7, -5, 3], index=['a', 'b', 'c', 'e'])
print(obj_)
```

### Esential Functionality

#### Reindexing

```python
obj = pd.Series([4.5, 7.2, 5, 3], index=['a', 'b', 'c', 'd'])
print(obj)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print(obj2)
print()
obj3 = pd.Series(['Blue', 'Purple', 'Yellow'], index=[0, 2, 4])
print(obj3)
obj3.reindex(range(6), method='ffill')
```

## Starting with pandas
- query : `df = pd.read_sql_query("SELECT * FROM table_name", conn) `
- csv file: `df = pd.read_csv(filename.csv)`
- csv file: `df = pd.read_csv(filename.csv, encoding='utf-8' )`
- tab separated file : `df = pd.read_csv(filename.txt, delimiter='\t')`
- excel file: `df = pd.read_excel(filename.xlsx)`

```python
# reading data from sqlite database
db_name = '/home/dabve/programming/python/project/gestion_stocks/etatsStocksPDR.sqlite'
conn = sqdb.connect(db_name)
query = 'SELECT designation, code, reference, qte, prixU, valeur FROM magasin_pdr'
df = pd.read_sql_query(query, conn)
# OR
# curs.execute(query)
# desc = [desc[0] for desc in curs.description]
# rows = curs.fetchall()
# df = pd.DataFrame.from_records(data=rows, columns=desc)
```

```python
print(df.head(10))                      # head or tail like in bash, take number of line as argument
print(divider)
print('Number of rows: {}'.format(len(df)))
print('Columns: {}'.format(df.columns))
print('Columns as a list: {}'.format(list(df.columns)))
print(divider)
print()
print('Get a specific columns: \n{}'.format(df.code))     # or df['code']
print()
print('Like limit in SQL: \n{}'.format(df['code'][:5]))
print()
print('Multiple Columns: \n{}'.format(df[{'designation', 'code', 'qte', 'prixU'}][:6]))
print()
```

### Making changes

```python
df['valeur'] = df['qte'] * df['prixU']
# work with indexes, the first part means all rows, and the second mean the 5, and 6 columns
# axis = 1: horizontaly, and 0 for verticaly
df['valeur'] = df.iloc[:, 5:7].sum(axis=1)

del df['valeur']                            # delete column 'valeur'
df = df.drop(columns=['valeur'])            # drop column
df = df.drop('valeur', axis=1)              # drop column
```

### Working with rows

```python
print(df.loc[0:3])          # loc: label based index
print()
print(df.iloc[1])           # positional argument
print()
print(df.iloc[1:5])
print()
print(df.iloc[2,1])         # get a specific row and columns, 2, 1 == second row, first one

# iterate through rows
print('\nIterate through all rows: \n')
for index, row in df.iterrows():
    # this will print a details for all records
    print('index: {}\n{}'.format(index, row))
    print(divider)
    if index == 5: break

# search where qte == 0
print('\nQuantité = 0')
print(df.loc[df['qte'] == 0][:10])
# Statistics
print(df.describe())
```

### Filtering Data

```python
print(df.loc[df['designation'] == 'Fusible'])
print()
print(df.loc[(df['designation'] == 'Fusible') & (df['code'] == 'GOP-009')])
print()
print(df.loc[(df['designation'] == 'Fusible') & (df['qte'] > 10)])
print(divider)
axe_desig = df.loc[(df['designation'] == 'AXE') & (df['qte'] >=3)]
print('[+] With original index\n', axe_desig)
axe_desig.reset_index(drop=True, inplace=True)
print(divider)
print('[+] Reseting index\n', axe_desig)
```

### Sorting and describing data

```python
import re
new_df = df[{'designation', 'code', 'qte', 'prixU'}]
print(new_df.sort_values(['code']))
print(divider)
code = new_df.loc[new_df['code'].str.contains('^-', flags=re.I, regex=True)]
# bhs_article = df.loc[df['code'].str.contains('BHS')]
print(code.sort_values(['code', 'qte']).head(15)) print(divider) print(code.sort_values(['code'], ascending=False).head(15))
```

```python
bhs_article = new_df.loc[df['code'].str.contains('BHS')]
print(bhs_article)
print(divider)
# ~ == not contain
# bhs_article = df.loc[ ~ df['code'].str.contains('BHS')]
search = df.loc[(df['code'].str.contains('BHS')) & (df['qte'] <= 3)]
print(search[{'designation', 'code', 'qte', 'prixU'}].sort_values(['qte']))
print(divider)
bhs_autop = new_df.loc[df['code'].str.contains('bhs|autop', flags=re.I, regex=True)]
print(bhs_autop.head(15))
print()
print(bhs_autop.tail(15))
print(divider)
moteur = new_df.loc[df['designation'].str.contains('^moteur', flags=re.I, regex=True)]
print(moteur[{'designation', 'code'}])

print('Somme des valeur BHS: {}'.format(df.loc[df['code'].str.contains('BHS')]['valeur'].sum()))
print('Somme Total des Articles: {}'.format(df['valeur'].sum()))
```

### Grouping

```python
grouped = bhs_article.groupby(bhs_article['qte'])
print('Article par quantité')
print(grouped.size())
print(divider)
```

### Save to file
```python
colnames = list(new_df.columns.values)
df_toSave = new_df[colnames[0:4]]                           # specify columns

df_toSave.to_csv('fileOut.csv')                             # write as csv file
df_toSave.to_csv('fileOut.csv', index=False)                # no index

df_toSave.to_excel('fileOut.xlsx', index=False)             # to excel
print('done creating your report')
```

