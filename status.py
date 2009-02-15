import base
import pysvn

class status(base.SVNBase):
    def __init__(self, argv):
        base.SVNBase.__init__(self)

        self.path = '.'
        if len(argv) > 0:
            self.path = argv[-1]

    def execute(self):
        changes = self.client.status(self.path)
        changes.sort()

        added, deleted, modified, conflicts, unversioned, other = self.partition(changes)

        for file in conflicts:
            self.printc(base.Red, "C\t%s" % file)

        for file in added:
            self.printc(base.Green, "A\t%s" % file)

        for file in deleted:
            self.printc(base.Blue, "D\t%s" % file)

        for file in modified:
            self.printc(base.White, "M\t%s" % file)

        for file in unversioned:
            self.printc(base.Reset, "?\t%s" % file)

        for file in other:
            self.printc(base.Reset, "-\t%s" % file)

    def partition(self, files):
        added = []
        deleted = []
        modified = []
        conflicts = []
        unversioned = []
        other = []

        for file in files:
            if file.text_status == pysvn.wc_status_kind.added:
                added.append(file.path)
            elif file.text_status == pysvn.wc_status_kind.deleted:
                deleted.append(file.path)
            elif file.text_status == pysvn.wc_status_kind.modified:
                modified.append(file.path)
            elif file.text_status == pysvn.wc_status_kind.conflicted:
                conflicts.append(file.path)
            elif file.text_status == pysvn.wc_status_kind.unversioned:
                unversioned.append(file.path)
            else:
                other.append(file.path)


        return (added, deleted, modified, conflicts, unversioned, other)
