from models.book import Book


class DaoBooks():
    def __init__(self, books):
        self.books = books
        self.counter = 0

        for book in self.books:
            if book.code >= self.counter:
                self.counter = book.code + 1

    def create_book(self, title, author, year_p, category) -> bool:

        try:
            new_book = Book(self.counter, title, author, year_p, category)

            self.books.append(new_book)
            self.counter += 1

            return True
        except Exception:
            return False

    def remove_book(self, code) -> bool:

        try:
            book_found = self.search_book(code)

            if book_found is None:
                return False

            self.books.remove(book_found)

            return True
        except ValueError:
            return False

    def update_book(self, code_book_to_update, new_t, new_a, new_y, new_cat) -> bool:

        try:
            book_found = self.search_book(code_book_to_update)

            if book_found is None:
                return False

            book_found.title = new_t
            book_found.author = new_a
            book_found.year_published = new_y
            book_found.category = new_cat

            return True
        except AttributeError:
            return False

    def search_book(self, code) -> Book | None:

        for book in self.books:
            if book.code == code:
                return book

        return None

    def search_by_title(self, term) -> list:
        found_books = []

        for book in self.books:
            if book.matches_title(term):
                found_books.append(book)

        return found_books

    def get_free_books(self) -> list:
        free_books = []

        for book in self.books:
            if book.is_free():
                free_books.append(book)

        return free_books