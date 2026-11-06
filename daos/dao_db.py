from pathlib import Path

from models.book import Book
from models.member import Member


class ManagerDB:
    SEPARATOR = ";"

    def __init__(self, books_file, members_file):
        self.books_file = Path(books_file)
        self.members_file = Path(members_file)

    def read_lines(self, file_path) -> list:
        if not file_path.exists():
            return []

        lines = file_path.read_text(encoding="utf-8").splitlines()

        return [line for line in lines if line.strip() != ""]

    def parse_holding(self, text, indicator):
        if text == indicator:
            return indicator
        return int(text)

    def load_books(self) -> list:
        books = []

        for line in self.read_lines(self.books_file):
            fields = line.split(self.SEPARATOR)

            holding = Book.FREE_INDICATOR
            if len(fields) > 5:
                holding = self.parse_holding(fields[5], Book.FREE_INDICATOR)

            books.append(Book(int(fields[0]), fields[1], fields[2], int(fields[3]), fields[4], holding))

        return books

    def load_members(self) -> list:
        members = []

        for line in self.read_lines(self.members_file):
            fields = line.split(self.SEPARATOR)

            holding = Member.NONE_INDICATOR
            if len(fields) > 3:
                holding = self.parse_holding(fields[3], Member.NONE_INDICATOR)

            members.append(Member(int(fields[0]), fields[1], fields[2], holding))

        return members

    def save_books(self, books) -> bool:

        try:
            lines = []

            for book in books:
                lines.append(self.SEPARATOR.join([
                    str(book.code), book.title, book.author,
                    str(book.year_published), book.category,
                    str(book.currently_holding_code)
                ]))

            self.books_file.write_text("\n".join(lines), encoding="utf-8")
            return True
        except OSError:
            return False

    def save_members(self, members) -> bool:

        try:
            lines = []

            for member in members:
                lines.append(self.SEPARATOR.join([
                    str(member.code), member.name, member.email,
                    str(member.currently_holding_code)
                ]))

            self.members_file.write_text("\n".join(lines), encoding="utf-8")
            return True
        except OSError:
            return False