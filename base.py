import pysvn
import platform

if platform.system() == 'Windows':
    Red = 4
    Yellow = 14
    Green = 2|8
    Blue = 1|8
    White = 15
    Reset = 0
else:
    Red = "\033[00;31m"
    Yellow = "\033[00;33m"
    Green = "\033[01;32m"
    Blue = "\033[01;34m"
    White = "\033[01;37m"
    Reverse = "\033[07m"
    Reset = "\033[0m"

def color_str(color, str):
	return color + str + base.Reset

class SVNBase:
    def __init__(self):
        self.client = pysvn.Client()

    def execute(self):
        pass

    def printc(self, color, text):
        print color, text, Reset

from url import *
from info import *
from status import *
from diff import *

def factory(argv):
    command = argv[0]
    return eval(command)(argv[1:])
