import pysvn
import platform
import os
import sys

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

    def write(self, string):
        if os.isatty(sys.stdout.fileno()):
            for line in string.split("\n"):
                print self.format_line(line)
        else:
            print string

    def printc(self, color, text):
        print color, text, Reset

from url import *
from info import *
from status import *
from diff import *

def factory(argv):
	command = argv[0]
	try:
		return eval(command)(argv[1:])
	except NameError, e:
		print e
		print "Unknown command: '%s'" % (command)
		print "Type 'svn help' for usage." 
		return None

