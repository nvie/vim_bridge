python << eop
import os
import vim
from vim_bridge import bridged

@bridged
def public():
    return "I am public."

@bridged
def _private():
    return "I am private (available in the current script only)."

@bridged
def my_name_is_auto_converted():
    return "In Python, I'm called my_name_is_auto_converted, but in Vim, I'm called MyNameIsAutoConverted :)"

@bridged
def _long_private_name():
    return "I'm private, and my case is converted automatically."
eop

echo Public()
echo s:Private()
echo MyNameIsAutoConverted()
echo s:LongPrivateName()
