python << END
import os.path
from vim_bridge import bridged

@bridged
def is_cool(name):
    return name == 'Mr. Freeze'
END

echo IsCool("Mr. Freeze")
