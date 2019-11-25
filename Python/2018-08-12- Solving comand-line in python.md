A instance:
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

Run it at command-line and provide useful help messages:

    $ python prog.py -h
    usage: prog.py [-h] [--sum] N [N ...]

    Process some integers.

    positional arguments:
     N           an integer for the accumulator

    optional arguments:
     -h, --help  show this help message and exit
     --sum       sum the integers (default: find the max)
     
    $ python prog.py 1 2 3 4
    4

    $ python prog.py 1 2 3 4 --sum
    10

---

We can define a instance `parser` by `argparse.ArgumentParser`.

    parser = argparse.ArgumentParser(description='Process some integers.')
    
`description` is keyword that be used to present some description of usage string.

    >>> parser = argparse.ArgumentParser(description='A foo that bars')
    >>> parser.print_help()
    usage: argparse.py [-h]

    A foo that bars

    optional arguments:
     -h, --help  show this help message and exit
    
*And more information refer to* [ArgumentParser objects](https://docs.python.org/3/library/argparse.html#argumentparser-objects)

The `parse_args()` method supports several ways of specifying the value fo an option, if it's none that denote the arguments from user input.

    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> parser.add_argument('-x')
    >>> parser.add_argument('--foo')
    >>> parser.parse_args(['-x', 'X'])
    Namespace(foo=None, x='X')
    >>> parser.parse_args(['--foo', 'FOO'])
    Namespace(foo='FOO', x=None)

*More information refer to* [The parse_args() method](https://docs.python.org/3/library/argparse.html#the-parse-args-method)

## The add_argument() method

the method have some keywords:

> - `name or flags` - Either a name or a list of option strings, e.g.`foo` or `-f`, --`foo`
> - `action` - The basic type of action to be taken when this argument is encountered at the command line
> - `nargs` - the number of command-line arguments that should be consumed
> - `const` - A constant value required by some action and nargs selections
> - `default` - The value produced if the argument is absent from command line
> - `type` - the type to which the command-line argument should be converted.
> - `help` - A brief description of what the argument does
> - `metavar` - A name for the argument in usage messages
> - `dest` - The name of the attribute to be added to the object returned by parse_args

**name or flags**

the `add_argument` method must know whether an optional argument, like `-f` or `--foo`, a positional argument, like a list of filenames.

for example,  an optional argument could be created like:

    >>> parser.add_argument('-f', '--foo')
    
while a positional argument could be created like:

    >>> parser.add_argument('bar')
    
Optional arguments will be identified by the `-` prefix.

    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> parser.add_argument('-f', '--foo')
    >>> parser.add_argument('bar')
    >>> parser.parse_args(['BAR'])
    Namespace(bar='BAR', foo=None)
    >>> parser.parse_args(['BAR', '--foo', 'FOO'])
    Namespace(bar='BAR', foo='FOO')
    >>> parser.parse_args(['--foo', 'FOO'])
    usage: PROG [-h] [-f FOO] bar
    PROG: error: the following arguments are required: bar

**action**

the `action` keyword argument specifies how the command-line arguments should  be handled. And if  --foo is present then foo=42, 

Some instance:

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo', action='store_const', const=42)
    >>> parser.parse_args(['--foo'])
    Namespace(foo=42)
    
`store_true` and `store_false` - these are special cases of `store_const`, they storing the values `True` and `False` respectively. For example:

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo', action='store_true')
    >>> parser.add_argument('--bar', action='store_false')
    >>> parser.add_argument('--baz', action='store_false')
    >>> parser.parse_args('--foo --bar'.split())
    Namespace(foo=True, bar=False, baz=True)
    
*more information refer to* [action](https://docs.python.org/3/library/argparse.html#action)

**nargs**

The keyword argument associates a defferent number of command-line arguments with a single action.

- `N`.n arguments from the command line will be gathered together into a list.

        >>> parser = argparse.ArgumentParser()
        >>> parser.add_argument('--foo', nargs=2)
        >>> parser.add_argument('bar', nargs=1)
        >>> parser.parse_args('c --foo a b'.split())
        Namespace(bar=['c'], foo=['a', 'b'])
    
- `?`.If no command-line argument is present, the value from default will be produced.Note that for optional arguments, there is an additional case - the option string is present but not followed by a command-line argument.In this case the value from const will be produced.

    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', nargs='?', const='c', default='d')
    parser.add_argument('bar', nargs='?', default='d')
    parser.parse_args(['XX', '--foo', 'YY'])

    parser.parse_args(['XX', '--foo'])

    parser.parse_args([])

- `*`.All command-line arguments present are gathered into a list.

        >>> parser = argparse.ArgumentParser()
        >>> parser.add_argument('--foo', nargs='*')
        >>> parser.add_argument('--bar', nargs='*')
        >>> parser.add_argument('baz', nargs='*')
        >>> parser.parse_args('a b --foo x y --bar 1 2'.split())
        Namespace(bar=['1', '2'], baz=['a', 'b'], foo=['x', 'y'])

**const**
 the
the `const` argument of add_argument() is used to hold constant values that are not read from the command line but are required for the various ArgumentParser actions. The two most common users of it are:

> - when add_argument() is called with `action=store_const`
> - When add_argument() is called with option strings (like -f or --foo) and nargs='?'.

**default**

Specifies what value should be used if the command-line argument is not present. For optional arguments, the `default` value is used when the option string was not present at the command line

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--length', default='10', type=int)
    >>> parser.add_argument('--width', default=10.5, type=int)
    >>> parser.parse_args()
    Namespace(length=10, width=10.5)
    
*more information refer to* [default](https://docs.python.org/3/library/argparse.html#default)

**type**

By default, ArgumentParser objects read command-line arguments as simple string. However, quite often the command-line string should instead be interpreted as another type.

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('foo', type=int)
    >>> parser.add_argument('bar', type=open)
    >>> parser.parse_args('2 temp.txt'.split())
    Namespace(bar=<_io.TextIOWrapper name='temp.txt' encoding='UTF-8'>, foo=2)
    
**meravar**

    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> parser.add_argument('-x', nargs=2)
    >>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
    >>> parser.print_help()
    usage: PROG [-h] [-x X X] [--foo bar baz]

    optional arguments:
     -h, --help     show this help message and exit
     -x X X
     --foo bar baz
     
**dest**

Most ArgumentParser actions add some value as an attribute of the objects returned by parse_args(). The name of this attribute is determined by `dest` keyword argument of add_argument(). For positional argument actions, `dest` is normally supplied as the first argument.

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('bar')
    >>> parser.parse_args(['XXX'])
    Namespace(bar='XXX')
    
`dest` allows a custom attribute name to be provided:

    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo', dest='bar')
    >>> parser.parse_args('--foo XXX'.split())
    Namespace(bar='XXX')
    

