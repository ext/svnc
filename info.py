import base
import datetime

class info(base.SVNBase):
    def __init__(self, argv):
        base.SVNBase.__init__(self)

        self.path = '.'

        if len(argv) > 0:
            self.path = argv[-1]

    def execute(self):
        entry = self.client.info(self.path)
        print 'Path: ', self.path

        if self.path != entry.name:
            print 'Name: ', entry.name

        if entry.copy_from_url:
            print 'Branched from: ', entry.copy_from_url, '@', reventry.copy_from_revision

        print 'URL: ', entry.url
        print 'Repository Root: ', entry.repos
        print 'Repository UUID: ', entry.uuid
        print 'Revision: ', entry.revision.number
        print 'Node Kind: ', entry.kind
        print 'Schedule: ', entry.schedule
        print 'Last commit author: ', entry.commit_author
        print 'Last commit rev: ', entry.commit_revision.number
        print 'Last commit date: ', datetime.datetime.fromtimestamp(entry.commit_time)
        print 'Text Last Updated: ', datetime.datetime.fromtimestamp(entry.text_time)
        print 'Checksum: ', entry.checksum

        print
