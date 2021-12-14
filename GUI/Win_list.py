from conexion.conexion import conexion
import tkinter as tk
from tkinter import ttk
from setting import config
from db.List import List


class Win_list(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__( *args, **kwargs)

		self.frame_list = tk.Frame(self)
		self.frame_list.config(bg=config.BACKGROUND)
		self.frame_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		ttk.Button(self.frame_list, text='Actualizar lista', command=lambda:List(self.list,self.message)).grid(row=1, column=0, columnspan=2, pady=4)

		self.message = tk.Label(self.frame_list, text='', bg=config.BACKGROUND)
		self.message.grid(row=3, column=0, columnspan=2, pady=6)

		self.list = tk.Text(self.frame_list, width=65, height=20)
		self.list.grid(row=2, column=1, pady=10)
		self.scroll = tk.Scrollbar(self.frame_list, command=self.list.yview)
		self.scroll.grid(row=2, column=2, sticky=tk.NSEW)
		self.list.config(yscrollcommand=self.scroll.set)

