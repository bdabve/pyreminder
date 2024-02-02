+---------------------------------------------------------------------
|→ heapq.merge()
|---------------
|   >>> a = [1, 4, 7, 10]
|   >>> b = [2, 5, 6, 11]
|   >>> for c in heapq.merge(a, b):
|   ...     print(c, ', ', end='')
|   1, 2, 4, 5, 6, 7, 10, 11
|
|   >>> with open('file1', 'rt') as file1, open('file2', 'rt') as file2, open('file3', 'wt') as outf:
|   ...     for line in heapq.merge(file1, file2):
|   ...         outf.write(lne)
|____________________________________________________________________
