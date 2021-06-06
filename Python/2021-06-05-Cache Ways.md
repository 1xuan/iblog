# How To Cache

## Simple Implementation

### Using decorator (closure)

> To use decorator to create a closure, assign result of callable to free variable as to cache

~~~python
def caching(func):
    _cache = _default = object()
    def wrapper(*args, **kwargs):
        if _cache is _default:
            _cache = func(*args, **kwargs)
        return _cache
    return wrapper


@caching
def foo():
    ...
~~~

### In class

> Save computed result in `_cache` attr of class

~~~python
class Foo:
    def __init__(self):
        self._cache = {}

    def __calculate(self):
        ...

    @property
    def spam(self):
        if 'spam' in self._cache:
            return self._cache['spam']

        self._cache['spam'] = self.__calculate()

        return self._cache['spam']

~~~

### Using Descriptor

> Use descriptor as decorator to change class method as a descritor attr, to create a instance attr which name is same as the methond name, because of `get descriptor` characteristic, the instance will access instance attr directly instead of discriptor when invoke it by dot 

~~~python
class lazy_property:
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, inst, class_):
        if inst is None:
            return self
        value = self.fget(inst)
        setattr(inst, self.fget.__name__, value)
        return value


class Foo:
    @lazy_property
    def calc(self):
        ...
~~~

### Using builtin function: lru_cache


~~~python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
~~~

**More info about LRU to reference:**

[Caching in Python Using the LRU Cache Strategy](https://realpython.com/lru-cache-python/)

[Python实现：详解LRU缓存淘汰算法](https://mp.weixin.qq.com/s/kB2kaeYaZliDfTxsZ4ONaA)

### Using third-party module

- [cachetools](https://github.com/tkem/cachetools)

~~~python
from cachetools import cached, LRUCache, TTLCache

@cached(cache={})
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
~~~

- [beaker](https://github.com/bbangert/beaker)

- [python-diskcache](https://github.com/grantjenks/python-diskcache)

