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
