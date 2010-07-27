python << END
import os.path
from vim_bridge import bridged

@bridged
def NormalizePath(path):
    return os.path.realpath(path)

@bridged
def RealPath(path):
    # It does not matter if you call NormalizePath from here...
    return NormalizePath(path)
END

" ...or from here
echo NormalizePath("/this/../or/./.././that/is/./a/.//very/../obscure/..//././long/./../path/name")
echo RealPath("..")
