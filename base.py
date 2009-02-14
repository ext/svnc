import pysvn
import datetime

class SVNBase:
    def __init__(self, path):
        self.path = path
        self.client = pysvn.Client()

    def execute(self):
        pass

class url(SVNBase):
    def execute(self):
        entry = self.client.info(self.path)
        print entry.url

class info(SVNBase):
    def execute(self):
        entry = self.client.info(self.path)
        print 'Path: ', entry.name
        print 'URL: ', entry.url
        print 'Repository Root: ', entry.repos
        print 'Repository UUID: ', entry.uuid
        print 'Revision: ', entry.revision.number
        print 'Node Kind: ', entry.kind
        print 'Schedule: ', entry.schedule
        print 'Last commit author: ', entry.commit_author
        print 'Last commit rev: ', entry.commit_revision.number
        print 'Last commit date: ', datetime.datetime.fromtimestamp(entry.commit_time)

        if entry.copy_from_url:
            print 'Branched from: ', entry.copy_from_url, '@', reventry.copy_from_revision

        print

def factory(argv, path):
    command = argv[1]
    return eval(command + path)
