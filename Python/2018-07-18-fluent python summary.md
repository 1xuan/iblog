## chpater 2 an arrary of sequences
	
在python3中list comprehension中有自己的作用域（python2中不行，并且是可以共用的。

	>>> x = 'ABC'
	>>> dummy = [ord(x) for x in x]
	>>> x
	'ABC'
	>>> dummy	
	[65, 66, 67]

两个循环

	In [95]: [(i, j) for i in [1, 2, 3] for j in [4, 5]]
	Out[95]: [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]

**Using * to grab excess items**

	>>> a, *body, c, d = range(5)
	>>> a, body, c, d
	(0, [1, 2], 3, 4)
	>>> *head, b, c, d = range(5)
	>>> head, b, c, d
	([0, 1], 2, 3, 4)

In the context of parallel assignment, the * prefix can be applied to exactly one variable, but it can appear in any position。

**Nested Tuple Unpacking**

	metro_areas = [
	('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
	('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
	('Mexico City', 'MX', 20.142, (19.433333, -99.133333))]

	for name, cc, pop, (latitude, longitude) in metro_areas:

**Named Tuples**

	>>> from collections import namedtuple
	>>> City = namedtuple('City', 'name country population coordinates')
	>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
	>>> tokyo
	City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
	139.691667))
	>>> tokyo.population
	36.933
	>>> tokyo.coordinates
	(35.689722, 139.691667)
	>>> tokyo[1]
	'JP'

**Building Lists of Lists**

