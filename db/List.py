from db.Connection import DataBase
import tkinter as tk
import sqlite3 as sql
from setting import config

class List():
	def __init__(self, list, message):
		self._list = list
		self._message = message
		self.complete_list()


	def complete_list(self):
		self._list.config(state = tk.NORMAL)
		try:
			query = 'SELECT * FROM ARTICULOS'
			articles = DataBase(query, ).fetchall()
			print(articles)
			self._list.delete(1.0, tk.END)

			for serial, name, price in articles:
				self._list.insert(1.0, f'CÓDIGO: {serial} | Descripción: {name} -- Precio: {price} $\n')

			self._message['text'] = ''

		except sql.OperationalError:
			self._message['fg'] = config.WARNINGS
			self._message['text'] = 'No se a conectado a la base de datos'

		self._list.config(state = tk.DISABLED)	

