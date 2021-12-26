import tkinter as tk
from tkinter import ttk
from setting import config
from GUI.NavBar import Navbar
from GUI.Table import Table
from GUI.Notebook import Notebook
from GUI.Notification_bar import Notification

'''
	Clase que administra todas las clases que crean ventanas y contiene el notebook que utiliza todas 
	las calles importadas, ademas que la clase manager crea la ventana principal de la app
'''

class Manager(ttk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.create_widgets()
		self.configure_win()
		self.configure_self()
		self.pack(expand=True, fill=tk.BOTH)

	def create_widgets(self):
		# Top bar
		# self.menu_bar = Menu_bar(self.master)

		# Windows
		self.navbar = Navbar(self, bg=config.BACKGROUND_SECONDARY)
		self.table = Table(self)
		self.notebook =  Notebook(self)
		self.notification_bar = Notification(self, bg='#2979ae')

	def configure_win(self):
		"""Main window setting"""
		self.master.geometry('1000x500')
		self.master.title('Sistema Inventario')

	def configure_self(self):
		"""Configuration of the upper menu, so that it is expandible"""
		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, minsize=55)
		self.rowconfigure(1, weight=1)
		self.rowconfigure(2, minsize=20)