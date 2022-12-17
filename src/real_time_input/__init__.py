import dir_ops as do
import os
import platform

_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
_src_Dir = _Dir.ascend()                                  #src Dir that is one above
_repo_Dir = _src_Dir.ascend()                    
_cwd_Dir = do.Dir( do.get_cwd() )


key_mapping = {
  'Windows': {
    '\r': 'ENTER', #all values need to be longer than one character to not confuse with an input
    '\t': 'TAB',
    '\x08': 'BACKSPACE'
  },
  'Darwin': {
    '\n': 'ENTER',
    '\t': 'TAB',
    '\x7f': 'BACKSPACE',
    '\x1b': 'ESCAPE'
  }
}

# First, see what kind of platform we are running on
PLATFORM_SYSTEM = platform.system()
if PLATFORM_SYSTEM == 'Darwin' or PLATFORM_SYSTEM == 'Linux': # Linux and Mac behave the same
    platform_system = 'Darwin'
    import termios
    import tty

elif PLATFORM_SYSTEM == 'Windows':
    import msvcrt

PHONETIC_ALPHABET = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel',
    'india','juliett','kilo','lima','mike','november','oscar','papa','quebec','romeo',
    'sierra','tango','uniform','victor','whiskey','xray','yankee','zulu']


from .RealTimeInput import RealTimeInput
