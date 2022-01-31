import sqlite3 as sql

class DataBase():
	def __init__(self, query, parameter = ()):
		self._query = query
		self._parameters = parameter
		self._db = 'DataBase.db'
		self.query_db()

	def query_db(self):
		self.conn = sql.connect(self._db)
		self.cur = self.conn.cursor()
		result = self.cur.execute(self._query, self._parameters)
		self.conn.commit()
		return result

	def fetchall(self):
		return self.query_db().fetchall()