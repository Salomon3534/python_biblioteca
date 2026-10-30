

DB_FILE = "_library_db.csv"
LOG = "_log.txt"

MG_DB = ManagerDB(DB_FILE)

MG_BOOKS = ManagerBooks(MG_DB.get_books())
MG_MEMBERS = ManagerMembers(MG_DB.get_members())