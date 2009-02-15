import base

class diff(base.SVNBase):
	def __init__(self, argv):
		base.SVNBase.__init__(self)
	
		self.path = '.'
		if len(argv) > 0:
			self.path = argv[-1]
	
	def execute(self):
		print self.client.diff('.', self.path)
