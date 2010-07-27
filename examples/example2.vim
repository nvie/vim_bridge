python << endpython
from vim_bridge import bridged

@bridged
def GetLongest(list):
    return max(map(lambda s: len(s), list))

endpython

echo GetLongest(['one', 'two', 'three', 'four'])
            " returns 5 (because "three" is 5 chars long)
