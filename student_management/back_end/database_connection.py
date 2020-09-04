import mysql.connector


# class for database connection
class DbConnection:
    def __init__(self):
        self.con = mysql.connector.connect(host='localhost', user='softwarica', password='Tokha321@',
                                           database='assignment')
        self.cursor = self.con.cursor()

    def insert(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def update(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def delete(self, query, values):
        self.cursor.execute(query, values)
        self.con.commit()

    def select(self, query):
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        self.con.commit()
        return records

    def user_login(self, query, values):
        self.cursor.execute(query, values)
        record = self.cursor.fetchall()
        self.con.commit()
        return record
