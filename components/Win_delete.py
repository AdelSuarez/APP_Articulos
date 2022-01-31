import tkinter as tk
from tkinter import ttk
from setting import config
from db.Delete import Delete


class Win_delete(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.name_var = tk.StringVar()
		self.price_var = tk.StringVar()

		self.frame_delete = tk.Frame(self)
		self.frame_delete.config(bg=config.BACKGROUND)
		self.frame_delete.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_delete, text='Borrar artículo', bg=config.BACKGROUND).grid(row=1, column=0, columnspan=2)
		
		tk.Label(self.frame_delete, text='Código: ', bg=config.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.serial_delete = ttk.Entry(self.frame_delete)
		self.serial_delete.grid(row=2, column=1, pady=4)

		tk.Label(self.frame_delete, text='Nombre: ', bg=config.BACKGROUND).grid(row=3, column=0, sticky=tk.E)
		self.name = ttk.Entry(self.frame_delete, state='readonly', textvariable=self.name_var)
		self.name.grid(row=3, column=1, pady=5)

		tk.Label(self.frame_delete, text='Precio: ', bg=config.BACKGROUND).grid(row=4, column=0, sticky=tk.E)
		self.price = ttk.Entry(self.frame_delete, state='readonly', textvariable=self.price_var)
		self.price.grid(row=4, column=1, pady=4)

		ttk.Button(self.frame_delete, text='Borrar', command=lambda:Delete(self.serial_delete, self.message, self.name_var, self.price_var)).grid(row=5, column=0, columnspan=2, pady=4)

		self.message = tk.Label(self.frame_delete, text='', bg=config.BACKGROUND)
		self.message.grid(row=6, column=0, columnspan=2, pady=5)


