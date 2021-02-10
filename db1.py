import sqlite3

class DB():
    """docstring for DB."""

    def __init__(self, name='data.sqlite3'):
        super(DB, self).__init__()
        self.name = name
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.name, check_same_thread = False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS db_db(
            id INT PRIMARY KEY,
            time TEXT,
            boxe_number TEXT,
            d1 TEXT,
            d2 TEXT,
            d3 TEXT,
            d4 TEXT,
            d5 TEXT,
            d6 TEXT)
            """)


    def append_data(self, data):
        self.cursor.execute("INSERT INTO db_db VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        self.conn.commit()

    def output_data(self):
        self.cursor.execute("SELECT * FROM db_db")
        return self.cursor.fetchall()