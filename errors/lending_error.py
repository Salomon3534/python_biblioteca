class LendingError(Exception):

    def __init__(self, message, book_code, member_code):
        super().__init__(message)
        self.message = message
        self.book_code = book_code
        self.member_code = member_code