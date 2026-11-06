from models.member import Member


class DaoMembers():
    def __init__(self, members):
        self.members = members
        self.counter = 0

        for member in self.members:
            if member.code >= self.counter:
                self.counter = member.code + 1

    def create_member(self, name, email) -> bool:

        try:
            new_member = Member(self.counter, name, email)

            self.members.append(new_member)
            self.counter += 1

            return True
        except Exception:
            return False

    def remove_member(self, code) -> bool:

        try:
            member_found = self.search_member(code)

            if member_found is None:
                return False

            self.members.remove(member_found)

            return True
        except ValueError:
            return False

    def update_member(self, code_member_to_update, new_name, new_email) -> bool:

        try:
            member_found = self.search_member(code_member_to_update)

            if member_found is None:
                return False

            member_found.name = new_name
            member_found.email = new_email

            return True
        except AttributeError:
            return False

    def search_member(self, code) -> Member | None:

        for member in self.members:
            if member.code == code:
                return member

        return None

    def get_members_with_book(self) -> list:
        members_with_book = []

        for member in self.members:
            if member.has_book():
                members_with_book.append(member)

        return members_with_book