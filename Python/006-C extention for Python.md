## Accessing C code using ctypes

Run in a normal way:

~~~
>>> import sum
>>> sum.our_function([1, 2, 3, 4])
10
~~~

sum.c

~~~
int our_function(int num_numbers, int *numbers) {
    int sum = 0;                                                                
    for (int i = 0; i < num_numbers; i++) {
        sum += numbers[i];
    }
    return sum;
}
~~~

compile:

~~~
cc -fPIC -shared -o libsum.so sum.c
~~~

main.py

~~~
import ctypes

# Set correct path explicitly, regardless of absolute path or relative path
_sum = ctypes.CDLL('./libsum.so')

_sum.our_function.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_int))


def our_function(numbers):
    global _sum
    num_numbers = len(numbers)
    array_type = ctypes.c_int * num_numbers
    result = _sum.our_function(ctypes.c_int(num_numbers), array_type(*numbers))

    return int(result)
~~~

## A simple C extension module

print "Hello World"

~~~
>>> import myModule
>>> myModule.helloworld()
Hello World
~~~


Three steps:

mymodule.c

~~~
#include <Python.h>

static PyObject* helloworld(PyObject* self, PyObject* args)
{
    printf("Hello World\n");
    return Py_None;
}

static PyMethodDef myMethods[] = {
    { "helloworld", helloworld, METH_NOARGS, "Prints Hello World" },
    { NULL, NULL, 0, NULL }
};

static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "myModule",
    "Test Module",
    -1,
    myMethods
};

PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}
~~~

setup.py
~~~
from distutils.core import setup, Extension

setup(
    name='myModule',
    version='1.0',
    ext_modules=[Extension('myModule', ['mymodule.c'])]
)
~~~

compile:

~~~
$ python setup.py build
$ sudo python3 setup.py install
~~~

## Using Cython

run:

~~~
>>> import run_cython
>>> main.text(10)
3628800
~~~

install cython

~~~
pip install cython
~~~

run_cython.pyx

~~~
cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x+1):
        y *= i
    return y
~~~

setup.py

~~~
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('run_cython.pyx'))
~~~

compilation

~~~
python setup.py build_ext --inplace
~~~


## Reference

[Creating Basic Python C Extensions - Tutorial](https://tutorialedge.net/python/python-c-extensions-tutorial/)

[Using C from Python: How to create a ctypes wrapper](https://pgi-jcns.fz-juelich.de/portal/pages/using-c-from-python.html)

[Calling C functions from Python - part 1 - using ctypes](http://yizhang82.dev/python-interop-ctypes)

[Use Cython to get more than 30X speedup on your Python code](https://towardsdatascience.com/use-cython-to-get-more-than-30x-speedup-on-your-python-code-f6cb337919b6)

