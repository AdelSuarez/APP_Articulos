import tkinter as tk
from tkinter import messagebox
from conexion.crear_base_datos import crear_conexion
from funciones_menu_bar.funciones import cerrar_ap, acerca_de_funcion, borrar_lista_completa
from constantes import style

class Menu_bar(tk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		barra_menu = tk.Menu()
		self.master.config(menu=barra_menu)

		acerca_de = tk.Menu(barra_menu, tearoff=0, **style.submenu_configurations)
		acerca_de.add_command(label='Acerca de...', command=acerca_de_funcion)

		conexion = tk.Menu(barra_menu, tearoff=0, **style.submenu_configurations)
		conexion.add_command(label='Conectar', command=crear_conexion)
		conexion.add_command(label='Borrar lista', command=borrar_lista_completa)
		conexion.add_separator()
		conexion.add_command(label='Salir', command=lambda:cerrar_ap(*args))

		barra_menu.add_cascade(label='Conexion', menu=conexion)
		barra_menu.add_cascade(label='Acerca de', menu=acerca_de)
		



