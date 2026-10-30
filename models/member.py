class Member:

    NONE_INDICATOR = "none"

    def __init__(self, code, name, email, currently_holding_code = NONE_INDICATOR):
        self.code = code
        self.name = name
        self.email = email
        self.currently_holding_code = currently_holding_code

    def assign_book(self, wanted_book) -> bool:
        if self.currently_holding_code == self.NONE_INDICATOR:
            self.currently_holding_code = wanted_book
            return True
        else:
            return False


    def return_lended_book(self) -> bool:
        if self.currently_holding_code != self.NONE_INDICATOR:
            self.currently_holding_code = self.NONE_INDICATOR
            return True
        else:
            return False