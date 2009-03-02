import base
import subprocess
import getopt
import pysvn
import os
import sys

def which(program):
	import os
	def is_exe(fpath):
		return os.path.exists(fpath) and os.access(fpath, os.X_OK)

	fpath, fname = os.path.split(program)
	if fpath:
		if is_exe(program):
			return program
	else:
		for path in os.environ["PATH"].split(os.pathsep):
			exe_file = os.path.join(path, program)
			if is_exe(exe_file):
				return exe_file

	return None

def format_line(line):
	c = line[:1]
	if c == '+':
		return base.color_str(base.Green, line)
	elif c == '-':
		return base.color_str(base.Red, line)
	else:
		return line

class diff(base.SVNBase):
	def __init__(self, argv):
		base.SVNBase.__init__(self)
		
		opts, args = getopt.getopt(argv, 'r:c:Nx:', ['revision'])
		
		self.path = ['.']
		self.revision_start = pysvn.Revision(pysvn.opt_revision_kind.base)
		self.revision_end = pysvn.Revision(pysvn.opt_revision_kind.working)
		
		if len(args) > 0:
			self.path = args
		
		for key, value in opts:
			if key == '-r':
				self.revision_start, self.revision_stop = self.revision_from_argument(value)
			
			print key, ': ', value
	
	def revision_from_argument(self, string):
		parts = string.split(':')
		
		if len(parts) == 1:
			return self.revision_from_string(parts[0]), pysvn.Revision(pysvn.opt_revision_kind.working)
		
		if len(parts) == 2:
			return self.revision_from_string(parts[0]), self.revision_from_string(parts[1])
	
	def revision_from_string(self, string):
		try:
			return pysvn.Revision(pysvn.opt_revision_kind.number, int(string))
		except ValueError:
			try:
				return {
					'HEAD': pysvn.Revision(pysvn.opt_revision_kind.head),
					'BASE': pysvn.Revision(pysvn.opt_revision_kind.base),
					'COMMITED': pysvn.Revision(pysvn.opt_revision_kind.committed),
					'PREV': pysvn.Revision(pysvn.opt_revision_kind.previous),
					'WORKING': pysvn.Revision(pysvn.opt_revision_kind.working)
				}[string.upper()]
			except KeyError:
				# check if it is a date
				raise 'foo'
	
	def execute(self):
		print self.revision_end
		diff = self.client.diff(
			'.',
			self.path[0],
			self.revision_start,
			self.path[0],
			self.revision_end,
		)
		
		if os.isatty(sys.stdout.fileno()):
			for line in diff.split("\n"):
				print format_line(line)
		else:
			print diff
		
		diffstat = which('diffstat')
		if diffstat:
			p = subprocess.Popen([diffstat], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			diffstat = p.communicate(diff)[0]
			print diffstat

