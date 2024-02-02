# Getting started with pandas

## Load Data into pandas.

- query : `df = pd.read_sql_query("SELECT * FROM table_name", conn) `
- csv file: `df = pd.read_csv(filename.csv)`
- csv file: `df = pd.read_csv(filename.csv, encoding='utf-8' )`
- tab separated file : `df = pd.read_csv(filename.txt, delimiter='\t')`
- excel file: `df = pd.read_excel(filename.xlsx)`

  ```python
  df = pd.DataFrame.from_records(data=rows, columns=desc)
  print(df.head(10))                                 # head(number of line) and tail(number of line)
  print(len(df))                                     # number of rows
  ```

- Work With Columns
  ```python
  print(df.columns)                                   # columns name
  print(df.columns.values)                            # columns name
  print(df['code'].head(10))                          # or df.code
  print(df['code'][:5])                               # limit 5 rows
  print(df[{'code', 'designation', 'qte', 'prixU'}])  # multiple columns
  ```

- Rows

  ```python
  print(df.loc[0:3])                                  # label based indexing
  print(df.iloc[1])                                   # print the first row, iloc == positional indexing
  print(df.iloc[1:4])                                 # print multiple rows
  print(df.iloc[2, 1])                                # get a specific location

  for index, row in df.iterrows():
      # itterate though all row
      print(df[{'code', 'qte'}])

  print(df.loc[df['qte'] == 0])                       # search all where qte = 0, loc == label based indexing
  print(df[df['qte'] > 0])                       # search all where qte = 0, loc == location
  print(df.describe())                                # statistique like min, max
  ```

## Sorting and Describing Data

  ```python
  print(df.sort_values['code'])
  print(df.sort_values['code', 'qte'])
  print(df.sort_values['code'], ascending=False)
  print(df.sort_values['code', 'qte'], ascending=[1, 0])       # first ascending, and second false
  ```

## Making changes to the data

  ```python
  df['valeur'] = df['qte'] * df['prixU']
  df['valeur'].sum()
  df.goupby['qte'].sum()

  # work with indexes, the first part means all rows, and the second mean the 5, and 6 columns
  # axis = 1: horizontaly, and 0 for verticaly
  df['valeur'] = df.iloc[:, 5:7].sum(axis=1)

  del df['valeur']                            # delete column 'valeur'
  df = df.drop(columns=['valeur'])            # drop column
  df = df.drop('valeur', axis=1)            # drop column
  ```

## Save a copy to out file

  ```python
  colnames = list(df.columns.values)
  df_toSave = df[colnames[0:4]]
  df_toSave.to_csv('fileOut.csv')
  df_toSave.to_csv('fileOut.csv', index=False)                # no index

  df_toSave.to_excel('fileOut.csv', index=False)                # to excel
  ```

## Filtering data

**_&_** : AND
**_|_** : OR

  ```python
  df.loc[df['designation'] == 'AXE']
  df.loc[(df['designation'] == 'AXE') & (df['code'] == 'GOP-009')]
  df.loc[(df['designation'] == 'Fusible') & (df['qte'] > 10)]
  df.loc[(df['designation'] == 'AXE') & (df['qte'] >=3)]
  ```
