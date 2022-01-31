import tkinter as tk
from tkinter import ttk
from setting import config
from db.Create import Create
from db.List import List

'''
	Clase que crea la venta de "Cargar de artículo" donde contiene los widgets y funciones de 
	dicha ventana
'''

class Win_create(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame_create = tk.Frame(self)
		self.frame_create.config(bg=config.BACKGROUND)
		self.frame_create.pack(fill=tk.BOTH, expand=True)

		tk.Label(self.frame_create, text='Artículo Nuevo', bg=config.BACKGROUND).grid(row=0, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

		tk.Label(self.frame_create, text='Nombre: ', bg=config.BACKGROUND).grid(row=1, column=0, sticky=tk.W)		
		self.name_create = ttk.Entry(self.frame_create)
		self.name_create.grid(row=1, column=1, pady=4)

		tk.Label(self.frame_create, text='Precio: ', bg=config.BACKGROUND).grid(row=2, column=0, sticky=tk.W)
		self.price_create = ttk.Entry(self.frame_create)
		self.price_create.grid(row=2, column=1, pady=4)

		tk.Button(self.frame_create, text='Confirmar', command=lambda:Create(self.name_create, self.price_create, self.message)).grid(row=3, column=0, columnspan=2, pady=4)

		self.message = tk.Label(self.frame_create, text='', bg=config.BACKGROUND)
		self.message.grid(row=4, column=0, columnspan=2, pady=6)






