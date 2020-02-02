`eval` and `exec` can dynamically execute Python code, and `eval` just only execute expression but `exec` can execute statements.

## compile

Compile the source into a code or AST object. Code objects can be executed  by `exec` or `eval`.

**compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)**

- source: normal string or ...

- filename: which the code was read

- mode: 'eval' or 'exec' or 'single'

Comparing:

- exec(code_string) == exec(compile(code_string, '<string>', 'exec'))

- eval(code_string) == eval(compile(code_string, '<string>', 'eval'))

And for the performance:

~~~bash
In [1]: def foo():
   ...:     code = compile('a, b = 1, 2', '<string>', 'exec')
   ...:     exec(code, {})

In [2]: timeit foo()                                                            
6.61 µs ± 13.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [3]: def foo2(): 
   ...:     exec('a, b = 1, 2',{})
In [4]: timeit foo2()                                                           
6.45 µs ± 24.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
~~~

It takes nearly same amount of time.

And another way

~~~bash
In [1]: timeit compile('a, b = 1, 2', '<string>', 'exec')                      
6.36 µs ± 18.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [2]: code = compile('a, b = 1, 2', '<string>', 'exec')                      
In [3]: timeit exec(code, {})                                                  
226 ns ± 3.07 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
~~~

As we can see, the most of time is for compilation, little time is for execution. Basically, two cases both are equivalent.


## globals() and locals()

- globals():

> Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called). It will change as module's variables change and vice versa.

~~~bash
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> globals()['a'] = 1
>>> a
1
>>> b = 2
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 1, 'b': 2}
~~~

- locals()

> Update and return a dictionary representing the current local symbol table.Note that at the module level, locals() and globals() are the same dictionary.(The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter)

~~~bash
>>> def foo():
...     a = 1
...     print(locals())
... 
>>> a = 2
>>> foo()
{'a': 1}
~~~

Another way:

~~~bash
>>> def foo():
...     locals()['a'] = 1
...     print(a)
... 
>>> foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in foo
NameError: name 'a' is not defined
~~~

# eval

**eval(expression[, globals[, locals]])**

> The expression argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the globals and locals dictionaries as global and local namespace.The return value is the result of the evaluated expression.

# exec

**exec(object[, globals[, locals]])**

This function supports dynamic execution of Python code. If exec gets two separate objects as globals and locals, the code will be executed as if it were embedded in a class definition.

~~~bash
>>> code = """
... def foo():
...     a = 10
...     print(locals())
...     print(globals())
... foo()
... """
>>> exec(code, g, l)
{'a': 10}
{'a': 1, '__builtins__': {...}}
~~~

And: 

~~~bash
>>> g = {'a': 1}
>>> l = {'a': 2}
>>> code = """
... print(a)
... print(locals())
... print(globals())
... """
>>> exec(code, g, l)
2
{'a': 2}
{'a': 1, '__builtins__': {...}}
~~~

continuing:

~~~bash
>>> g = {'a': 1}
>>> l = {'a': 2}
>>> code = """
... a = 3
... print(locals())
... print(globals())
... """
>>> exec(code, g, l)
{'a': 3}
{'a': 1, '__builtins__': {...}}
~~~

Obviously, globals() dictionary will not change normally (if don't use `global` keyword). And as it says: as if it were embedded in a class.

### Referenced for more information

[Built-in Functions](https://docs.python.org/3/library/functions.html#exec)

[Be careful with exec and eval in Python](https://lucumr.pocoo.org/2011/2/1/exec-in-python/)

[https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile#](https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile#)
