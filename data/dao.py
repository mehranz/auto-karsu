from datetime import datetime
import sqlite3 as db
import config
from data.models import Token


class DataAccessObject:

    db_name: str

    def __init__(self, db_name: str):
        self.db_name = f'{config.PROJECT_ROOT}/data/{db_name}{config.SQLITE_DB_FILE_EXTENSION}'
        self.create_tokens_table()

    def create_tokens_table(self):
        with db.connect(self.db_name) as connection:
            table_create_query = '''CREATE TABLE IF NOT EXISTS tokens
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                email VARCHAR (256) NOT NULL UNIQUE ,
                token TEXT NOT NULL ,
                last_submitted DATETIME
            )'''
            connection.execute(table_create_query)

    def check_exists(self, email: str) -> bool:
        with db.connect(self.db_name) as connection:
            select_query = f'SELECT * FROM tokens WHERE email = ?'
            query_result = connection.execute(select_query, (email, ))
            return True if len(query_result.fetchall()) != 0 else False

    def get_all_tokens(self):
        models = []
        with db.connect(self.db_name) as connection:
            result = connection.execute('SELECT * FROM tokens;')
            for t in result.fetchall():
                models.append(Token.from_db_cursor(t))
            return models

    def insert_token(self, email, token) -> bool:
        if self.check_exists(email):
            return self.update_token(email, token)

        with db.connect(self.db_name) as connection:
            insert_query = 'INSERT INTO tokens(id, email, token) VALUES (?, ?, ?);'
            connection.execute(insert_query, (None, email, token))
            return True

    def update_token(self, email, token):
        with db.connect(self.db_name) as connection:
            update_query = 'UPDATE tokens SET token=? WHERE email=?'
            connection.execute(update_query, (token, email))
            return True

    def track_submit(self, token: Token):
        with db.connect(self.db_name) as connection:
            q = 'UPDATE TOKENS SET last_submitted=? WHERE email=?'
            connection.execute(q, (datetime.utcnow().isoformat(), token.value))
            return True


dao = DataAccessObject('tokens')
