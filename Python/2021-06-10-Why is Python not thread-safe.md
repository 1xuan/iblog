## prerequisite knowledge

- what is thread-safe?

[Thread safety by wikipedia](https://en.wikipedia.org/wiki/Thread_safety) says: Thread-safe code only manipulates shared data structures in a manner that ensures that all threads behave properly and fulfill their design specifications without unintended interaction. 

- what is GIL

GIL: The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter.

**more info**

[What Is the Python Global Interpreter Lock (GIL)?](https://realpython.com/python-gil/)

- working of Python Interpreter

Python doesn’t convert its code into machine code, something that hardware can understand. It actually converts it into something called byte code. So within python, compilation happens, but it’s just not into a machine language. It is into byte code (.pyc or .pyo) and this byte code can’t be understood by the CPU. So we need an interpreter called the python virtual machine to execute the byte codes. 

Python Code -> `Syntax Checker and Translator` -> Byte Code -> `Python Virtual Machine (PVM)` -> Output

**more info**

[Internal working of Python](https://www.geeksforgeeks.org/internal-working-of-python/)

### Why do we need to care about thread-safe even with GIL?

Python interpreter convert code to opcode, then execute opcode. Opcode execution is atomic because of GIL, so that single opcode is thread-safe. But only built-in data type execution is one single opecode.

~~~python
>>> lst = [3, 2, 1]
>>> 
>>> def foo():
...     lst.sort()
... 
>>> dis.dis(foo)
  2           0 LOAD_GLOBAL              0 (lst)
              2 LOAD_ATTR                1 (sort)
              4 CALL_FUNCTION            0
              6 POP_TOP
              8 LOAD_CONST               0 (None)
             10 RETURN_VALUE
~~~

Even though the line lst.sort() takes several steps, the sort call itself is a single bytecode `CALL_FUNCTION`.

Another example:

~~~python
>>> n = 0
>>>
>>> def foo():
        global n
        n += 1
>>> import dis
>>> dis.dis(foo)
LOAD_GLOBAL              0 (n)
LOAD_CONST               1 (1)
INPLACE_ADD
STORE_GLOBAL             0 (n)

# Even operator += is composited by two opcode `INPLACE_ADD` and `STORE_GLOBAL`

threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)
~~~

Usually this code prints 100, because each of the 100 threads has incremented n. But sometimes you see 99 or 98, if one of the threads' updates was overwritten by another. So, despite the GIL, you still need locks to protect shared mutable state.

**Conclution**: All that the GIL does is protect Python's internal interpreter state. It does not guarantee execution will be locked and protected in some processes like += operation or custom data structure operation.

**reference**

[Is the += operator thread-safe in Python?](https://stackoverflow.com/questions/1717393/is-the-operator-thread-safe-in-python)

**further reading**

- [Grok the GIL: How to write fast and thread-safe Python](https://opensource.com/article/17/4/grok-gil)

- [Gilectomy](https://lwn.net/Articles/689548/)

