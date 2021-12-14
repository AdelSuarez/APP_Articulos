from db.Connection import DataBase
import tkinter as tk
from tkinter import messagebox
from setting import config

class Delete():
	def __init__(self, serial, message, name, price):
		self._serial = serial
		self._name = name
		self._price = price
		self._message = message
		self.delete_item()


	def delete_item(self):
		serial_space = (self._serial.get()).strip()

		if len(serial_space) != 0:

			query = 'SELECT * FROM ARTICULOS WHERE ID=?'
			parameters = (serial_space, )
			articles = DataBase(query, parameters).fetchall()
			print(articles)

			if articles != []:
				for i in articles:
					self._name.set(i[1])
					self._price.set(i[2])
				value = messagebox.askquestion('Borrar artículo', 'Deseas borrar el artículo')

				if value == 'yes':
					query_delete = 'DELETE FROM ARTICULOS WHERE ID = ?'
					parameters_delete = (serial_space, )
					DataBase(query_delete, parameters_delete)
					self._serial.delete(0, tk.END)
					self._name.set('')
					self._price.set('')
					self._message['fg'] = config.READY
					self._message['text'] = '¡Artículo borrado con éxito!'

			elif articles == []:
				self._message['fg'] = config.WARNINGS
				self._message['text'] = '¡El código no éxiste!'

		else:
			self._message['fg'] = config.WARNINGS
			self._message['text'] = '¡El código es requerido!'

