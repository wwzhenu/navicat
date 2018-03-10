from sqlite3 import *


class manageSqlite:
    file = "connections.db"
    conn = connect(file)
    conn.row_factory=Row
    cursor = conn.cursor()

    def __init__(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS connections (name VARCHAR(20), host VARCHAR(20), port VARCHAR(10), user VARCHAR(50), pwd VARCHAR(50))')

    def addConnect(self, name, host, port, user, pwd):
        self.cursor.execute("INSERT INTO connections(name, host, port, user, pwd) VALUES (?,?,?,?,?)",
                            (name, host, port, user, pwd))
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def showConnect(self):
        self.cursor.execute("SELECT * FROM connections")
        data = self.cursor.fetchall()
        return data