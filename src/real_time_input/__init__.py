import os
import platform

KEY_MAPPING = {
  'Windows': {
    '\r': 'ENTER', #all values need to be longer than one character to not confuse with an input
    '\t': 'TAB',
    '\x08': 'BACKSPACE'
  },
  'Linux': {
    '\n': 'ENTER',
    '\t': 'TAB',
    '\x7f': 'BACKSPACE',
    '\x1b': 'ESCAPE'
  }
}

# First, see what kind of platform we are running on
PLATFORM_SYSTEM = platform.system()
if PLATFORM_SYSTEM == 'Darwin' or PLATFORM_SYSTEM == 'Linux': # Linux and Mac behave the same
    PLATFORM_SYSTEM = 'Linux'
    import termios
    import tty

elif PLATFORM_SYSTEM == 'Windows':
    import msvcrt

PHONETIC_ALPHABET = ['alpha','bravo','charlie','delta','echo','foxtrot','golf','hotel',
    'india','juliett','kilo','lima','mike','november','oscar','papa','quebec','romeo',
    'sierra','tango','uniform','victor','whiskey','xray','yankee','zulu']


from .RealTimeInput import RealTimeInput
