NCTU e3 dump
============

> No worries about e3 shutdown

Download all course materials in your e3 by one click


Get the materials
=================

```
$ e3dump --username yourusername --password yourpassword
INFO     Start: 【107下】1xxx.......
INFO     Download finished: 1-ex....
INFO     Start: 【107下】1xxx.......
INFO     Download finished: 7-de....
INFO     Download finished: 4-ac....
.....
INFO     Done!
```


Install
=======

via pip

```
$ python -m pip install e3dump
```

via pipenv

```
$ pipenv install e3dump
```


Usage
=====

```
usage: e3dump [-h] --username USERNAME --password PASSWORD [--path PATH]

NCTU e3 dump

optional arguments:
  -h, --help           show this help message and exit
  --username USERNAME  NCTU e3 username
  --password PASSWORD  NCTU e3 password
  --path PATH          Dump to this path, default is current pwd
```