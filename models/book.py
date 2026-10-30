class Book:

    FREE_INDICATOR = "free"

    def __init__(self, code, title, author, year_published, category, currently_holding_code = FREE_INDICATOR):
        self.code = code
        self.title = title
        self.author = author
        self.year_published = year_published
        self.category = category
        self.currently_holding_code = currently_holding_code


    def lend(self, new_owner) -> bool:
        if self.currently_holding_code != self.FREE_INDICATOR:
            self.currently_holding_code = new_owner
            return True
        else:
            return False
        

    def free(self) -> bool:
        self.currently_holding_code = self.FREE_INDICATOR
        return True

    