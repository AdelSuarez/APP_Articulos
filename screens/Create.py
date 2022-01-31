import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style


class Create_screen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent, manager)
        self._manager = manager
        self.grid(row=1, column=0, sticky=tk.NSEW)
        self.configure_win()
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = tk.Frame(self)
        self.header.columnconfigure(1, weight=1)

        tk.Button(self.header, text='Volver', command=lambda:self._manager.create_to_home()).grid(row=0, column=0, pady=10, padx=10, sticky=tk.W)
        tk.Label(self.header, text='NUEVO ARTICULO', font='Oswald 12 bold').grid(row=0, column=1, sticky=tk.EW, columnspan=2)

        self.header.grid(row=0, column=0, sticky=tk.NSEW)

        # Controllers
        self.controller = tk.Frame(self)

        tk.Label(self.controller, text='Articulo:').grid(row=0, column=0, sticky=tk.W)
        self.name_entry = ttk.Entry(self.controller)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.controller, text='Precio cliente:').grid(row=1, column=0, sticky=tk.W)
        self.price_entry = ttk.Entry(self.controller)
        self.price_entry.grid(row=1, column=1)

        tk.Label(self.controller, text='Precio base:').grid(row=2, column=0, sticky=tk.W)
        self.base_price = ttk.Entry(self.controller)
        self.base_price.grid(row=2, column=1)
        self.controller.grid(row=1, column=0, sticky=tk.NSEW)

    def configure_win(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        # self.rowconfigure(0, weight=1)


