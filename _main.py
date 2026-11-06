from controller import Controller

BOOKS_FILE = "db_books.txt"
MEMBERS_FILE = "db_members.txt"
LOG = "log.txt"


def main():
    controller = Controller(LOG, BOOKS_FILE, MEMBERS_FILE)
    controller.run()


if __name__ == "__main__":
    main()