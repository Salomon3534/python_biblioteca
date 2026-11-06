class View:

    def show_menu(self) -> str:
        print("\n=== BIBLIOTECA ===")
        print("1. Mostrar todos los libros")
        print("2. Mostrar libros disponibles")
        print("3. Buscar libro por título")
        print("4. Prestar libro a un socio")
        print("5. Devolver libro de un socio")
        print("6. Mostrar socios con libro")
        print("7. Añadir socio o libro")
        print("8. Acabar")

        return input("Elige una opción: ")

    def ask_text(self, message) -> str:
        return input(message).strip()

    def ask_int(self, message) -> int | None:
        try:
            return int(input(message))
        except ValueError:
            return None

    def show_message(self, message):
        print(message)

    def show_books(self, books):
        if len(books) == 0:
            print("No hay libros.")
            return

        print(f"\n{'Cód':<6}{'Título':<40}{'Autor':<25}{'Año':<6}{'Estado'}")
        print("-" * 90)

        for book in books:
            state = "Disponible" if book.is_free() else f"Prestado (socio {book.currently_holding_code})"
            print(f"{book.code:<6}{book.title[:38]:<40}{book.author[:23]:<25}{book.year_published:<6}{state}")

    def show_loans(self, loans):
        if len(loans) == 0:
            print("Ningún socio tiene libros.")
            return

        for member, book in loans:
            print(f"[{member.code}] {member.name} -> [{book.code}] {book.title}")