# Deque In Python

### Queue implementation using a list:

~~~Python
class Queue:
    def __init__(self, maxlen):
        self._data = [None] * maxlen
        self.maxlen = maxlen
        self._size = 0
        self._front = 0
        self._rear = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return not bool(self._size)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.maxlen
        self._size -= 1
        return value

    def enqueue(self, val):
        self._rear = (self._rear + 1) % self.maxlen
        self._data[self._rear] = val

        if self._rear == self._front:
            self._front = (self._front + 1) % self.maxlen

        if self._size < self.maxlen:
            self._size += 1


    def __str__(self):
        vals = []
        cur = self._front
        while cur != self._rear:
            vals.append(self._data[cur])
            cur = (cur + 1) % self.maxlen
        else:
            vals.append(self._data[self._rear])

        queue_string = ', '.join(str(c) for c in vals if c)

        return f"Queue[{queue_string}]"
~~~ 

### Using deque

The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.

~~~Python
>>> from collections import deque

>>> q = deque(maxlen=3)
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3], maxlen=3)
>>> q.append(4)
>>> q
deque([2, 3, 4], maxlen=3)
>>> q.append(5)
>>> q
deque([3, 4, 5], maxlen=3)
~~~

Adding or poppint items from either end of a queue has O(1) complexity. This is unlike list where inserting or removing items from the front of the list is O(N).

