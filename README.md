restricted-grep
===============

A restricted implementation of grep in Python.
Special characters:
* .   ==> Represents any character
* /   ==> Escapes any special meaning the following character may have
* *   ==> The previous character may appear 0 or more times.
All other characters have no special values.

Usage
-----
From the command line:
>>> python3 rgrep.py "input.txt" "pattern"

Where input.txt is a string representing the path to the .txt file you wish
to search, and pattern is the limited regex you wish to use.

License
-------
This code is for instructional purposes only. It's based on a homework assignment
from one of my classes, and as such will probably be taken down this summer to limit
cheating in the future.  The only restriction on this code is that it absolutely cannot
be used in any way to aid you on a programming assignment here.  Yes, I know this carries
almost no weight in the real world, so I'm appealing to your moral side.
