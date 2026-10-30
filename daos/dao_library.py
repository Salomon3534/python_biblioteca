from daos.dao_db import ManagerDB
from daos.dao_books import ManagerBooks
from daos.dao_members import ManagerMembers


class ManagerLibrary:
    def __init__(self, logfile, dbfile):
        self.logfile = logfile
        self.dbfile = dbfile

        self.MGDB = ManagerDB(self.dbfile)
        self.MGBOOKS = ManagerBooks(self.MGDB.load_books())
        self.MGMEMBERS = ManagerMembers(self.MGDB.load_members())