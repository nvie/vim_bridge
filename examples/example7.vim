python << END
import os.path
from vim_bridge import bridged

@bridged
def is_cool(name):
    return name == 'Mr. Freeze'

@bridged
def dont_return_anything():
    print "I'm a function without return value."
END

echo IsCool("Mr. Freeze")
echo DontReturnAnything()
