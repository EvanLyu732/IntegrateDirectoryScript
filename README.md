# IntegrateDirectoryScript
A python script for comparing the difference between different directory and integrate them.

### Background:

Let's say there are two directory and we called it **A** and **B**. Their Structure like this:

**A**:

```
A
├── sub1
│   └── Asub1.txt
├── sub2
└── sub3
```
**B**:
```
B
├── sub1
│   └── Bsub1.txt
├── sub2
│   └── Bsub2.txt
└── sub3
```

This script will give a result like this but with a new directory name:

```
C
├── sub1
│   ├── Asub1.txt
│   └── Bsub1.txt
├── sub2
│   └── Bsub2.txt
└── sub3
```


### Usage:
Basically, this script requires three variables. First directory, second directory and the newest directory

```bash
python3 IntegerScript.py --help

usage: IntegerScript.py [-h] firdir secdir newdir

positional arguments:
  firdir      first directory absolute root path
  secdir      second directory absolute root path
  newdir      new directory absolute root path

optional arguments:
  -h, --help  show this help message and exit

```

