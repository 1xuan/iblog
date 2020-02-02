# argparse module usage

As official document said: "The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv".

## what does sys.argv do?

for instance:

~~~python
import sys

print(sys.argv)
~~~

~~~bash
$ python3 -m 1 2 3 4 5
['/home/yixuan/temp/py', '-m', '1', '2', '3', '4', '5']
~~~

