import base
import pysvn

def compare(x,y):
	s = compare_status(x.text_status, y.text_status)
	if s <> 0:
		return s
	else:
		return cmp(x.path, y.path)

status_dict = {
	pysvn.wc_status_kind.added:0,
	pysvn.wc_status_kind.modified:0,
	pysvn.wc_status_kind.normal:2,
	pysvn.wc_status_kind.ignored:9
}

def compare_status(x,y):
	return status_dict[x] < status_dict[y]

def filter_changes(x):
	return not( x.text_status == pysvn.wc_status_kind.ignored or x.text_status == pysvn.wc_status_kind.normal )

def c(color, str):
	return base.color_str(color, str)

formatkey_dict = {
	pysvn.wc_status_kind.none:' ',
	pysvn.wc_status_kind.unversioned: '?',
	pysvn.wc_status_kind.normal: ' ',
	pysvn.wc_status_kind.added: c(base.Green, 'A'),
	pysvn.wc_status_kind.missing: c(base.Red, '!'),
	pysvn.wc_status_kind.deleted: c(base.Blue, 'D'),
	pysvn.wc_status_kind.replaced: 'R',
	pysvn.wc_status_kind.modified: c(base.White, 'M'),
	pysvn.wc_status_kind.merged: 'G',
	pysvn.wc_status_kind.conflicted: c(base.Red, 'C'),
	pysvn.wc_status_kind.ignored: 'I',
	pysvn.wc_status_kind.obstructed: c(base.Red, '~'),
	pysvn.wc_status_kind.external: 'X',
	pysvn.wc_status_kind.incomplete: ' '
}

def format(x):
	return '%s%s%s %s' % (
			format_status(x),
			format_prop(x),
			format_lock(x), 
			x.path)

def format_status(x):
	return formatkey_dict[x.text_status]

def format_prop(x):
	return formatkey_dict[x.prop_status]

def format_lock(x):
	if x.is_locked:
		return 'L'
	else:
		return ' '

class status(base.SVNBase):
	def __init__(self, argv):
		base.SVNBase.__init__(self)
	
		self.path = '.'
		if len(argv) > 0:
			self.path = argv[-1]
	
	def execute(self):
		changes = self.client.status(self.path)
		
		changes.sort(cmp=compare)
		
		for file in filter(filter_changes, changes):
			print format(file)
