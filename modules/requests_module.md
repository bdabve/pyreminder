### Getting Started

```python
>>> import requests
>>> res = requests.get('https://www.google.com')        # get a webpage
>>> try:
...     res.raise_for_status()
... except Exception as err:
...     print('There was a problem: {}'.format(err))        # There was a problem: 404 Client Error: Not Found
```

- Passing parameter in URLs

    ```python
    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.get('http://httpbin.org/get', params=payloas)  # https://httpbin.org/get?key2=value2&key1=value1

    >>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    >>> r = requests.get('http://httpbin.org/get', params=payloas)  # https://httpbin.org/get?key1=value1&key2=value2&key2=value3
    ```

- Read the content of the server's response

    ```python
    >>> r = requests.get(url)
    >>> r.url

    >>> r.text
    >>> r.encoding                      # 'utf-8'
    >>> r.encoding = 'ISO-8859-1'       # change the encoding
    >>> r.content                       # binary response content like pdf
    >>> r.json()                        # json response content

    >>> r.status_code                           # 200
    >>> r.status_code == requests.codes.ok      # True
    >>> r.history
    >>> r.cookies
    >>> request.get(url, timeout=0.001)     # set timeout
    ```

- custom headers

    ```python
    from fake_useragent import UserAgent        # fake_useragent
    user_agent = UserAgent()
    # available: (random | safari | ff | firefox | google | chrome | opera | msie | ie)
    # print(user_agent.opera)

    url = 'https://api.randomuser.me'
    format_ = 'json'
    nationality = 'es'
    payload = {'format': format_, 'nat': nationality}
    headers = {'user-agent': user_agent.random}             # custom header for request
    res = requests.get(url, headers=headers, params=payload)
    print(res.url)

    headers = {'Accept': 'application/json'}
    res = requests.get(url, headers=headers, auth=auth)

    # update existing key
    res.headers.update('Content-Type') = 'application/json'

    # set new one 
    res.headers['Accept'] = 'application/json'

    # cookies
    res.cookies
    ```

- save what is being streamed to a file

    ```python
    >>> r = requests.get('https://api.github.com/events', stream=True)  # get the row socket response from the server
    >>> whith open(filename, 'wb') as fd:
    ...    for chunk in r.iter_content(chunk_size=128):
    ...         fd.write(chunk)

    >>> res = requests.get(url)
    >>> res.raise_for_status()
    >>> with open('RomeoAndJuliet.txt', 'wb') as playfile:
    ...     for chunk in res.iter_content(100000):
    ...         playfile.write(chunk)
    ```

- Using API

    ```python
    from requests.auth import HTTPBasicAuth
    url = 'https://leakix.net/search?page={}&q={}&scope=leak'.format(1, 'db_host')
    auth = HTTPBasicAuth('apikey', 'cqHfIqcYJGFYJzCGWoTgLI5CN5ocR11GD3uCGe1TLmm4I3Ea')
    res = requests.get(url, headers={'Accept': 'application/json'}, auth=auth)
    print(res.headers)
    ```
- requests with Tor
- NOTE: Tor server must be running

    ```python
    session = requests.session()
    print(session.proxies)
    res = requests.get('https://httpbin.org/ip')
    print(res.text)

    session.proxies['http'] = 'socks5h://localhost:9050'
    session.proxies['https'] = 'socks5h://localhost:9050'
    res = requests.get('https://httpbin.org/ip')
    print(res.text)
    ```
