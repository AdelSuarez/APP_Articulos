import tkinter as tk
from tkinter import ttk
from GUI.Win_create import Win_create
from GUI.Win_query import Win_query
from GUI.Win_list import Win_list
from GUI.Win_delete import Win_delete
from GUI.Win_edit import Win_edit
from menu_bar import Menu_bar


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
		self.create_widgets()

	def create_widgets(self):

		# Top bar
		self.menu_bar = Menu_bar(self.master)


		# Window manager
		self.notebook = ttk.Notebook(self)

		self.create = Win_create(self.notebook)
		self.query = Win_query(self.notebook)
		self.list = Win_list(self.notebook)
		self.delete = Win_delete(self.notebook)
		self.edit = Win_edit(self.notebook)

		self.notebook.add(self.create, text='Carga de artículos', padding=20)
		self.notebook.add(self.query, text='Consulta por código', padding=20)
		self.notebook.add(self.list, text='Listado completo', padding=20)
		self.notebook.add(self.delete, text='Borrado de artículo', padding=20)
		self.notebook.add(self.edit, text='Modificar artículo', padding=20)
		self.notebook.pack(pady=10, padx=10)

