import base

class url(base.SVNBase):
    def __init__(self, argv):
        base.SVNBase.__init__(self)

    def execute(self):
        entry = self.client.info('.')
        print entry.url

