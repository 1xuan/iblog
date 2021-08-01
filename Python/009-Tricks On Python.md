# Tricks On Python

## built-in type

### iterable object 

- filter with comprehension

~~~python
# list
$ lst = [1, 2, 3, 4, 5, 6]
$ even_lst = [i for i in lst if i%2 == 0]
[2, 4, 6]

# dict 
$ d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
$ even_d = {k: v for k, v in d.items() if v%2 == 0}
{'b': 2, 'c': 4}

# set
$ s = {1, 2, 3, 4, 5, 6}
$ even_s = {i for i in s if i%2 == 0}
{2, 4, 6}
~~~

- check if all items in collection are True

~~~python
$ s = [True, True, False]
$ all(s)
False
~~~

- check if any item in iterable-object is True

~~~python
$ s = [True, False, False]
$ any(s)
True
~~~

### list

- merge two list

~~~python
$ a = [1]
$ b = [2]
$ [*a, *b]
[1, 2]
~~~

### dict

- merge two dict

~~~python
$ a = {'a': 1}
$ b = {'b': 2}
$ {**a, **b}
{'a': 1, 'b': 2}
~~~

