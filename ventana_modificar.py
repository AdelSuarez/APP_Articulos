import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constantes import style
from conexion.modificar_articulo import verificacion_articulo, modificar_articulos


class Modificar_articulo(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.frame_modificar = tk.Frame(self)
		self.frame_modificar.config(padx=150, bg=style.BACKGROUND)
		self.frame_modificar.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		tk.Label(self.frame_modificar, text='Editar artículo', bg=style.BACKGROUND).grid(row=0, column=0, columnspan=2)

		tk.Label(self.frame_modificar, text='Código: ', bg=style.BACKGROUND).grid(row=1, column=0, sticky=tk.E)
		self.codigo_editar = ttk.Entry(self.frame_modificar)
		self.codigo_editar.grid(row=1, column=1, pady=4)

		self.nombre_var = tk.StringVar()
		self.precio_var = tk.StringVar()

		# Nombre antiguo
		tk.Label(self.frame_modificar, text='Nombre: ', bg=style.BACKGROUND).grid(row=2, column=0, sticky=tk.E)
		self.nombre_antiguo = ttk.Entry(self.frame_modificar, state='readonly', textvariable=self.nombre_var)
		self.nombre_antiguo.grid(row=2, column=1, pady=4)

		# Nombre nuevo
		tk.Label(self.frame_modificar, text='Nuevo nombre: ', bg=style.BACKGROUND).grid(row=3, column=0, sticky=tk.E)
		self.nombre_nuevo = ttk.Entry(self.frame_modificar, state='readonly')
		self.nombre_nuevo.grid(row=3, column=1, pady=4)

		# Precio antiguo
		tk.Label(self.frame_modificar, text='Precio: ', bg=style.BACKGROUND).grid(row=4, column=0, sticky=tk.E)
		self.precio_antiguo = ttk.Entry(self.frame_modificar, state='readonly', textvariable=self.precio_var)
		self.precio_antiguo.grid(row=4, column=1, pady=4)

		# Precio nuevo
		tk.Label(self.frame_modificar, text='Nuevo precio: ', bg=style.BACKGROUND).grid(row=5, column=0, sticky=tk.E)
		self.precio_nuevo = ttk.Entry(self.frame_modificar, state='readonly')
		self.precio_nuevo.grid(row=5, column=1, pady=4)

		ttk.Button(self.frame_modificar, text='Verificar', command=lambda:verificacion_articulo(self.codigo_editar, self.nombre_var, self.precio_var, self.mensaje_info, self.boton, self.nombre_nuevo, self.precio_nuevo)).grid(row=6, column=0, pady=4)
		self.boton = ttk.Button(self.frame_modificar, text='Modificar', state=tk.DISABLED, command=lambda:modificar_articulos(self.codigo_editar, self.nombre_var, self.precio_var, self.nombre_nuevo, self.precio_nuevo, self.mensaje_info))
		self.boton.grid(row=6, column=1, pady=4)

		self.mensaje_info = tk.Label(self.frame_modificar, text='', bg=style.BACKGROUND)
		self.mensaje_info.grid(row=7, column=0, columnspan=2, pady=5)

