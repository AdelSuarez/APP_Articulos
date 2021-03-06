import tkinter as tk

import tkinter.messagebox
from setting import config


class Navbar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self._master= master
        self.grid(row=0, column=0, sticky=tk.NSEW, columnspan=2)

        self.title = tk.Label(self, text="SISTEMA DE INVENTARIO", **config.TITLE_CONFIG)
        self.title.pack(side=tk.LEFT, padx=5)

        self.info = tk.Button(self, text='INFO', relief=tk.FLAT, overrelief=tk.RAISED, **config.BUTTON_INFO, justify=tk.CENTER)
        self.info.pack(side=tk.RIGHT, padx=10)