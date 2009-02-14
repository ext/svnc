import pysvn

class SVNBase:
    def __init__(self):
        self.client = pysvn.Client()

    def execute(self):
        pass

from url import *
from info import *
from status import *

def factory(argv):
    command = argv[0]
    return eval(command)(argv[1:])
