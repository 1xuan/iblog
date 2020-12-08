# Regular Class

### create a class

method 1: normally

~~~python
class Foo:
    pass
~~~

method 2: use type

~~~python
>>> MyClass = type('MyClass', (MySuperClass, MyMixin), dict(x=42, foo=lambda self: 'have fun'))

# the code above is functionally equivalent to:
class MyClass(MySuperClass, MyMixin):
    x = 42
    
    def foo(self):
        return 'have fun'
~~~

## how to generate a instance?

The order: `construct` -> `initialize`.

If `__new__` is invoked during the object construction, and then `__init__` will be invoked immediately along with `self` passed. If `__new__()` does not return an instance of cls, then the new instance’s `__init__()` method will not be invoked. The `__new__` method can also return an instance of a different class, and when that happens, the interpreter does not call `__init__` . Actually, `__init__` is forbidden from returning anything, it's really an 'intializer'.

**For instance:**

~~~python
class Foo: 
    def __new__(cls): 
        # or object.__new__(cls)
        # res = super(Foo, cls).__new__(cls) 
        res = super().__new__(cls) 
        print(cls, res) 
        return res 
    def __init__(self): 
        print(self) 

>>> c = Foo()
<class '__main__.Foo'> <__main__.Foo object at 0x7fc3b42297f0>
<__main__.Foo object at 0x7fc3b42297f0>
~~~

And, to implement singleton:

~~~python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
~~~

**create a instance: `__new__`**

- object.\_\_new\_\_(cls[, ...])

cls.\_\_new\_\_() is a static method. The return value of \_\_new\_\_() should be the new object instance (usually an instance of cls).

**initialize a instance: `__init__`**

no non-`None` value may be returned by `__init__`.

## Scope and name

- variable named with prefix `__`

Python mangles these names and it is used to avoid name clashes with names defined by subclasses.

Interpreter will change name automatically by adding a prefix the class where they defined. And it will be stored into dict, using a new name. We should instead use new name if we wanna get it, and we still use original name if we just use it in method(such way, Interpreter will resolve it by itself).

~~~python
class A:
    def __init__(self, a):
        self.__a = a


class B(A):
    def __init__(self, a, b):
        self.__b = b
        self.__c__ = 3
        super().__init__(a)

    def get_a(self):
        print('self.__a:', self.__a)

    def get_b(self):
        print('self.__b:', self.__b)

a = A(1)
b = B(1, 2)

>>> a.__a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__a'
>>> a.__dict__	
{'_A__a': 1}
    
>>> b.__dict__
{'_B__b': 2, '__c__': 3, '_A__a': 1}
>>> b._B__b
2
>>> b.__c__
3
>>> b._A__a
1

>>> b.get_a()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "main.py", line 13, in get_a
    print('self.__a:', self.__a)
AttributeError: 'B' object has no attribute '_B__a'
>>> b.get_b()
self.__b: 2

~~~

## Special Method

- *\_\_dict\_\_*

The `__dict__` of an object is where its attributes are kept

First of all:

~~~python
class Foo:
    def __init__(self, name):
        self.name = name

>>> Foo.__dict__
mappingproxy({'__module__': '__main__', '__init__': <function Foo.__init__ at 0x7f79e9982c80>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None})
>>> f = Foo('guido')
>>> f.name
'guido'
>>> f.__dict__
{'name': 'guido'}
>>> f.__dict__['wow'] = 'wow'
>>> f.wow
'wow'
>>> f.__dict__
{'name': 'guido', 'wow': 'wow'}
~~~

So, instance's `__dict__` is just for their attrs, not including class's attrs. And if the same attrs occur in class namespace, instance is prior.

Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary.

- *\_\_init\_\_*

> To initialize instance

There is a triky for initialize many instance's attributes quickly:

~~~python
class Record:
    def __init__(self, **kwargs):                                               
        self.__dict__.update(kwargs)
~~~


#### Customizing attribute access

> Attribute access using either dot notation or the built-in functions `gettattr` , `hasattr` and `setattr` trigger the appropriate special methods listed here. 
>
> getting attrs order: `__getattribute__` -> `__dict__` -> `class attrs` -> `__getattr__`

- *\_\_getattr\_\_(self, name)*

