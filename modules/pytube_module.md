<link rel="stylesheet" href="style.css">

## Read It

- [Website](https://www.pythoncheatsheet.org)
- [Github](https://github.com/wilfredinni/python-cheatsheet)
- [PDF](https://github.com/wilfredinni/Python-cheatsheet/raw/master/python_cheat_sheet.pdf)

## Table of Content

- [Getting Started](#getting-started)
- [Command line usage](#command-line-usage)

***

- [Linux Main](file:///home/dabve/python/py_cheatsheet/markdown/main.md)
- [Windows Main](file:///D:/my_Folder/backups/python/py_cheatsheet/markdown/main.md)

## Documentation

- [pytube doc](https://python-pytube.readthedocs.io/en/latest/)

### Getting Started

- Installation

```bash
$ pip3 install pytube3
```
- usage

    ```python
    >>> from pytube import YouTube
    >>> from pprint import pprint

    >>> yt = YouTube("http://www.youtube.com/watch?v=Ik-RsDGPI5Y")
    ```

- Once set, you can see all the codec and quality options YouTube has made
- available for the particular video by printing videos.

    ```python
    >>> pprint(yt.get_videos())
    ```

- view the auto generated filename:

    ```python
    >>> pprint(yt.filename)
    ```

- set the filename:

    ```python
    >>> yt.set_filename('Dancing Scene from Pulp Fiction')
    ```

- You can also filter the criteria by filetype.ytprint(yt.filter('flv'))

    ```python
    >>> pprint(yt.filter('flv'))
    ```

- wanted the highest resolution available for a specific file type, you

    ```python
    >>> pprint(yt.filter('mp4')[-1])
    ```

- You can also get all videos for a given resolution

    ```python
    >>> pprint(yt.filter(resolution='480p'))
    ```

- To select a video by a specific resolution and filetype you can use the get method.
- NB: get() can only be used if and only if one object matches your criteria.

    ```python
    >>> video = yt.get('mp4', '720p')
    >>> video = yt.get('mp4')
    ```

- MultipleObjectsReturned: 2 videos met criteria.
- In this case, we'll need to specify both the codec (mp4) and resolution
- (either 360p or 720p).video

- Okay, let's download it! (a destination directory is required)

    ```python
    >>> video.download('/tmp/')
    ```

### Command line usage

- You can download a video by simply passing the -e (or --extension=) switch and setting it to the desired filetype:

    ```bash
    $ pytube -e mp4 http://www.youtube.com/watch?v=Ik-RsDGPI5Y
    ```

- Same thing for specifying a resolution:

    ```bash
    $ pytube -r 720p http://www.youtube.com/watch?v=Ik-RsDGPI5Y
    ```

- When run without a resolution or extension, it shows a list of available formats to download

    ```bash
    $ pytube http://www.youtube.com/watch?v=Ik-RsDGPI5Y
    ```

| Resolution |     Extension |
| :---------:|:-------------:|
| 0  3gp     |        144p
| 1  3gp     |        240p
| 2  mp4     |        360p
| 3  mp4     |        720p
| 4  webm    |        360p

Enter choice:

- You can see a list of available formats by passing the -s (or --show-available) flag

    ```bash
    $ pytube -s http://www.youtube.com/watch?v=Ik-RsDGPI5Y
    ```

- You can also specify a download file path (-p or --path=):

    ```bash
    $ pytube -e mp4 -p ~/Downloads/ http://www.youtube.com/watch?v=Ik-RsDGPI5Y
    ```

- and/or optionally choose the filename (-f or --filename=):

    ```bash
    $ pytube -e mp4 -f "Dancing Scene from Pulp Fiction" http://www.youtube.com/watch?v=Ik-RsDGPI5Y
    ```
