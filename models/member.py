class Member:

    NONE_INDICATOR = "none"

    def __init__(self, code, name, email, currently_holding_code: int | str = NONE_INDICATOR):
        self.code = code
        self.name = name
        self.email = email
        self.currently_holding_code = currently_holding_code

    def has_book(self) -> bool:
        return self.currently_holding_code != self.NONE_INDICATOR

    def assign_book(self, wanted_book) -> bool:
        if not self.has_book():
            self.currently_holding_code = wanted_book
            return True
        return False

    def return_lended_book(self) -> bool:
        if self.has_book():
            self.currently_holding_code = self.NONE_INDICATOR
            return True
        return False