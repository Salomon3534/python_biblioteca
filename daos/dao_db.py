from pathlib import Path

class ManagerDB:
    def __init__(self, from_file):
        self.from_file = Path(from_file)

    def read_file(self):

        if not self.from_file.exists():
            return ""

        return self.from_file.read_text(encoding="utf-8")

    def write_file(self, content):
        self.from_file.parent.mkdir(parents=True, exist_ok=True)
        self.from_file.write_text(content, encoding="utf-8")

    def append_file(self, content):
        self.from_file.parent.mkdir(parents=True, exist_ok=True)

        with self.from_file.open("a", encoding="utf-8") as file:
            file.write(content)

    def file_exists(self):
        return self.from_file.is_file()

    def delete_file(self):
        if self.file_exists():
            self.from_file.unlink()