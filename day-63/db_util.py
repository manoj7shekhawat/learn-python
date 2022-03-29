import sqlite3 as sql


class DBUtil:

    def __init__(self):
        super().__init__()

    def create_table(self):
        db = sql.connect("books-collection.db")
        db.execute(
            "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)"
        )

    def get_books(self):
        connection = sql.connect("books-collection.db")
        crsr = connection.cursor()
        crsr.execute(f"SELECT * FROM books")
        result = crsr.fetchall()
        connection.close()
        print(f"{result}")
        return result

    def insert_row(self, title, author, rating):
        connection = sql.connect("books-collection.db")
        crsr = connection.cursor()
        crsr.execute(f"INSERT INTO books VALUES(2, '{title}', '{author}', '{rating}')")
        connection.commit()
        connection.close()