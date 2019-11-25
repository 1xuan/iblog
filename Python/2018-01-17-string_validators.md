---
layout: post
title: python下字符串验证方法
date: 2018-01-17 18:04
---
### str.isalnum()
检查是否字符串所有的字符都是字母数字(a-z, A-Z和0-9).

	>>> print ('ab123'.isalnum())
	True
	>>> print ('ab123#'.isalnum())
	False

### str.isalpha()
检查是否所有的字符都是字母(a-z和A-Z).

	>>> print ('abcD'.isalpha())
	True
	>>> print ('abcd1'.isalpha())
	False
	
### str.isdigit()
检查是否所有的字符都是数字(0-9).

	>>> print ('1234'.isdigit())
	True
	>>> print ('123edsd'.isdigit())
	False
	
### str.islower()
检查是否所有的字符都是小写字母(a-z).

	>>> print ('abcd123#'.islower())
	True
	>>> print ('Abcd123#'.islower())
	False

### str.isupper()

	>>> print ('ABCD123#'.isupper())
	True
	>>> print ('Abcd123#'.isupper())
	False
	
## 使用`any()`函数

any() Parameters

They `any()` method takes an iterable (list, string, dictionary etc.) in Python.	
Return Value from any()

The any method returns:

- `True` if at least one element of an iterable is true
- `False` if all elements are false or if an iterable is empty

**举个例子**
	
	>>>l = (0, 1, 2, 3, 4)
	>>> print(any(l))
	True
	>>>l = (0, False)
	>>>print(any(l))
	False
	>>>l = (0, False, 1)
	>>>print(any(l))
	True
	
我们可以使用下面的语句来判断是否存在字符属于某个类型:

	print(any(s.isalnum() for s in str))	
