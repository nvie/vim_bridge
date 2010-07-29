# Mock of the vim module, for testing outside of vim
from mock import Mock

my_mock = Mock()

def eval(s): return my_mock().eval(s)
def command(s): return my_mock().command(s)
