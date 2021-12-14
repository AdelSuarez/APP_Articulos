import tkinter as tk
from tkinter import ttk
from setting import config
from db.Edit import Edit
from db.Edit_query import Edit_query


class Win_edit(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame_edit = tk.Frame(self)
		self.frame_edit.config(padx=150, bg=config.BACKGROUND)
		self.frame_edit.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_edit, text='Editar artículo', bg=config.BACKGROUND).grid(row=0, column=0, columnspan=2)

		tk.Label(self.frame_edit, text='Código: ', bg=config.BACKGROUND).grid(row=1, column=0, sticky=tk.E)
		self.serial_edit = ttk.Entry(self.frame_edit)
		self.serial_edit.grid(row=1, column=1, pady=4)

		self.name_var = tk.StringVar()
		self.price_var = tk.StringVar()

		# Old name
		tk.Label(self.frame_edit, text='Nombre: ', bg=config.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.old_name = ttk.Entry(self.frame_edit, state='readonly', textvariable=self.name_var)
		self.old_name.grid(row=2, column=1, pady=4)

		# New name
		tk.Label(self.frame_edit, text='Nuevo nombre: ', bg=config.BACKGROUND).grid(row=3, column=0, sticky=tk.E)
		self.new_name = ttk.Entry(self.frame_edit, state='readonly')
		self.new_name.grid(row=3, column=1, pady=4)

		# Old price
		tk.Label(self.frame_edit, text='Precio: ', bg=config.BACKGROUND).grid(row=4, column=0, sticky=tk.E)
		self.old_price = ttk.Entry(self.frame_edit, state='readonly', textvariable=self.price_var)
		self.old_price.grid(row=4, column=1, pady=4)

		# New price
		tk.Label(self.frame_edit, text='Nuevo precio: ', bg=config.BACKGROUND).grid(row=5, column=0, sticky=tk.E)
		self.new_price = ttk.Entry(self.frame_edit, state='readonly')
		self.new_price.grid(row=5, column=1, pady=4)

		ttk.Button(self.frame_edit, text='Verificar', command=lambda:Edit_query(self.serial_edit, self.name_var, self.price_var, self.message, self.button, self.new_name, self.new_price)).grid(row=6, column=0, pady=4)

		self.button = ttk.Button(self.frame_edit, text='Modificar', state=tk.DISABLED, command=lambda:Edit(self.serial_edit, self.name_var, self.price_var, self.new_name, self.new_price, self.message))
		self.button.grid(row=6, column=1, pady=4)

		self.message = tk.Label(self.frame_edit, text='', bg=config.BACKGROUND)
		self.message.grid(row=7, column=0, columnspan=2, pady=5)

