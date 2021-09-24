import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constantes import style
from conexion.borrar_articulo import borrar_articulo

class Borra_articulo(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.nombre_var = tk.StringVar()
		self.precio_var = tk.StringVar()

		self.frame_borrar = tk.Frame(self)
		self.frame_borrar.config(padx=160, bg=style.BACKGROUND)
		self.frame_borrar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_borrar, text='Borrar artículo', bg=style.BACKGROUND).grid(row=1, column=0, columnspan=2)
		
		tk.Label(self.frame_borrar, text='Código: ', bg=style.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.codigo_borrar = ttk.Entry(self.frame_borrar)
		self.codigo_borrar.grid(row=2, column=1, pady=4)

		tk.Label(self.frame_borrar, text='Nombre: ', bg=style.BACKGROUND).grid(row=3, column=0, sticky=tk.E)
		self.nombre = ttk.Entry(self.frame_borrar, state='readonly', textvariable=self.nombre_var)
		self.nombre.grid(row=3, column=1, pady=5)

		tk.Label(self.frame_borrar, text='Precio: ', bg=style.BACKGROUND).grid(row=4, column=0, sticky=tk.E)
		self.precio = ttk.Entry(self.frame_borrar, state='readonly', textvariable=self.precio_var)
		self.precio.grid(row=4, column=1, pady=4)

		ttk.Button(self.frame_borrar, text='Borrar', command=lambda:borrar_articulo(self.codigo_borrar, self.mensaje_info, self.nombre_var, self.precio_var)).grid(row=5, column=0, columnspan=2, pady=4)

		self.mensaje_info = tk.Label(self.frame_borrar, text='', bg=style.BACKGROUND)
		self.mensaje_info.grid(row=6, column=0, columnspan=2, pady=5)


