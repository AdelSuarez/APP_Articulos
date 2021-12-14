from db.Connection import DataBase
from setting import config

class Consult():
	def __init__(self, serial, name, price, message):
		self._serial = serial
		self._name = name
		self._price = price
		self._message = message
		self.consult_item()

	def consult_item(self):
		'''Query the database, to display the information from the interface'''

		if len(self._serial.get()) != 0:
			query = 'SELECT * FROM ARTICULOS WHERE ID=?'
			parameters = ((self._serial.get()).strip(), )
			articles = DataBase(query, parameters).fetchall()
			print(articles)
			if articles != []:
				for i in articles:
					self._name.set(i[1])
					self._price.set(i[2])

				self._message['fg'] = config.READY
				self._message['text'] = '¡Consulta realizada con éxito!'

			elif articles == []:
				self._name.set('')
				self._price.set('')
				self._message['fg'] = config.WARNINGS
				self._message['text'] = 'El código no éxiste'


		else:
			self._name.set('')
			self._price.set('')
			self._message['fg'] = config.WARNINGS
			self._message['text'] = '¡El serial es requerido!'