
Getting Started
```python
>>> import requests
>>> import bs4

# Downloading the web page
>>> res = requests.get('https://medium.com/@vonkunesnewton/generating-pdfs-with-reportlab-ced3b04aedef')
>>> res.raise_for_status()      # Get the status code

# Creating a BeautifulSoup object from html you can pass a local HTML file
>>> soup = bs4.BeautifulSoup(res.text, features='lxml')
>>> soup = bs4.BeautifulSoup(open('./jumia_categories.html'), features='lxml')

>>> print(soup.head)
>>> print(soup.title.text)
>>> first_link = soup.a                                   # get only the first tag by that name (a)
>>> print(first_link.name)
>>> print(first_link.string)
>>> print(first_link.attrs)                               # dict object
>>> print(first_link.attrs['href'])
>>> print(first_link.attrs['class'])

>>> links = soup.find_all('a')
>>> links = soup.find_all('a', limit=2)                   # limit work like in SQL Query

>>> for link in links:
...     try:
...         print('[+] href       : ', link.attrs['href'])
...         print('[+] class name : ', link.attrs['class'])
...         print('[+] link text  : ', link.text)
...         print('[+] Parent link: ', link.parent.name)
...         print('[+] Has a CLASS: ', 'class' in link)
...         print('[+] Has an ID  : ', 'id' in link)
...         print('-' * 30)
...     except KeyError:
...         # href is missing
...         pass

>>> links = soup.find_all('a', {'class': 'vent-link'})
>>> print('\nVENTE LINKS')
>>> for link in links:
>>>     print(link)
```
- find: looking for single result, usefull for searching by id
  ```python
  # if find cant find anything, returns None
  >>> link = soup.find('a', text='Zara')
  >>> print('[+] Zara Text in Links: ', link)
  ```

- The `select()` method take css selectors for the element you are looking for.
  ```python
  >>> soup_obj.select('div')
  >>> soup_obj.select('#author')        # by id
  >>> soup_obj.select('.notice')        # by class name
  >>> soup_obj.select('div span')       # css selectors
  >>> soup_obj.select('div > span')
  >>> soup_obj.select('input[name]')
  >>> soup_obj.select('input[type="button"]')
  ```
- Finding an element with the select() Method
  ```python
  >>> soup.select('div')        : All elements named `<div>`
  >>> soup.select('#author')    : The elements with an id attribute of author
  >>> soup.select('.notice')    : All elements that use a CSS class attri-bute named notice
  >>> soup.select('div span')   : All elements named `<span>` that are within an element named `<div>`
  >>> soup.select('div > span') : All elements named `<span>` that are directly within an element named `<div>`,
                                  with no other element in between
  >>> soup.select('input[name]'): All elements named `<input>` that have a name attribute with any value
  >>> soup.select('input[type="button"]'): All elements named `<input>` that have an attribute named type with value button
  
  >>> soup.select('p #author') # match any element that has an id attr of author, as long as it is also inside a <p> element.
  
  >>> elems = exampleSoup.select('#author')
  >>> type(elems)             <class 'list'>
  >>> len(elems)              1
  >>> type(elems[0])          <class 'bs4.element.Tag'>
  >>> elems[0].getText()      'Al Sweigart'
  >>> str(elems[0])           '<span id="author">Al Sweigart</span>'
  >>> elems[0].attrs          {'id': 'author'}
  ```
- The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML element.
- The list will contain one Tag object for every match in the BeautifulSoup object’s HTML.
- Tag values can be passed to the str() function to show the HTML tags they represent.
  ```python
  >>> pElems = exampleSoup.select('p')
  >>> str(pElems[0])  '<p>Download my <strong>Python</strong> book from <a href="http://inventwithpython.com">my website</a>.</p>'
  >>> pElems[0].getText() 'Download my Python book from my website.'
  >>> str(pElems[1])      '<p class="slogan">Learn Python the easy way!</p>'
  >>> pElems[1].getText() 'Learn Python the easy way!'
  >>> str(pElems[2])      '<p>By <span id="author">Al Sweigart</span></p>'
  >>> pElems[2].getText() 'By Al Sweigart'
  ```
