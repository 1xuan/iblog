# Python Import System

The Order:

`sys.modules` --> `sys.meta_path` --> `sys.path` --> `sys.path_importer_cache` --> `sys.path_hooks`

- `sys.meta_path`: return spec

- `sys.path`: iterate over sys.path, each one proccessed by path\_hooks

- `sys.path_importer_cache`: finder cached for each directory

- `sys.path_hooks`: hooks for every path, return a spec eventually


### A simple example:

~~~
from importlib.abc import Loader, MetaPathFinder
from importlib.util import spec_from_file_location

class MyMetaPathFinder(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        modname = AIM_MODULE_NAME
        location = YOUR_INIT_FILE_PATH

        if fullname == modname:
            return spec_from_file_location(
                name=AIM_MODULE_NAME,
                location=YOUR_INIT_PATH,
                loader=MyLoader(),
                submodule_search_locations=[YOUR_PKG_PATH]
            )
        else:
            return None


class MyLoader(Loader):
    def exec_module(self, module):
        with open(module.__file__) as f:
            data = f.read()
        exec(data, module.__dict__)
~~~


# Reference

[Import System](https://docs.python.org/3/reference/import.html)

[Python: Import Anything](https://www.usenix.org/system/files/login/articles/09beazley_061-068_online.pdf)

[David Beazley - Modules and Packages: Live and Let Die! - PyCon 2015](https://www.youtube.com/watch?v=0oTh1CXRaQ0)

[How python's import machinery works](https://manikos.github.io/how-pythons-import-machinery-works)

[How to implement an import hook that can modify the source code on the fly using importlib?](https://stackoverflow.com/questions/43571737/how-to-implement-an-import-hook-that-can-modify-the-source-code-on-the-fly-using)

[Import almost anything in Python: an intro to module loaders and finders](https://blog.quiltdata.com/import-almost-anything-in-python-an-intro-to-module-loaders-and-finders-f5e7b15cda47)
