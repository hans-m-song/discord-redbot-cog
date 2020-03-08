import sys
import os

# TODO figure out where to put a default config file

class File:

    def __init__(self, db_path=None):
        self.pwd = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.db_path = (self.pwd + db_path) if db_path is not None else None

    def load(self, filename=None):
        if filename is None:
            path = self.db_path
        else:
            path = self.pwd + filename

        with open(self.pwd + filename, "r") as f:
            db = [i.rstrip() for i in f]
            return db

    def save(self, db, filename=None):
        if filename is None:
            path = self.db_path
        else:
            path = self.pwd + filename

        with open(self.pwd + filename, "w") as f:
            f.write('\n'.join(db))
