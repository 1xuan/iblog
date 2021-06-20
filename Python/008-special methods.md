<sub>The following stuff is validated in CPython3.8</sub>


## Attributes

- \_\_name\_\_: the name of object

- \_\_dict\_\_: the namespace of object


## customization

- **\_\_new\_\_**

[object.\_\_new\_\_ from official doc ](https://docs.python.org/3.8/reference/datamodel.html#object.__new__)

*\_\_new\_\_ is static method*. Python use `__new__` to create an instance of class. When invokes class (like AClass()), Python will invoke `__new__` of class first, then return an instance.


example:

~~~python
class Foo:
    def __new__(cls, *args, **kwargs):
        print(f'call __new__ of {cls.__name__}')
        return super().__new__(cls, *args, **kwargs)

>>> inst = Foo()
call __new__ of Foo

"""
But there is a trap
Even we should use (*args, **kwargs) to capture variable number of arguments,
but be in top level of class, which inherits object implicitly or explicitly,
the super() of the class is object, calling super().__new__(cls, *args, **kwargs)
is equivalent to calling object.__new__(cls, *args, **kwargs).
however object.__new__ won't accept any parameter.
So we should pass only one single cls
It should be:

return super().__new__(cls)
or
return object.__new__(cls)

"""


# So this will raise error

>>> inst = Foo('a arg')
call __new__ of Foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "temp.py", line 4, in __new__
    return super().__new__(cls, *args, **kwargs)
TypeError: object() takes no parameters


# Just like this situation

>>> object.__new__(Foo, 'a arg')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object() takes no parameters
~~~

So we rewrite above example:

~~~python

# a plan
class Foo:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

# another plan
class Foo:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
~~~

As we can see, `*args` and `**kwargs` isn't used at all. But those arguments wil be passed to `__init__` exactly same way. We initialize instance in `__init__`.(even though we can initialize instance, but it is not advised. And if we rewrite).

For whether or not write like above case in subclass, the answer is it depends.

~~~python
"""
If super() class doesn't rewrite __new__, then super().__new__ is object.__new__.
"""

class Base: pass
                                                                                
class Foo(Base):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


>>> super(Foo, Foo).__new__
<built-in method __new__ of type object at 0x9d17a0>

>>> super(Foo, Foo).__new__ is object.__new__
True
~~~

- **\_\_init\_\_**

[object.\_\_init\_\_ from official doc](https://docs.python.org/3.8/reference/datamodel.html#object\.\_\_init\_\_)

`__init__` is called after `__new__` called. It is used to initialize instance.

~~~python
class Foo:
    def __init__(self, a):
        self.a = a
~~~

- **\_\_call\_\_**

> Called when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) roughly translates to type(x).\_\_call\_\_(x, arg1, ...). [from Python doc](https://docs.python.org/3.8/reference/datamodel.html#object.__call__)

example:

~~~python
class Foo:
    def __call__(self):
        return 'instance called'

>>> foo = Foo()
>>> foo()
'instance called'
~~~

- **\_\_del\_\_**

[object.\_\_del\_\_(self) in Python doc](https://docs.python.org/3.8/reference/datamodel.html#object.__del__)

example:

~~~python
class Foo:                                                                      
    def __del__(self):
        print(f"{self} destroyed")


>>> foo = Foo()
>>> del foo
<__main__.Foo object at 0x7fcaf4e390f0> destroyed
~~~

- **\_\_repr\_\_**

[object.\_\_repr\_\_(self)](https://docs.python.org/3.8/reference/datamodel.html#object.__repr__)

Called by the repr() built-in function to compute the “official” string representation of an object. **If a class defines __repr__() but not __str__(), then __repr__() is also used when an “informal” string representation of instances of that class is required.**

**This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.**

example:

~~~python
class Foo:
    def __repr__(self):
        return 'repr of Foo'

>>> foo = Foo()
>>> print(repr(foo))
repr of Foo
>>> print(foo)
repr of Foo
~~~

- **\_\_str\_\_**

[object.\_\_str\_\_(self)](https://docs.python.org/3.8/reference/datamodel.html#object.__str__):

> Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely printable string representation of an object. The return value must be a string object.

example:

~~~python
class Foo:
    def __str__(self):
        return 'str of Foo'

>>> foo = Foo()
>>> print(str(foo))
str of Foo
~~~

- **\_\_eq\_\_**

[object.\_\_eq\_\_(self, other)](https://docs.python.org/3.8/reference/datamodel.html#object.__eq__):

> By default, object implements \_\_eq\_\_() by using is, returning NotImplemented in the case of a false comparison: True if x is y else NotImplemented.

example:

~~~python
class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return type(other) is type(self) and self.val == other.val

>>> Foo(1) == Foo(1)
True
>>> Foo(1) == 1
False
>>> Foo(1) == Foo(2)
False
~~~

- **\_\_hash\_\_**

[object.\_\_hash\_\_(self)](https://docs.python.org/3.8/reference/datamodel.html#object.__hash__):

> Called by built-in function hash() and for operations on members of hashed collections including set, frozenset, and dict. \_\_hash\_\_() should return an integer. 

There are some rules for whether to define \_\_hash\_\_:

~~~
                                  |---> could def __hash__ if it's immutable
        |---> |def __eq__    |--->|
        |                         |---> shouldn't def __hash__ if it's mutable
None -> |
        |                         |--->
        |---> |not def __eq__|--->|    |---> shouldn't def __hash__ anyway
                                  |--->


The only function of __hash__ is to generate unique hash value for hash collections. If there is not __eq__, then it is different between any both objects(excludes same objects which are with same id).

Take set as an example, set uses hash value to compute address of slot, then store object in that slot. If add a new object, it will **compare the hash value and the key (by == comparison)** if slot is occupied. So, don't define __hash__ anyway if __eq__ not exists.
~~~

example:

~~~python
class Foo:
    def __init__(self, val: int):
        self.val = val

    def __eq__(self, other):
        return type(self) is type(other) and hash(self) == hash(other)
    
    def __hash__(self):
        return self.val


>>> foo_1 = Foo(1)
>>> foo_2 = Foo(2)
>>> hash(foo_1), hash(foo_2)
(1, 2)
>>> d = {}
>>> d[foo_1] = 1
>>> d
{<__main__.Foo object at 0x7f3c1f871208>: 1}
>>> d[foo_2] = 2
>>> d
{<__main__.Foo object at 0x7f3c1f871208>: 1, <__main__.Foo object at 0x7f3c1f871278>: 2}
>>> foo_1a = Foo(1)
>>> hash(foo_1a)
1
>>> foo_1a in d
True
>>> d[foo_1a] = '1a'
>>> d
{<__main__.Foo object at 0x7f3c1f871208>: '1a', <__main__.Foo object at 0x7f3c1f871278>: 2}
~~~



- **\_\_slots\_\_**

[object.\_\_slots\_\_](https://docs.python.org/3.8/reference/datamodel.html#object.__slots__):

> This class variable can be assigned a string, iterable, or sequence of strings with variable names used by instances. \_\_slots\_\_ reserves space for the declared variables and prevents the automatic creation of \_\_dict\_\_ and \_\_weakref\_\_ for each instance.

- **\_\_bool\_\_**

[object.\_\_bool\_\_(self)](https://docs.python.org/3.8/reference/datamodel.html#object.__bool__):

> Called to implement truth value testing and the built-in operation bool(); should return False or True. When this method is not defined, \_\_len\_\_() is called, if it is defined, and the object is considered true if its result is nonzero. If a class defines neither \_\_len\_\_() nor \_\_bool\_\_(), all its instances are considered true.

example:

~~~python
class Foo:
    def __bool__(self):
        return True
~~~

## customizing attribute access

- **\_\_getattr\_\_**

[object.\_\_getattr\_\_(self, name)](https://docs.python.org/3.8/reference/datamodel.html#object.__getattr__)

> **Note that if the attribute is found through the normal mechanism, \_\_getattr\_\_() is not called.** (This is an intentional asymmetry between \_\_getattr\_\_() and \_\_setattr\_\_().)

example:

~~~python
class Foo:
    def __init__(self, val):
        self.val = val
    def __getattr__(self, name):
        return f'getattr {name}'

>>> foo = Foo('a')
>>> foo.val
'a'
>>> foo.nothisattr
'getattr nothisattr'
~~~

- **\_\_getattribute\_\_**

[object.\_\_getattribute\_\_(self, name)](https://docs.python.org/3.8/reference/datamodel.html#object.__getattribute__)

> Called unconditionally to implement attribute accesses for instances of the class. If the class also defines \_\_getattr\_\_(), the latter will not be called unless \_\_getattribute\_\_() either calls it explicitly or raises an AttributeError.

example:

~~~python
class C:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, key):
        return self.name
    def __getattribute__(self, val):
        print(f'through getattribute {val}')
        return object.__getattribute__(self, val)

>>> c = C('guido')
>>> c.name
through getattribute name
'guido'
>>> c.another_name
through getattribute another_name
through getattribute name
'guido'
~~~

further reading:

[Python 3 \_\_getattribute\_\_ vs dot access behaviour ](https://stackoverflow.com/questions/39043912/python-3-getattribute-vs-dot-access-behaviour)

- **\_\_setattr\_\_**

[object.\_\_setattr\_\_(self, name, value)](https://docs.python.org/3.8/reference/datamodel.html#object.__setattr__)

> Called when an attribute assignment is attempted. This is called instead of the normal mechanism (i.e. store the value in the instance dictionary). name is the attribute name, value is the value to be assigned to it.

example:

~~~python
class Foo:
    def __setattr__(self, name, value):
        # self.__dict__[name] = value
        object.__setattr__(self, name, value)
~~~

- **\_\_delattr\_\_**

[object.\_\_delattr\_\_(self, name)](https://docs.python.org/3.8/reference/datamodel.html#object.__delattr__)

> Like \_\_setattr\_\_() but for attribute deletion instead of assignment. This should only be implemented if del obj.name is meaningful for the object.

example:

~~~python
class Foo:
    def __delattr__(self, name):
        print(f'delete attr {name}')
        object.__delattr__(self, name)

>>> foo = Foo()
>>> foo.a = 1
>>> del foo.a
delete attr a
~~~

### Descriptors

- [object.\_\_get\_\_](https://docs.python.org/3.8/reference/datamodel.html#object.__get__) -> value

- [object.\_\_set\_\_](https://docs.python.org/3.8/reference/datamodel.html#object.__set__) -> None

- [object.\_\_delete\_\_](https://docs.python.org/3.8/reference/datamodel.html#object.__delete__) -> None

- [object.\_\_set_name\_\_](https://docs.python.org/3.8/reference/datamodel.html#object.__set_name__) -> None

data descriptor: object defines `__set__` or `__delete__`

non-data descriptor: object defines `__get__`

precedence: `data descriptor` > `instance's __dict__` > `non-data descriptor`

example:

~~~python
class Descriptor(object):
   
    def __init__(self, name =''):
        self.name = name
   
    def __get__(self, obj, objtype):
        return "{}for{}".format(self.name, self.name)
   
    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")
           
class GFG(object):
    name = Descriptor()
     
>>> g = GFG()
>>> g.name = "Geeks"
>>> g.name
GeeksforGeeks
~~~

further reading:

[Descriptor HowTo Guide](https://docs.python.org/3.8/howto/descriptor.html)

## customizing class creation

...

## Emulating container types

- [object.\_\_len\_\_(self)](https://docs.python.org/3.8/reference/datamodel.html#object.__len__)

> Called to implement the built-in function len(). Should return the length of the object, an integer >= 0. Also, an object that doesn’t define a \_\_bool\_\_() method and whose \_\_len\_\_() method returns zero is considered to be false in a Boolean context.

example:

~~~python
class Foo:
    def __init__(self):
        self._lst = []
    def append(self, val):
        self._lst.append(val)
    def __len__(self):
        print('call __len__')
        return len(self._lst)

>>> foo = Foo()
>>> len(foo)
call __len__
0
>>> foo.append('a')
>>> len(foo)
call __len__
1
~~~

- [object.\_\_getitem\_\_(self, key)](https://docs.python.org/3.8/reference/datamodel.html#object.__getitem__)

> Called to implement evaluation of self[key]. For sequence types, **the accepted keys should be integers and slice objects (it may be a string in dict)**.

example:

~~~python
class Foo:
    def __init__(self):
        self._lst = ['a', 'b', 'c']
    def __getitem__(self, key):
        print(key)
        return self._lst[key]
        
>>> foo = Foo()
>>> foo[0]
0
'a'
>>> foo[1]
1
'b'
~~~

or 

~~~python
class Foo:
    def __init__(self):
        self._d = {'a': 1, 'b': 2, 'c': 3}
    def __getitem__(self, key):
        print(key)
        return self._d[key]

>>> foo = Foo()
>>> foo['a']
a
1
>>> foo['b']
b
2
~~~

- [object.\_\_setitem\_\_(self, key, name)](https://docs.python.org/3.8/reference/datamodel.html#object.__setitem__)

> Called to implement assignment to self[key]. 

example:

~~~python
class Foo:
    def __init__(self):
        self._lst = ['a', 'b', 'c']
    def __setitem__(self, key, value):
        print(key)
        self._lst[key] = value
        
>>> foo = Foo()
>>> foo._lst
['a', 'b', 'c']
>>> foo[0] = 'aa'
0
>>> foo._lst
['aa', 'b', 'c']
~~~

- [object.\_\_iter\_\_(self, key, name)](https://docs.python.org/3.8/reference/datamodel.html#object.__iter__)

> This method is called when an iterator is required for a container.

example:

~~~python
class Foo:
    def __init__(self):
        self._lst = [1, 2, 3]
    def __iter__(self):
        print('call __iter__')
        return iter(self._lst)

>>> foo = Foo()
>>> for i in foo:
...     print(i)
... 
call __iter__
1
2
3
~~~

- [object.\_\_contains\_\_(self, key, name)](https://docs.python.org/3.8/reference/datamodel.html#object.__contains__)

> Called to implement membership test operators. Should return true if item is in self, false otherwise.

~~~python
class Foo:
    def __contains__(self, item):
        print(item)
        return item in [1, 2, 3]

>>> foo = Foo()
>>> 1 in foo
1
True
>>> 4 in foo
4
False
~~~

## With Statement Context Managers

- [object.\_\_enter\_\_(self)](https://docs.python.org/3.8/reference/datamodel.html#object.__enter__)

- [object.\_\_exit\_\_(self, exc_type, exc_value, traceback)](https://docs.python.org/3.8/reference/datamodel.html#object.__exit__)

**refrence**

[Data Model](https://docs.python.org/3.8/reference/datamodel.html)

