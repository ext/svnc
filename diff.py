import base
import subprocess

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
	
		self.path = '.'
		if len(argv) > 0:
			self.path = argv[-1]
	
	def execute(self):
		diff = self.client.diff('.', self.path)
		for line in diff.split("\n"):
			print format_line(line)
		
		diffstat = which('diffstat')
		if diffstat:
			p = subprocess.Popen([diffstat], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			diffstat = p.communicate(diff)[0]
			print diffstat

