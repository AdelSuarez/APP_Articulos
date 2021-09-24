import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conexion.consultar_articulo import consultar_articulo
from constantes import style

class Consultar_articulo(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.nombre = tk.StringVar()
		self.precio = tk.StringVar()


		self.frame_consulta = tk.Frame(self)
		self.frame_consulta.config(padx=160, bg=style.BACKGROUND)
		self.frame_consulta.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_consulta, text='Consulta artículo', bg=style.BACKGROUND).grid(row=0, column=0, columnspan=2, pady=10)

		tk.Label(self.frame_consulta, text='Código: ', bg=style.BACKGROUND).grid(row=1, column=0, sticky=tk.E)
		self.codigo_consulta = ttk.Entry(self.frame_consulta)
		self.codigo_consulta.grid(row=1, column=1, pady=4)

		tk.Label(self.frame_consulta, text='Nombre: ', bg=style.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.nombre_consulta = ttk.Entry(self.frame_consulta, state='readonly', textvariable=self.nombre)
		self.nombre_consulta.grid(row=2, column=1, pady=4)

		tk.Label(self.frame_consulta, text='Precio: ', bg=style.BACKGROUND).grid(row=3, column=0, sticky=tk.E)
		self.precio_consulta = ttk.Entry(self.frame_consulta, state='readonly', textvariable=self.precio)
		self.precio_consulta.grid(row=3, column=1, pady=4)

		ttk.Button(self.frame_consulta, text='Consultar', command=lambda:consultar_articulo(self.codigo_consulta, self.nombre, self.precio, self.mensaje_info)).grid(row=4, column=0, columnspan=2, pady=4)

		self.mensaje_info = tk.Label(self.frame_consulta, text='', bg=style.BACKGROUND)
		self.mensaje_info.grid(row=5, column=0, columnspan=2, pady=5)