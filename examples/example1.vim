python << endpython
from vim_bridge import bridged

@bridged
def SayHello(first, last):
    return "Hello, %s %s!" % (first, last)

endpython

" Now call directly into the Python function!
echo SayHello("John", "Doe")
            " prints "Hello, John Doe!"
