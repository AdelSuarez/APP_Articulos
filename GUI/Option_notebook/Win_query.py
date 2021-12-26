import tkinter as tk
from tkinter import ttk
from db.Consult import Consult
from setting import config

class Win_query(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.name_var = tk.StringVar()
		self.price_var = tk.StringVar()


		self.frame_query = tk.Frame(self)
		self.frame_query.config(bg=config.BACKGROUND)
		self.frame_query.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_query, text='Consulta artículo', bg=config.BACKGROUND).grid(row=0, column=0, columnspan=2, pady=10)

		tk.Label(self.frame_query, text='Código: ', bg=config.BACKGROUND).grid(row=1, column=0, sticky=tk.E)
		self.serial_query = ttk.Entry(self.frame_query)
		self.serial_query.grid(row=1, column=1, pady=4)

		tk.Label(self.frame_query, text='Nombre: ', bg=config.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.name_query = ttk.Entry(self.frame_query, state='readonly', textvariable=self.name_var)
		self.name_query.grid(row=2, column=1, pady=4)

		tk.Label(self.frame_query, text='Precio: ', bg=config.BACKGROUND).grid(row=3, column=0, sticky=tk.E)
		self.price_query = ttk.Entry(self.frame_query, state='readonly', textvariable=self.price_var)
		self.price_query.grid(row=3, column=1, pady=4)

		ttk.Button(self.frame_query, text='Consultar', command=lambda:Consult(self.serial_query, self.name_var, self.price_var, self.message)).grid(row=4, column=0, columnspan=2, pady=4)

		self.message = tk.Label(self.frame_query, text='', bg=config.BACKGROUND)
		self.message.grid(row=5, column=0, columnspan=2, pady=5)