from conexion.conexion import conexion
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constantes import style
from conexion.lista_completa import listado_completo 



class Lista_articulos(ttk.Frame):
	def __init__(self, *args, **kwargs):
		super().__init__( *args, **kwargs)

		self.frame_lista = tk.Frame(self)
		self.frame_lista.config(bg=style.BACKGROUND)
		self.frame_lista.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		ttk.Button(self.frame_lista, text='Actualizar lista', command=lambda:listado_completo(self.lista)).grid(row=1, column=0, columnspan=2, pady=4)

		self.lista = tk.Text(self.frame_lista, width=65, height=20)
		self.lista.grid(row=2, column=1, pady=10)
		self.scroll = tk.Scrollbar(self.frame_lista, command=self.lista.yview)
		self.scroll.grid(row=2, column=2, sticky=tk.NSEW)
		self.lista.config(yscrollcommand=self.scroll.set)

