## class inheriting

- dir()

~~~
>>> dir(object)
['__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']

>>> object.__dict__
mappingproxy({'__repr__': <slot wrapper '__repr__' of 'object' objects>, '__hash__': <slot wrapper '__hash__' of 'object' objects>, '__str__': <slot wrapper '__str__' of 'object' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'object' objects>, '__setattr__', ... })

>>> set(dir(object)) == set(object.__dict__.keys())
True

>>> class C: pass

>>> set(object.__dict__.keys()) - set(dir(C))
set()
>>> set(dir(C)) - set(object.__dict__.keys())
{'__dict__', '__module__', '__weakref__'}

~~~

As 'instance' has their `__dict__`, class has their own `__dict__` likewise, and there are just three exclusive attrs in plain class.



