=====================================
 vim_bridge - a Python-to-Vim bridge
=====================================

What is it?
-----------
vim_bridge_ is a Python-to-Vim bridge decorator that allows transparent calls
to Python functions in native Vim scripts.


Installation
------------
Simply install the vim_bridge_ Python package, using setuptools,
``easy_install``, or ``pip``.


.. _vim_bridge: http://pypi.python.org/pypi/vim_bridge/


Usage
-----
In a Vim script, decorate your Python functions as follows to expose them as
native Vim callables.  Both arguments and return values are casted so it should
be transparent::

    python << endpython
    from vim_bridge import bridged

    @bridged
    def SayHello(first, last):
        return "Hello, %s %s!" % (first, last)

    endpython

    " Now call directly into the Python function!
    echo SayHello("John", "Doe")
               " prints "Hello, John Doe!"


Supported
---------
The following data types have proven to work:

* Strings
* Integers
* Lists
* Exceptions


More examples
-------------
Passing in a list::

    python << endpython
    from vim_bridge import bridged

    @bridged
    def GetLongest(list):
        return max(map(lambda s: len(s), list))

    endpython

    echo GetLongest(['one', 'two', 'three', 'four'])
                " returns 5 (because "three" is 5 chars long)


Catching exceptions::

    python << endpython
    from vim_bridge import bridged

    @bridged
    def WillCauseException():
        raise Exception("Oops")

    endpython

    " This will throw an error to the user...
    echo WillCauseException()

    " But here's how you can catch that in Vim
    try
        echo WillCauseException()
    catch
        echo "Something went wrong. Aborting."
    finally
        echo "Cleaning up."
    endtry


Using Python stdlib functions to do work that would be more difficult using
pure Vim scripting::

    python << END
    import os.path
    from vim_bridge import bridged

    @bridged
    def NormalizePath(path):
        return os.path.realpath(path)
    END

    echo NormalizePath("/this/../or/./.././that/is/./a/.//very/../obscure/..//././long/./../path/name")
    echo NormalizePath("..")

