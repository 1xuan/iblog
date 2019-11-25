## coroutines

Coroutines is also a generator, both of them use yield. While parent program invoke child program, we can interrupt routine at where we want  by yield. It's more like multithreading, but it run in a threading. There is no overhead for thread switching, and it's no need thread lock.

There is a picture show you.

![coroutine](https://github.com/1xuan/1xuan.github.io/blob/master/_posts/images/run_coroutine.png)

A coroutine can be in one of four states. You can determine the current state using the inspect.getgeneratorstate(...) function, which returns one of these strings:

- 'GEN_CREATED'

- 'GEN_RUNNING'

- 'GEN_SUSPENDED'

- 'GEN_CLOSED'

**yield from**

when a generator gen calls yield from subgen() , the subgen takes over and will yield values to the caller of gen ; the caller will in effect drive subgen directly. Meanwhile gen will be blocked, waiting until subgen terminates. 

	>>> def gen():
	...		for c in 'AB':
	...			yield c
	...		for i in range(1, 3):
	...			yield i
	...
	>>> list(gen())
	['A', 'B', 1, 2]

Can be written as:

	>>> def gen():
	...		yield from 'AB'
	...		yield from range(1, 3)
	...
	>>> list(gen())
	['A', 'B', 1, 2]	
	
The code in Example is certainly not the most straightforward solution to the problem, but it serves to show yield from in action.
	
![caller_delegating_subgenerator](https://github.com/1xuan/1xuan.github.io/blob/master/_posts/images/caller_delegating_subgenerator.png)

Code as following:

	from collections import namedtuple

	Result = namedtuple('Result', 'count average')


	# the subgenerator
	def averager():
	    total = 0.0
	    count = 0
	    average = None
	    while True:
		term = yield   # although there yield None, you konw it will yield to caller straight.
		if term is None:
		    break
		total += term
		count += 1
		average = total/count
	    return Result(count, average)


	# the delegating generator
	def grouper(results, key):
	    # the results[key] is assigned by that value subgenerator returned
	    # there will not raise StopIteration while sugenerator closed
	    # the reason why use `while True` loop here is, that delegating genarator as
	    # a generator, if it closed, then generator raise a exception. Thus, when
	    # subgenerator closed, grouper() will run to `yield from` again, and create
	    # another averager instance, lastly, suspend.
	    # If the call raises StopIteration , the delegating generator is resumed
	    # So, we can also write code as following:
	    
	    # results[key] = yield from averager()
	    # yield
	    
	    while True:
		results[key] = yield from averager()   # The value of the yield from expression is the first argument to the StopItera tion exception raised by the subgenerator when it terminates.

	# the client code, a.k.a. the caller
	def main(data):
	    results = {}
	    for key, values in data.items():
		group = grouper(results, key)   # there produce a delegating generator
		next(group)   # prime subgenerator
		for value in values:
		    group.send(value)   # the value is sent into subgenerator
		group.send(None)   # terminate the subgenerator

	    report(results)


	def report(results):
	    for key, result in sorted(results.items()):
		group, unit = key.split(';')
		print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group, result.average, unit))


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
	
	main(data)

Every yield from chain must be driven by a client that calls next(...) or .send(...) on the outermost delegating generator.
	
**asyncio**

There is a asyncio routine:

	#!/usr/bin/env python3

	# spinner_asyncio.py

	# credits: Example by Luciano Ramalho inspired by
	# Michele Simionato's multiprocessing example in the python-list:
	# https://mail.python.org/pipermail/python-list/2009-February/538048.html

	# BEGIN SPINNER_ASYNCIO
	import asyncio
	import itertools
	import sys


	@asyncio.coroutine  # <1>
	def spin(msg):  # <2>
	    write, flush = sys.stdout.write, sys.stdout.flush
	    for char in itertools.cycle('|/-\\'):
		status = char + ' ' + msg
		write(status)
		flush()
		write('\x08' * len(status))
		try:
		    yield from asyncio.sleep(.1)  # <3>
		except asyncio.CancelledError:  # <4>
		    break
	    write(' ' * len(status) + '\x08' * len(status))


	@asyncio.coroutine
	def slow_function():  # <5>
	    # pretend waiting a long time for I/O
	    yield from asyncio.sleep(3)  # <6>
	    return 42


	@asyncio.coroutine
	def supervisor():  # <7>
	    spinner = asyncio.async(spin('thinking!'))  # <8>
	    print('spinner object:', spinner)  # <9>
	    result = yield from slow_function()  # <10>
	    spinner.cancel()  # For tasks, there is the Task.cancel() instance method, which raises CancelledError inside the coroutine.
	    return result


	def main():
	    loop = asyncio.get_event_loop()  # <12>
	    result = loop.run_until_complete(supervisor())  # <13>
	    loop.close()
	    print('Answer:', result)


	if __name__ == '__main__':
	    main()
	# END SPINNER_ASYNCIO
	
The use of the @asyncio.coroutine decorator is not mandatory, but highly recommended: it makes the coroutines stand out among regular functions, and helps with debugging by issuing a warning when a coroutine is garbage collected without being yielded from—which means some operation was left unfinished and is likely a bug. This is not a priming decorator.

A Task drives a coroutine, You don’t instantiate Task objects yourself, you get them by passing a coroutine to asyncio.async(...) or loop.create_task(...) .

When you get a Task object, it is already scheduled to run (e.g., by asyn cio.async );

*You can replace `asyncio.coroutine` and `yield from` by `asyncio` and `await` after python3.5*
	

	
	
	
