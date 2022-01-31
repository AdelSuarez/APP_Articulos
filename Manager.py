import tkinter as tk
from setting import config
from screens.NavBar import Navbar
# from components.Table import Table
# from components.Notebook import Notebook
from screens.Notification_bar import Notification
from screens.Home import HomeScreen
from screens.Create import Create_screen

class Manager(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.container = tk.Frame(self.master)
		# self.create_widgets()
		self.configure_win()
		self.configure_self()
		self.container.pack(expand=True, fill=tk.BOTH)

		self.navbar = Navbar(self.container, bg=config.BACKGROUND_SECONDARY)
		self.notification_bar = Notification(self.container, bg='#2979ae')

		self.frames = {}
		screens = (HomeScreen, Create_screen, )
		for f in screens:
			frame = f(self.container, self)
			self.frames[f] = frame
			frame.grid(row=1, column=0, sticky=tk.NSEW)

		self.show_frame(HomeScreen)

	def show_frame(self, container):
		frame = self.frames[container]
		frame.tkraise()

	def home_to_create(self):
		self.show_frame(Create_screen)

	def create_to_home(self):
		self.show_frame(HomeScreen)

	def configure_win(self):
		"""Main window setting"""
		self.master.geometry('1000x500')
		self.master.title('Sistema Inventario')

	def configure_self(self):
		"""Configuration of the upper menu, so that it is expandible"""
		self.container.columnconfigure(0, weight=1)
		self.container.rowconfigure(0, minsize=55)
		self.container.rowconfigure(1, weight=1)
		self.container.rowconfigure(2, minsize=20)