- *\_\_setattr\_\_(self, name)*

- *\_\_getattribute\_\_(self, name)*

A simple instance:

~~~python
class C:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, key):
        return self.name
    def __getattribute__(self, val):
        print('through getattribute')
        return object.__getattribute__(self, val)

>>> c = C('guido')
>>> print(c.name)
through getattribute
guido
~~~

*For more info*

[3.3.2. Customizing attribute access](https://docs.python.org/3/reference/datamodel.html#customizing-attribute-access)

[Python 3 \_\_getattribute\_\_ vs dot access behaviour ](https://stackoverflow.com/questions/39043912/python-3-getattribute-vs-dot-access-behaviour)

### Descriptor

The implementation of ...

> descr.\_\_get\_\_(self, obj, type=None) -> value

- If instance of class invocate descriptor by dot notation, so, the obj is the instance, and the type parameter is type(instance).

- If class invocate descriptor, so the obj is the None, and the type is class.

> descr.\_\_set\_\_(self, obj, value) -> None

> descr.\_\_delete\_\_(self, obj) -> None

- data descriptor: object defines `__set__` or `__delete__`

- non-data descriptor: object defines `__get__`

> precedence: `data descriptor` > `instance's __dict__` > `non-data descriptor`

simple instance:
    
~~~python
class Desc:                                                                     
    def __get__(self, inst, class_):
        print(inst, class_)

    def __set__(self, inst, value):
        print(inst, value)

class C:
    d = Desc()
>>> c = C()
>>> c
<__main__.C object at 0x7f38b4467080>
>>> c.d
<__main__.C object at 0x7f38b4467080> <class '__main__.C'>
>>> C.d
None <class '__main__.C'>
>>> c.d = 1
<__main__.C object at 0x7f38b4467080> 1
>>> C.d = 1
>>> C.d
1
>>> c.d
1
~~~


**Property**

> building a `data descriptor` that triggers function calls upon access to an attribute

- property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

here some code:

~~~python

# Prevent assigning a negative value for price

class LineItem:                                                             
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

### another way

class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value                                           
        else:
            raise ValueError('value must be > 0')

    weight = property(get_weight, set_weight, doc='weight in kilograms')


### function could be also

# Writing and reading directly from instance __dict__

def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            # there use `setattr` will lead to infinite recursion
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)

class LineItem:                                                                 
    weight = quantity('weight')
    prince = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
~~~


> descr.\_\_set_name_\_\_(self, obj, value) -> None

​	It is used to set name for descriptor, and called within `type.__new__` after base class created in which descriptor is created.

~~~Python
class Desc:
    def __get__(self, inst, class_):
        print(inst, class_)
    def __set__(self, inst, value):
        print(inst, value)
    def __set_name__(self, owner, name):
        print(owner, name)

class Foo(Base):
    print('start')
    d = Desc()
    print('over')


# result:
start
over
<class '__main__.Foo'> d
~~~

*for more info*

[Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)

## subclass

> \_\_subclasses\_\_

​	*Function to return subclasses of class (note: just return first level subclasses)*

~~~python
class Foo(object): pass
class Bar(Foo): pass
class Baz(Foo): pass
class Bing(Bar): pass

>>> Foo.__subclasses__()
[<class '__main__.Bar'>, <class '__main__.Baz'>]
~~~

[How to find all the subclasses of a class given its name?](https://stackoverflow.com/questions/3862310/how-to-find-all-the-subclasses-of-a-class-given-its-name)

> \_\_init\_subclass\_\_

​	 *hook that initializes **all subclasses** of a given class.*

​	run order: `type.__new__` -> `__set_name__` -> `__init_subclass__`

~~~Python
# It could be used to register subclasses
class PluginBase:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
~~~

*for more info*

[PEP 487 -- Simpler customisation of class creation](https://www.python.org/dev/peps/pep-0487/)

[Understanding \_\_init_subclass\_\_](https://stackoverflow.com/questions/45400284/understanding-init-subclass#:~:text=__init_subclass__%20is%20just,attribute%20values%20on%20those%20subclasses.)

---

# Metaclass

What Metaclass is, in a nutshell, class of class.

~~~python
>>> class Metaclass(type):
...     pass
... 
>>> type(Metaclass)
<class 'type'>

>>> class MyClass(metaclass=Metaclass):
...     pass
... 
>>> type(MyClass)
<class '__main__.Metaclass'>
~~~

**For instance**

~~~python
class Metaclass(type): 
    def __new__(cls, name, bases, attrs): 
        print('Metaclass__new__') 
        res = super(Metaclass, cls).__new__(cls, name, bases, attrs) 
        print('Metaclass__new__', res, cls, name, bases, attrs) 
        return res 
    def __init__(cls, name, bases, attrs): 
        print('Metaclass__init__', cls, name, bases, attrs) 
        super(Metaclass, cls).__init__(name, bases, attrs) 
        print('Metaclass__init__') 
    def __call__(cls, *args, **kwargs): 
        print('Metaclass__call__') 
        res = super(Metaclass, cls).__call__(*args, **kwargs) 
        print('Metaclass__call__', res, cls, args, kwargs) 
        return res 
                                                                       

class Myclass(metaclass=Metaclass): 
    def __new__(cls, *args, **kw): 
        print('myclass__new__') 
        res = super(Myclass, cls).__new__(cls)  # object has no parameters 
        print('myclass__new__', res, cls, args, kw) 
        return res 
    def __init__(self, name): 
        print('myclass__init__', self) 
        self.name = name 
    def get_name(self): 
        return self.name 

# output
Metaclass__new__
Metaclass__new__ <class '__main__.Myclass'> <class '__main__.Metaclass'> Myclass () {'__module__': '__main__', '__qualname__': 'Myclass', '__new__': <function Myclass.__new__ at 0x7f34803db488>, '__init__': <function Myclass.__init__ at 0x7f34803dbea0>, 'get_name': <function Myclass.get_name at 0x7f34803db0d0>, '__classcell__': <cell at 0x7f34812e9b88: Metaclass object at 0x28add68>}
Metaclass__init__ <class '__main__.Myclass'> Myclass () {'__module__': '__main__', '__qualname__': 'Myclass', '__new__': <function Myclass.__new__ at 0x7f34803db488>, '__init__': <function Myclass.__init__ at 0x7f34803dbea0>, 'get_name': <function Myclass.get_name at 0x7f34803db0d0>, '__classcell__': <cell at 0x7f34812e9b88: Metaclass object at 0x28add68>}
Metaclass__init__

>>> c = Myclass('cool')                                                    
Metaclass__call__
myclass__new__
myclass__new__ <__main__.Myclass object at 0x7f34813672b0> <class '__main__.Myclass'> ('cool',) {}
myclass__init__ <__main__.Myclass object at 0x7f34813672b0>
Metaclass__call__ <__main__.Myclass object at 0x7f34813672b0> <class '__main__.Myclass'> ('cool',) {}

>>> c.name                                                                 
'cool'

>>> c.get_name()                                                           
'cool'
~~~

As we can see, the order is roughly: 

- when create a class which is the instance of metaclass 'Metaclass'

**`Metaclass's __new__` -> `Metaclass's __init__`**

- when create a instance which is the instance of class 'Myclass'

**`(begin)Metaclass's __call__` -> (`Myclass's __new__` -> `Myclass's __init__`) -> `Metaclass's __call__`(over)**

<u>There are some weird things, which I am not still clear about</u>

- In `Myclass`, the `__new__` which I redefine get all parameters (include 'cool' besides cls), and the `object` just take a parameter which is cls. (And more thing: the `Metaclass __call__` take the same parameters as `Myclass __new__`). Their relationship is complicated!

- How does the super() work exactly?

- ...

A small use of its functionality:

add a method for its 'instance'

~~~python
class Metaclass(type): 
    def __new__(cls, name, bases, attrs): 
        attrs['response'] = lambda self: "I am response" 
        return type.__new__(cls, name, bases, attrs)

>>> class myclass(metaclass=Metaclass): pass
>>> c = myclass()
>>> c.response()                                                           
'I am response'
~~~

*For more information*

[Understanding Python metaclasses](https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/)

[使用元类](https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072)

[Python official doc: Data model](https://docs.python.org/3/reference/datamodel.html#basic-customization)

\<\<Fluent Python\>\> -Luciano Ramalho

