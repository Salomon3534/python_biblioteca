from daos.dao_library import ManagerLibrary
from errors.lending_error import LendingError
from view import View


class Controller:
    def __init__(self, logfile, books_file, members_file):
        self.library = ManagerLibrary(logfile, books_file, members_file)
        self.view = View()

    def run(self):
        self.view.show_message(f"Se ha cargado la información de {self.library.count_books()} libros.")
        self.view.show_message(f"Se ha cargado la información de {self.library.count_members()} socios.")

        options = {
            "1": self.option_show_all_books,
            "2": self.option_show_free_books,
            "3": self.option_search_book,
            "4": self.option_lend_book,
            "5": self.option_return_book,
            "6": self.option_show_loans,
            "7": self.option_add,
        }

        running = True

        while running:
            option = self.view.show_menu()

            if option == "8":
                self.option_exit()
                running = False
            elif option in options:
                options[option]()
            else:
                self.view.show_message("Opción no válida.")

    def option_show_all_books(self):
        self.view.show_books(self.library.get_books())

    def option_show_free_books(self):
        self.view.show_books(self.library.get_free_books())

    def option_search_book(self):
        term = self.view.ask_text("Término del título: ")
        found_books = self.library.search_books(term)

        if len(found_books) == 0:
            self.view.show_message("No existe ningún libro con ese término.")
        else:
            self.view.show_books(found_books)

    def option_lend_book(self):
        book_code = self.view.ask_int("Código del libro: ")
        member_code = self.view.ask_int("Código del socio: ")

        try:
            self.library.lend_book(book_code, member_code)
            self.view.show_message("Préstamo realizado.")
        except LendingError as error:
            self.view.show_message(f"{error.message} (libro: {error.book_code}, socio: {error.member_code})")

    def option_return_book(self):
        member_code = self.view.ask_int("Código del socio: ")

        try:
            book = self.library.return_book(member_code)
            self.view.show_message(f"Libro devuelto: {book.title}")
        except LendingError as error:
            self.view.show_message(f"{error.message} (socio: {error.member_code})")

    def option_show_loans(self):
        self.view.show_loans(self.library.get_loans())

    def option_add(self):
        choice = self.view.ask_text("¿Qué quieres añadir? (1 = libro, 2 = socio): ")

        if choice == "1":
            self.add_book()
        elif choice == "2":
            self.add_member()
        else:
            self.view.show_message("Opción no válida.")

    def add_book(self):
        title = self.view.ask_text("Título: ")
        author = self.view.ask_text("Autor: ")
        year_p = self.view.ask_int("Año de publicación: ")
        category = self.view.ask_text("Categoría: ")

        if year_p is None:
            self.view.show_message("El año tiene que ser un número.")
        elif self.library.add_book(title, author, year_p, category):
            self.view.show_message("Libro añadido.")
        else:
            self.view.show_message("No se pudo añadir el libro.")

    def add_member(self):
        name = self.view.ask_text("Nombre: ")
        email = self.view.ask_text("Email: ")

        if self.library.add_member(name, email):
            self.view.show_message("Socio añadido.")
        else:
            self.view.show_message("No se pudo añadir el socio.")

    def option_exit(self):
        if self.library.save():
            self.view.show_message("Datos guardados en los ficheros.")
        else:
            self.view.show_message("Error al guardar los datos.")