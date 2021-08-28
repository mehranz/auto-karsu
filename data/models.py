from datetime import datetime


class Token:
    id: int
    email: str
    value: str
    last_submit: datetime

    def __init__(self, id: int, email: str, value: str, last_submit: datetime):
        self.id = id
        self.email = email
        self.value = value
        self.last_submit = last_submit

    @staticmethod
    def from_db_cursor(cursor):
        return Token(cursor[0], cursor[1], cursor[2], cursor[3])

    def __str__(self):
        return f'token for: {self.email}'