A list with three lists of length 3 can represent a tic-tac-toe board
	
	>>> board = [['_'] * 3 for i in range(3)]
	>>> board
	[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
	>>> board[1][2] = 'X'
	>>> board
	[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
	
A list with three references to the same list is useless

	>>> weird_board = [['_'] * 3] * 3
	>>> weird_board
	[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
	>>> weird_board[1][2] = 'O'
	>>> weird_board
	[['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]

The outer list is made of three references to the same inner list. While it is
unchanged, all seems right.in essence, it behaves like this code:

	row = ['_'] * 3
	board = []
	for i in range(3):
		board.append(row)

**Augmented Assignment with Sequences**

	>>> l = [1, 2, 3]
	>>> id(l)
	4311953800
	>>> l *= 2
	>>> l
	[1, 2, 3, 1, 2, 3]
	>>> id(l)
	4311953800
	>>> t = (1, 2, 3)
	>>> id(t)
	4312681568
	>>> t *= 2
	>>> id(t)
	4301348296
	
这里如果列表同样改为`l = l * 2`那么`l`对象会改变；

**A += Assignment Puzzler**

The unexpected result: item t2 is changed and an exception is raised.the mutable sequence in tuple, the order of execution: first, list append a item, then assign himself to tuple in original place. Because of inmutability of tuple, so this circumstance occurs.

	>>> t = (1, 2, [30, 40])
	>>> t[2] += [50, 60]
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment
	>>> t
	(1, 2, [30, 40, 50, 60])	

**Arrays**

If the list will only contain numbers, an array.array is more efficient than a list, and additional methods for fast loading and saving such as .frombytes and .tofile .

	>>> from array import array
	>>> from random import random
	>>> floats = array('d', (random() for i in range(10**7)))
	>>> floats[-1]
	0.07802343889111107
	>>> fp = open('floats.bin', 'wb')
	>>> floats.tofile(fp)
	>>> fp.close()
	
## chapter 3  Dictionaries and Sets

**generic mapping types**

	>>> a = dict(one=1, two=2, three=3)
	>>> b = {'one': 1, 'two': 2, 'three': 3}
	>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
	>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
	>>> e = dict({'three': 3, 'one': 1, 'two': 2})
	>>> a == b == c == d == e
	True

**Set Theory**

In addition to guaranteeing uniqueness, the set types implement the essential set operations as infix operators, so, given two sets a and b , a | b returns their union, a & b computes the intersection, and a - b the difference.

	found = len(needles & haystack)

## chpater 5 First-Class Functions

**Higher-Order Functions**

A function that takes a function as argument or returns a function as the result is a higher-order function.

**User-Defined Callable Types**

Not only are Python functions real objects, but arbitrary Python objects may also bemade to behave like functions. Implementing a __call__ instance method is all it takes.

	import random
	class BingoCage:
		def __init__(self, items):
			self._items = list(items)
			random.shuffle(self._items)	
		def pick(self):
			try:
				return self._items.pop()
			except IndexError:
				raise LookupError('pick from empty BingoCage')
		def __call__(self):
			return self.pick()
			
operation result:

	>>> bingo = BingoCage(range(3))
	>>> bingo.pick()
	1
	>>> bingo()
	0
	>>> callable(bingo)
	True
	
**Function Introspection**

Function objects have many attributes beyond __doc__ . We can invoke dir function:

	>>> dir(factorial)
	['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',	'__format__', '__ge__', '__get__', '__getattribute__', '__globals__','__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__','__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

**From Positional to Keyword-Only Parameters**

	>>> def f(a, *, b):
	...		return a, b
	...
	>>> f(1, b=2)
	(1, 2)
	>>> f(1, 2 ,3, 4, 5, 6)
	TypeError: f() takes 1 positional argument but 6 were given
	>>> TypeError: f() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
	
By this, if you want to evaluate `b`, you must designate keyword.

**Retrieving Information About Parameters**

Within a function object, the __defaults__ attribute holds a tuple with the default values of positional and keyword arguments. The defaults for keyword-only arguments appear in __kwdefaults__ . The names of the arguments, however, are found within the __code__ attribute, which is a reference to a code object with many attributes of its own.

	def clip(text, max_len=80):
	    """Return text clipped at the last space before or after max_len
	    """
	    end = None
	    if len(text) > max_len:
		space_before = text.rfind(' ', 0, max_len)
		if space_before >= 0:
		    end = space_before
		else:
		    space_after = text.rfind(' ', max_len)
		if space_after >= 0:
		    end = space_after
	    if end is None: # no spaces were found
		end = len(text)
	    return text[:end].rstrip()


	print(clip.__defaults__)
	print(clip.__code__)
	print(clip.__code__.co_varnames)
	print(clip.__code__.co_argcount)
	
	print:
	(80,)
	<code object clip at 0x7f29fd686a50, file "/home/yixuan/PycharmProjects/TestProject/learn.py", line 1>
	('text', 'max_len', 'end', 'space_before', 'space_after')
	2

**Function Annotations**

Each argument in the function declaration may have an annotation expression preceded by : . If there is a default value, the annotation goes between the argument name and the = sign. To annotate the return value, add -> and another expression between the ) and the : at the tail of the function declaration. The expressions may be of any type. The most common types used in annotations are classes, like str or int , or strings.

	def clip(text:str, max_len:'int > 0'=80) -> str:
		"""Return text clipped at the last space before or after max_len
		"""
		end = None
		if len(text) > max_len:
		    space_before = text.rfind(' ', 0, max_len)
		if space_before >= 0:
		    end = space_before
		else:
		    space_after = text.rfind(' ', max_len)
		if space_after >= 0:
		    end = space_after
		if end is None: # no spaces were found
			end = len(text)
		return text[:end].rstrip()


	print(clip.__annotations__)
	
	# {'text': <class 'str'>, 'return': <class 'str'>, 'max_len': 'int > 0'}

## chapter 6 Design Patterns with First-Class Functions

利用函数作为第一类对象的特性，重构由抽象类书写的代码。

构建抽象类：

	class Promotion(ABC):
		# the Strategy: an abstract base class
		@abstractmethod
		def discount(self, order):
			"""Return discount as a positive dollar amount"""

子类实现方法

## chapter 7 Function Decorator and Closures

**When Python Executes Decorators**

A key feature of decorators is that they run right after the decorated function is defined. That is usually at import time

	registry = []
	def register(func):
	    print('running register(%s)' % func)
	    registry.append(func)
	    return func
	@register
	def f1():
	    print('running f1()')
	@register
	def f2():
	    print('running f2()')
	def f3():
	    print('running f3()')
	def main():
	    print('running main()')
	    print('registry ->', registry)
	    f1()
	    f2()
	    f3()
	if __name__ == '__main__':
	    main()

	print:
	running register(<function f1 at 0x7f2a0d154158>)
	running register(<function f2 at 0x7f2a0d1541e0>)
	running main()
	registry -> [<function f1 at 0x7f2a0d154158>, <function f2 at 0x7f2a0d1541e0>]
	running f1()
	running f2()
	running f3()

If code is imported as module(and not run as a script), the output is this:

	>>> import registration
	running register(<function f1 at 0x10063b1e0>)
	running register(<function f2 at 0x10063b268>)

The main point of Example is to emphasize that function decorators are executed as soon as the module is imported, but the decorated functions only run when they are explicitly invoked. This highlights the difference between what Pythonistas call import time and runtime.

**Closures**

	def make_averager():
		series = []
		def averager(new_value):
			series.append(new_value)
			total = sum(series)
			return total/len(series)
		return averager

or

	def make_averager():
        count = 0
        total = 0
        def averager(new_value):
            nonlocal count, total
            count += 1
            total += new_value
            return total / count
        return averager
	
我想如果闭包之中声明一个全局变量，它会不会成为自由变量呢？

if you don't define variables by nonlocal or something before operate it. For instance:

    def make_averager():
        count = 0
        total = 0
        def averager(new_value):
            count += 1
            total += new_value
            return total / count
        return averager

Then interpretor will raise a error `UnboundLocalError: local variable 'count' referenced before assignment`.

And if you assign same variable name in function of closure, then it will be as a local variable. You need use `nonlocal` to use variables in closure.

You can use keyword `globle` to operate globle variables.

**Stacked Decorators**

In other words, this:

	@d1
	@d2
	def f():
		print('f')
		
Is the same as:

	def f():
		print('f')
		f = d1(d2(f))


## Chapter 8 Object References, Mutability, and Recycling

**The Relative Immutability of Tuples**

	>>> t1 = (1, 2, [30, 40])
	>>> t2 = (1, 2, [30, 40])
	>>> t1 == t2
	True
	>>> id(t1[-1])
	4302515784
	>>> t1[-1].append(99)
	>>> t1
	(1, 2, [30, 40, 99])
	>>> id(t1[-1])
	4302515784
	>>> t1 == t2
	False

**Copies Are Shallow by Default**

The easiest way to copy a list (or most built-in mutable collections) is to use the built-in constructor for the type itself. For example:

	>>> l1 = [3, [55, 44], (7, 8, 9)]
	>>> l2 = list(l1)
	>>> l2
	[3, [55, 44], (7, 8, 9)]
	>>> l2 == l1
	True
	>>> l2 is l1
	False

However, using the constructor or [:] produces a shallow copy (i.e., the outermost container is duplicated, but the copy is filled with references to the same items held by the original container). This saves memory and causes no problems if all the items are immutable. But if there are mutable items, this may lead to unpleasant surprises.

	l1 = [3, [66, 55, 44], (7, 8, 9)]
	l2 = list(l1)
	#
	l1.append(100)
	#
	l1[1].remove(55)
	#
	print('l1:', l1)
	print('l2:', l2)
	l2[1] += [33, 22] #
	l2[2] += (10, 11) #
	print('l1:', l1)
	print('l2:', l2)

	# the output:
	l1: [3, [66, 44], (7, 8, 9), 100]
	l2: [3, [66, 44], (7, 8, 9)]
	l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
	l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]	

通过id()函数可以很清楚的理解这个问题：

	In [68]: l1 = [3, [55, 44], (7, 8, 9)]

	In [69]: l2 = list(l1)

	In [70]: l2
	Out[70]: [3, [55, 44], (7, 8, 9)]

	In [71]: id(l1)
	Out[71]: 140005821023048

	In [72]: id(l2)
	Out[72]: 140005849885832

	In [73]: id(l1[0])
	Out[73]: 10919488

	In [75]: id(l2[0])
	Out[75]: 10919488

	In [76]: id(l1[1])
	Out[76]: 140005838271560

	In [77]: id(l2[1])
	Out[77]: 140005838271560

**Deep and Shallow Copies of Arbitrary Objects**

	class Bus:
		def __init__(self, passengers=None):
			if passengers is None:
				self.passengers = []
			else:
				self.passengers = list(passengers)
				def pick(self, name):
				self.passengers.append(name)
		def drop(self, name):
			self.passengers.remove(name)

	>>> import copy
	>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
	>>> bus2 = copy.copy(bus1)
	>>> bus3 = copy.deepcopy(bus1)
	>>> id(bus1), id(bus2), id(bus3)
	(4301498296, 4301499416, 4301499752)
	>>> bus1.drop('Bill')
	>>> bus2.passengers
	['Alice', 'Claire', 'David']
	>>> id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
	(4302658568, 4302658568, 4302657800)
	>>> bus3.passengers
	['Alice', 'Bill', 'Claire', 'David']
	
另外：

	>>> a = [10, 20]
	>>> b = [a, 30]
	>>> a.append(b)
	>>> a
	[10, 20, [[...], 30]]
	>>> from copy import deepcopy
	>>> c = deepcopy(a)
	>>> c
	[10, 20, [[...], 30]]

**Function Parameters as References**

The only mode of parameter passing in Python is **call by sharing**.Call by sharing means that each formalparameter of the function gets a copy of each reference in the arguments. In other words,the parameters inside the function become aliases of the actual arguments.The result of this scheme is that a function may change any mutable object passed as aparameter, but it cannot change the identity of those objects

	>>> def f(a, b):
	...		a += b
	...		return a
	...
	>>> x = 1
	>>> y = 2
	>>> f(x, y)
	3
	>>> x, y
	(1, 2)
	>>> a = [1, 2]
	>>> b = [3, 4]
	>>> f(a, b)
	[1, 2, 3, 4]
	>>> a, b
	([1, 2, 3, 4], [3, 4])
	>>> t = (10, 20)
	>>> u = (30, 40)
	>>> f(t, u)
	(10, 20, 30, 40)
	>>> t, u
	((10, 20), (30, 40))

参数被作为共享调用，这里列表作为可变对象，在列表作为参数传入函数之后，函数对原列表对象进行了修改，故a发生了变化。

对于tuple来说，虽然同样运用了 a += b，但是作为不可变对象，被创建之后不能被改变（如果内部存在可变对象则可变），而是重新创建了一个对象。

	>>> a = (1, 2)
	>>> id(a)
	140005849897096
	>>> a += (3, 4)
	>>> a
	(1, 2, 3, 4)
	>>> id(a)
	140005820954008

**Mutable Types as Parameter Defaults: Bad Idea**

	def f(a=[]):
	    a.append(1)
	    return a

	print(f())
	print(f())

	printout:
	[1]
	[1, 1]	
	
利用可变对象作为参数默认值，由于函数是共享调用，所以其实是每次函数参数是接受对之前对象的传递，而不是创建一个空的列表对象，所以对象的改变对之后函数的调用是有影响的。

**Defensive Programming with Mutable Parameters**

his solution is more flexible: now the argument passed to the passengers parameter may be a tuple or any other iterable, like a set or even database results, because the list constructor accepts any iterable.

	def __init__(self, passengers=None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)

这种方式会重新创建一个相同的对象。

**Tricks Python Plays with Immutables**

I was surprised to learn that, for a tuple t , t[:] does not make a copy, but returns a reference to the same object. You also get a reference to the same tuple if you write tuple(t) .

	>>> t1 = (1, 2, 3)
	>>> t2 = tuple(t1)
	>>> t2 is t1
	True
	>>> t3 = t1[:]
	>>> t3 is t1
	True

## Chapter 9 A Pythonic Object

**Overriding Class Attributes**

	class Vector2d:
	    typecode = 'd'
	    def __init__(self, x, y):
			self.x = float(x)
			self.y = float(y)

这里定义了一个类属性`typecode`，如果实例没有typecode属性而调用这个属性时，会使用`typecode='d'`作为默认值，如果有同类属性相同名字的实例属性，那么会对属性进行检索，优先使用实例属性。同样继承的实例属性同样可以在子类中对其进行重写。

## chapter 10 Sequence Hacking, Hashing, and Slicing

**Vector Take #3: Dynamic Attribute Access**

“The __getattr__ method is invoked by the interpreter when attribute lookup fails. In simple terms, given the expression my_obj.x , Python checks if the my_obj instance has an attribute named x ; if not, the search goes to the class ( my_obj.__class__ ), and then up the inheritance graph. 2 If the x attribute is not found, then the __getattr__ method defined in the class of my_obj is called with self and the name of the attribute as a string.

	shortcut_names = 'xyzt'
	def __getattr__(self, name):
		cls = type(self)
		if len(name) == 1:
			pos = cls.shortcut_names.find(name)
			if 0 <= pos < len(self._components):
				return self._components[pos]
		msg = '{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls, name))
	
	# the printout:
	>>> v = Vector(range(10))
	>>> v.x
	0.0
	>>> v.y, v.z, v.t
	(1.0, 2.0, 3.0)

此处cls为实例的类型，`<class '__main__.Vector'>`， `cls.shortcut_names`是对类属性的调用，并且`cls`为`<class '__main__.Vector'>`，同样可以利用`类名.属性`的方式来调用，比如`Vector.shortcut_name`。

Inappropriate behavior: assigning to v.x raises no error, but introduces
an inconsistency。

	>>> v = Vector(range(5))
	>>> v
	Vector([0.0, 1.0, 2.0, 3.0, 4.0])
	>>> v.x #
	0.0
	>>> v.x = 10 #
	>>> v.x #
	10
	>>> v
	Vector([0.0, 1.0, 2.0, 3.0, 4.0])

The inconsistency in Example 10-9 was introduced because of the way __getattr__ works: Python only calls that method as a fall back, when the object does not have the named attribute. However, after we assign v.x = 10 , the v object now has an x attribute, so __getattr__ will no longer be called to retrieve v.x : the interpreter will just return the value 10 that is bound to v.x .

Recall that in the latest Vector2d examples from Chapter 9, trying to assign to the .x or .y instance attributes raised AttributeError . In Vector we want the same exception with any attempt at assigning to all single-letter lowercase attribute names, just to avoid confusion. To do that, we’ll implement __setattr__ as listed.

	def __setattr__(self, name, value):
		cls = type(self)
		if len(name) == 1:
		if name in cls.shortcut_names:
			error = 'readonly attribute {attr_name!r}'
		elif name.islower():
			error = "can't set attributes 'a' to 'z' in {cls_name!r}"
		else:
			error = ''
		if error:
			msg = error.format(cls_name=cls.__name__, attr_name=name)
			raise AttributeError(msg)
		super().__setattr__(name, value)

**tips**:

Even without supporting writing to the Vector components, here is an important takeaway from this example: very often when you implement __getattr__ you need to code __setattr__ as well, to avoid inconsistent behavior in your objects.

## CHAPTER 11 Interfaces: From Protocols to ABCs

**Monkey-Patching to Implement a Protocol at Runtime**

	import collections
	from random import shuffle


	Card = collections.namedtuple('Card', ['rank', 'suit'])
	class FrenchDeck:
		ranks = [str(n) for n in range(2, 11)] + list('JQKA')
		suits = 'spades diamonds clubs hearts'.split()
		def __init__(self):
			self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
		def __len__(self):
			return len(self._cards)
		def __getitem__(self, position):
			return self._cards[position]

the usage of shuffle:

	>>> from random import shuffle
	>>> l = list(range(10))
	>>> shuffle(l)
	>>> l
	[5, 2, 9, 7, 8, 3, 1, 4, 0, 6]

However, if we try to shuffle a FrenchDeck instance, we get an exception:

	>>> from random import shuffle
	>>> from frenchdeck import FrenchDeck
	>>> deck = FrenchDeck()
	>>> shuffle(deck)
	Traceback (most recent call last):
		File "<stdin>", line 1, in <module>
		File ".../python3.3/random.py", line 265, in shuffle
			x[i], x[j] = x[j], x[i]
	TypeError: 'FrenchDeck' object does not support item assignment

The error message is quite clear: “ 'FrenchDeck' object does not support item assignment.” The problem is that shuffle operates by swapping items inside the collection, and FrenchDeck only implements the immutable sequence protocol. Mutable sequences must also provide a __setitem__ method.

Because Python is dynamic, we can fix this at runtime, even at the interactive console.

	>>> def set_card(deck, position, card):
	...		deck._cards[position] = card
	...
	>>> FrenchDeck.__setitem__ = set_card
	>>> shuffle(deck)
	>>> deck[:5]

## chapter 12 Inheritance: For Good or For Worse

**Subclassing Built-In Types Is Tricky**

	>>> class DoppelDict(dict):
	...		def __setitem__(self, key, value):
	...			super().__setitem__(key, [value] * 2)
	...
	>>> dd = DoppelDict(one=1) #
	>>> dd
	{'one': 1}
	>>> dd['two'] = 2 #
	>>> dd
	{'one': 1, 'two': [2, 2]}
	>>> dd.update(three=3) #
	>>> dd
	{'three': 3, 'one': 1, 'two': [2, 2]}

	>>> class AnswerDict(dict):
	...		def __getitem__(self, key):
	...			return 42
	...
	>>> ad = AnswerDict(a='foo') #
	>>> ad['a'] 
	42
	>>> d = {}
	>>> d.update(ad) #
	>>> d['a'] 
	'foo'
	>>> d
	{'a': 'foo'}

If you subclass collections.UserDict instead of dict , the issues exposed in Examples are both fixed.

	>>> import collections
	>>>
	>>> class DoppelDict2(collections.UserDict):
	...		def __setitem__(self, key, value):
	...			super().__setitem__(key, [value] * 2)
	...
	>>> dd = DoppelDict2(one=1)
	>>> dd
	{'one': [1, 1]}
	>>> dd['two'] = 2
	>>> dd
	{'two': [2, 2], 'one': [1, 1]}
	>>> dd.update(three=3)
	>>> dd
	{'two': [2, 2], 'three': [3, 3], 'one': [1, 1]}
	>>>
	>>> class AnswerDict2(collections.UserDict):
	...		def __getitem__(self, key):
	...			return 42
	...
	>>> ad = AnswerDict2(a='foo')
	>>> ad['a']
	42
	>>> d = {}
	>>> d.update(ad)
	>>> d['a']
	42
	>>> d
	{'a': 42}

## chapter 14 Iterables, Iterators, and Generators

**Why Sequences Are Iterable: The iter Function**

Whenever the interpreter needs to iterate over an object x , it automatically calls iter(x) . The iter built-in function:

> 1. Checks whether the object implements __iter__ , and calls that to obtain an iterator.
> 2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates an iterator that attempts to fetch items in order, starting from index 0 (zero).
> 3. If that fails, Python raises TypeError , usually saying “C object is not iterable,” where C is the class of the target object.

**New Syntax in Python 3.3: yield from**

	>>> def chain(*iterables):
	...		for it in iterables:
	...			for i in it:
	...				yield i
	...
	>>> s = 'ABC'
	>>> t = tuple(range(3))
	>>> list(chain(s, t))
	['A', 'B', 'C', 0, 1, 2]

另一种：

	>>> def chain(*iterables):
	...		for i in iterables:
	...			yield from i
	...
	>>> list(chain(s, t))
	['A', 'B', 'C', 0, 1, 2]

## chapter 15 Context Managers and else Blocks

**Do This, Then That: else Blocks Beyond if**

This is no secret, but it is an underappreciated language feature: the else clause can be used not only in if statements but also in for , while , and try statements.

The semantics of for/else , while/else , and try/else are closely related, but very different from if/else .

for
> The else block will run only if and when the for loop runs to completion (i.e., not if the for is aborted with a break ).

while
> The else block will run only if and when the while loop exits because the condition became falsy (i.e., not when the while is aborted with a break ).

try
> The else block will only run if no exception is raised in the try block. The official docs also state: “Exceptions in the else clause are not handled by the preceding except clauses.”

**Context Managers and with Blocks**

	>>> with open('mirror.py') as fp: #
	...		src = fp.read(60) #
	...
	>>> len(src)
	60
	>>> fp #
	<_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
	>>> fp.closed, fp.encoding #
	(True, 'UTF-8')
	>>> fp.read(60) #
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: I/O operation on closed file.

## chapter 16 coroutines

**Basic Behavior of a Generator Used as a Coroutine**

That’s why the first activation of a coroutine is always done with next(my_coro) —you can also call my_coro.send(None) , and the effect is the same.

If you create a coroutine object and immediately try to send it a value that is not None , this is what happens:

	>>> my_coro = simple_coroutine()
	>>> my_coro.send(1729)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: can't send non-None value to a just-started generator

**Decorators for Coroutine Priming**

	from functools import wraps
	def coroutine(func):
		"""Decorator: primes `func` by advancing to first `yield`"""
		@wraps(func)
		def primer(*args,**kwargs):
			gen = func(*args,**kwargs)
			next(gen)
			return gen
		return primer

	@coroutine
	def averager():
		total = 0.0
		count = 0
		average = None
		while True:
			term = yield average
			total += term
			count += 1
			average = total/count


	coro_avg = averager()
	from inspect import getgeneratorstate
	print(getgeneratorstate(coro_avg))
	print(coro_avg.send(10))

You can’t do much with a coroutine without priming it: we must always remember to call next(my_coro) before my_coro.send(x) . To make coroutine usage more convenient, a priming decorator is sometimes used.

**Coroutine Termination and Exception Handling**

An unhandled exception within a coroutine propagates to the caller of the next or send that triggered it.

	>>> from coroaverager1 import averager
	>>> coro_avg = averager()
	>>> coro_avg.send(40)
	40.0
	>>> coro_avg.send(50)
	45.0
	>>> coro_avg.send('spam') #
	Traceback (most recent call last):
	...
	TypeError: unsupported operand type(s) for +=: 'float' and 'str'
	>>> coro_avg.send(60) #
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	StopIteration

**Using yield from**

The first thing the yield from x expression does with the x object is to call iter(x) to obtain an iterator from it. This means that x can be any iterable.

	>>> def gen():
	...		yield from 'AB'
	...		yield from range(1, 3)
	...
	>>> list(gen())
	['A', 'B', 1, 2]

by delegating generator:

	from collections import namedtuple
	Result = namedtuple('Result', 'count average')
	# the subgenerator
	def averager():
	    total = 0.0
	    count = 0
	    average = None
	    while True:
			term = yield
			if term is None:
			    break
			total += term
			count += 1
			average = total/count
			print(average)
	    return Result(count, average)
	# the delegating generator
	def grouper(results, key):
	    while True:
			results[key] = yield from averager()
	# the client code, a.k.a. the caller
	def main(data):
	    results = {}
	    for key, values in data.items():
			group = grouper(results, key)
			next(group)
			for value in values:
			    group.send(value)
			group.send(None) # important!
	    # print(results)
	    report(results)

	def report(results):
	    for key, result in sorted(results.items()):
			group, unit = key.split(';')
			print('{:2} {:5} averaging {:.2f}{}'.format(
			    result.count, group, result.average, unit))

	data = {
	'girls;kg':
	[40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
	'girls;m':
	[1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
	'boys;kg':
	[39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
	'boys;m':
	[1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
	}

	if __name__ == '__main__':
	    main(data)

==其中去掉代理生成器中的while True之后，send(None)运行时会抛出StopIteration的错误, 此处的错误是由于代理生成器运行结束之后产生的==

If the sent value is not None , the subgenerator’s send() method is called. If the call raises StopIteration , the delegating generator is resumed. Any other exception is propagated to the delegating generator.







































