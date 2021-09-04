## read from stdin

- input

~~~python
>>> text = input()
yes
>>> text
'yes'
~~~

- readlines, (read, readline, ...)

~~~python
>>> import sys
>>> lines = sys.stdin.readlines()
yes
no
>>> lines
['yes\n', 'no\n']
~~~

But all the ways above, we must get input stream, the program will block forever otherwise. So We need to be aware of whether there is input stream when we use pipeline selectively.

So use following approachs

- select

~~~python
# main.py

import sys                                                                      
import select

if select.select([sys.stdin,],[],[],0.0)[0]:
    print("Have data!")
else:
    print("No data")
~~~

~~~bash
$ python main.py
No data
$ echo '' | python main.py
Have data!
~~~

- sys.stdin.isatty

~~~python
# main.py

import sys

if not sys.stdin.isatty():
    print("not sys.stdin.isatty")
else:                                                                           
    print("is  sys.stdin.isatty")
~~~

~~~bash
$ python main.py
is  sys.stdin.isatty
$ echo '' | python main.py
not sys.stdin.isatty
~~~

`sys.stdin.isatty` will judge whether this is an 'interactive' stream. Return False if it isn't else True.

