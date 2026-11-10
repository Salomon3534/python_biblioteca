from pathlib import Path

from controller import Controller

DATA_DIR = Path(__file__).resolve().parent / "_data"
BOOKS_FILE = DATA_DIR / "db_books.txt"
MEMBERS_FILE = DATA_DIR / "db_members.txt"
LOG = DATA_DIR / "log.txt"


def main():
    DATA_DIR.mkdir(exist_ok=True)

    controller = Controller(LOG, BOOKS_FILE, MEMBERS_FILE)
    controller.run()


if __name__ == "__main__":
    main()