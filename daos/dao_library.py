from datetime import datetime

from daos.dao_db import ManagerDB

from daos.dao_books import DaoBooks
from daos.dao_members import DaoMembers
from models.book import Book

from errors.lending_error import LendingError


class ManagerLibrary:
    def __init__(self, logfile, books_file, members_file):
        self.logfile = logfile

        self.MGDB = ManagerDB(books_file, members_file)
        self.MGBOOKS = DaoBooks(self.MGDB.load_books())
        self.MGMEMBERS = DaoMembers(self.MGDB.load_members())

    def write_log(self, event, details):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.logfile, "a", encoding="utf-8") as file:
            file.write(f"[{date}][{event}][{details}]\n")

    def count_books(self) -> int:
        return len(self.MGBOOKS.books)

    def count_members(self) -> int:
        return len(self.MGMEMBERS.members)

    def get_books(self) -> list:
        return self.MGBOOKS.books

    def get_free_books(self) -> list:
        return self.MGBOOKS.get_free_books()

    def search_books(self, term) -> list:
        return self.MGBOOKS.search_by_title(term)

    def add_book(self, title, author, year_p, category) -> bool:
        created = self.MGBOOKS.create_book(title, author, year_p, category)

        if created:
            self.write_log("NUEVO_LIBRO", f"Libro añadido: {title}")

        return created

    def add_member(self, name, email) -> bool:
        created = self.MGMEMBERS.create_member(name, email)

        if created:
            self.write_log("NUEVO_SOCIO", f"Socio añadido: {name}")

        return created

    def lend_book(self, book_code, member_code):
        book = self.MGBOOKS.search_book(book_code)
        member = self.MGMEMBERS.search_member(member_code)

        if book is None:
            raise LendingError("El libro no existe.", book_code, member_code)

        if member is None:
            raise LendingError("El socio no existe.", book_code, member_code)

        if member.has_book():
            raise LendingError("El socio ya tiene un libro.", book_code, member_code)

        if not book.is_free():
            raise LendingError("El libro lo tiene otro socio.", book_code, member_code)

        book.lend(member.code)
        member.assign_book(book.code)

        self.write_log("PRESTAMO", f"Libro {book.code} ({book.title}) prestado al socio {member.code} ({member.name})")

    def return_book(self, member_code) -> Book:
        member = self.MGMEMBERS.search_member(member_code)

        if member is None:
            raise LendingError("El socio no existe.", None, member_code)

        if not member.has_book():
            raise LendingError("El socio no tiene ningún libro.", None, member_code)

        book = self.MGBOOKS.search_book(member.currently_holding_code)

        if book is None:
            raise LendingError("El libro del socio no existe.", member.currently_holding_code, member_code)

        book.free()
        member.return_lended_book()

        self.write_log("DEVOLUCION", f"Libro {book.code} ({book.title}) devuelto por el socio {member.code} ({member.name})")

        return book

    def get_loans(self) -> list:
        loans = []

        for member in self.MGMEMBERS.get_members_with_book():
            book = self.MGBOOKS.search_book(member.currently_holding_code)

            if book is not None:
                loans.append((member, book))

        return loans

    def save(self) -> bool:
        books_saved = self.MGDB.save_books(self.MGBOOKS.books)
        members_saved = self.MGDB.save_members(self.MGMEMBERS.members)

        return books_saved and members_saved