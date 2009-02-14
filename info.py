import base
import datetime

class info(base.SVNBase):
    def __init__(self, argv):
        base.SVNBase.__init__(self)

        self.path = '.'
        self.recurse = False

        if len(argv) > 0:
            self.path = argv[-1]

    def execute(self):
        entries = self.client.info2(self.path, recurse=self.recurse)

        for file, entry in entries:
            self.display(file, entry)

    def display(self, file, entry):
        wc = entry.wc_info

        print 'Path: ', self.path
        self.display_field(entry, 'URL: ', 'URL')
        self.display_field(entry, 'Repository Root: ', 'repos_root_URL')
        if wc and wc.copyfrom_url:
            self.display_field(wc, 'Branched from', 'copyfrom_url')
            self.display_field(wc, 'Branched at', 'copyfrom_rev', self.format_revision)
        self.display_field(entry, 'Repository UUID: ', 'repos_UUID')
        self.display_field(entry, 'Revision: ', 'rev', self.format_rev)
        self.display_field(entry, 'Node Kind: ', 'kind')
        if wc:
            self.display_field(wc, 'Schedule: ', 'schedule')
        self.display_field(entry, 'Last commit author: ', 'last_changed_author')
        self.display_field(entry, 'Last commit rev', 'last_changed_rev', self.format_rev)
        self.display_field(entry, 'Last commit date', 'last_changed_date', self.format_datetime)

        if wc:
            self.display_field(wc, 'Text Last Updated: ', 'text_time', self.format_datetime)
            self.display_field(wc, 'Checksum', 'checksum')

        print

    def display_field(self, container, info, field, format = None):
        value = container.data[field]
        if value:
            if format:
                print info + ': ', format(value)
            else:
                print info + ': ', value
    
    def format_datetime(self, timestamp):
        t = datetime.datetime.fromtimestamp(timestamp)
        return t.strftime('%Y-%m-%d %H:%M:%S %z (%a, %d %b %Y)')

    def format_rev(self, rev):
        return rev.number
