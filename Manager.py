import tkinter as tk
from tkinter import ttk
from ventana_crear import Crear_articulo
from ventana_consulta import Consultar_articulo
from ventana_lista import Lista_articulos
from ventana_borrar import Borra_articulo
from ventana_modificar import Modificar_articulo
from menu_bar import Menu_bar
from constantes import style

'''
	Clase que administra todas las clases que crean ventanas y contiene el notebook que utiliza todas 
	las calles importadas, ademas que la clase manager crea la ventana principal de la app
'''

class Manager(ttk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.resizable(0,0)
		self.pack()
		self.crear_widgets()

	def crear_widgets(self):

		# Barra superion de opciones
		self.menu_bar = Menu_bar(self.master)


		# Gestor de la ventanas de enventos
		self.notebook = ttk.Notebook(self)

		self.crear_ventana = Crear_articulo(self.notebook)
		self.consultar_articulo = Consultar_articulo(self.notebook)
		self.lista_articulos = Lista_articulos(self.notebook)
		self.borrar_articulo = Borra_articulo(self.notebook)
		self.modificar_articulo = Modificar_articulo(self.notebook)

		self.notebook.add(self.crear_ventana, text='Carga de artículos', padding=20)
		self.notebook.add(self.consultar_articulo, text='Consulta por código', padding=20)
		self.notebook.add(self.lista_articulos, text='Listado completo', padding=20)
		self.notebook.add(self.borrar_articulo, text='Borrado de artículo', padding=20)
		self.notebook.add(self.modificar_articulo, text='Modificar artículo', padding=20)
		self.notebook.pack(pady=10, padx=10)

