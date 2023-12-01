import platform
import os
import dir_ops as do

# Dir that contains the package
_Dir = do.Dir(os.path.abspath(__file__)).ascend()


KEY_MAPPING = {
    'Windows': {
        '\r': 'ENTER',  # all values need to be longer than one character to not confuse with an input
        '\t': 'TAB',
        '\x08': 'BACKSPACE'
    },
    'Linux': {
        '\n': 'ENTER',
        '\t': 'TAB',
        '\x7f': 'BACKSPACE',
        '\x1b': 'ESCAPE'
    },
    'Darwin': {
        '\n': 'ENTER',
        '\r': 'ENTER',
        '\t': 'TAB',
        '\x7f': 'BACKSPACE',
        '\x1b': 'ESCAPE'
    }
}

# First, see what kind of platform we are running on
PLATFORM_SYSTEM = platform.system()
if PLATFORM_SYSTEM == 'Darwin' or PLATFORM_SYSTEM == 'Linux':  # Linux and Mac behave the same
    import termios
    import tty

elif PLATFORM_SYSTEM == 'Windows':
    import msvcrt
