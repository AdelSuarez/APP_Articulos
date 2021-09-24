import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constantes import style
from conexion.crear_articulo import articulo_creado

'''
	Clase que crea la venta de "Cargar de artículo" donde contiene los widgets y funciones de 
	dicha ventana
'''

class Crear_articulo(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame_crear = tk.Frame(self)
		self.frame_crear.config(padx=160, bg=style.BACKGROUND)
		self.frame_crear.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_crear, text='Artículo Nuevo', bg=style.BACKGROUND).grid(row=0, column=0, columnspan=2, pady=10)

		tk.Label(self.frame_crear, text='Nombre: ', bg=style.BACKGROUND).grid(row=1, column=0, sticky=tk.E)		
		self.nombre_crear = ttk.Entry(self.frame_crear)
		self.nombre_crear.grid(row=1, column=1, pady=4)

		tk.Label(self.frame_crear, text='Precio: ', bg=style.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.precio_crear = ttk.Entry(self.frame_crear)
		self.precio_crear.grid(row=2, column=1, pady=4)

		ttk.Button(self.frame_crear, text='Confirmar', command=lambda:articulo_creado(self.nombre_crear, self.precio_crear, self.mensaje_info)).grid(row=3, column=0, columnspan=2, pady=4)

		self.mensaje_info = tk.Label(self.frame_crear, text='', bg=style.BACKGROUND)
		self.mensaje_info.grid(row=4, column=0, columnspan=2, pady=6)






