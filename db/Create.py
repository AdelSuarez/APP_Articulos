import tkinter as tk
import random
from db.Connection import DataBase
from setting import config


class Create():
	def __init__(self, name, price, message):
		self._name = name
		self._price = price
		self._message = message
		self.create_item()


	def create_item(self):
		if self.field_validation(self._name, self._price):
			if self.price_validation(self._price):
				query = 'INSERT INTO ARTICULOS VALUES(?,?,?)'
				parameters = (self.serial_generator(), self._name.get(), self._price.get())
				DataBase(query, parameters)
				self._name.delete(0, tk.END)
				self._price.delete(0, tk.END)
				self._message['fg'] = config.READY
				self._message['text'] = '¡Artículo cargado con éxito!'

		else:
			self._message['fg'] = config.WARNINGS
			self._message['text'] = '¡Nombre y precio son requeridos'


	def field_validation(self, name, price):
		'''Validates that the user has not left empty fields in the inputs'''

		return len(name.get()) != 0 and len(price.get()) != 0


	def price_validation(self, price):
		'''Verify that they have not entered letters in the price field
			Observation: the funtion still needs to be polished so that it 
			receives float values'''

		try:
			return isinstance(int(price.get()), int)
		except ValueError:
			self._message['fg'] = config.WARNINGS
			self._message['text'] = '¡El precio no acepta letras!' 


	def serial_generator(self):
		''' Generate a unique serial to identify the items'''

		serial = ('')

		for i in range(5):
			number = random.randint(0, 9)
			serial += str(number)

		for i in range(1):
			vocal = random.choice('AEIOU')
			serial += vocal

		return serial


