python << END
import os.path
from vim_bridge import bridged

@bridged
def NormalizePath(path):
    return os.path.realpath(path)
END

echo NormalizePath("/this/../or/./.././that/is/./a/.//very/../obscure/..//././long/./../path/name")
echo NormalizePath("..")
