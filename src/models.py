class Token:
    id: int
    email: str
    value: str

    def __init__(self, id: int, email: str, value: str):
        self.id = id
        self.email = email
        self.value = value

    @staticmethod
    def from_db_cursor(cursor):
        return Token(cursor[0], cursor[1], cursor[2])

    def __str__(self):
        return f'token for: {self.email}'
