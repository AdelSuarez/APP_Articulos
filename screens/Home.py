import tkinter as tk
from tkinter import ttk
from components.Win_create import Win_create
from components.Win_delete import Win_delete
from components.Win_edit import Win_edit
from components.Win_list import Win_list
from components.Win_query import Win_query



class HomeScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self._manager = manager
        self.grid(row=1, column=0, sticky=tk.NSEW)
        self.controllers()
        self.create_table()
        self.create_controller()


    def create_table(self):
        self.table = ttk.Treeview(self, columns=('name', 'price', 'stock'), padding=[0,0,0,0])
        self.table.column('#0', stretch=0, width=80, anchor=tk.W)
        self.table.heading('#0', text='ID')
        self.table.column('name', width=300, anchor=tk.W)
        self.table.heading('name', text='Producto')
        self.table.column('price', stretch=0, width=80, anchor=tk.CENTER)
        self.table.heading('price', text='Precio')
        self.table.column('stock', stretch=0, width=70, anchor=tk.CENTER)
        self.table.heading('stock', text='Existencia')
        self.table.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)


    def create_controller(self):
        self.controller = tk.Frame(self, bg='red')
        # self.controller.columnconfigure(1, minsize=170)
        # self.controller.rowconfigure(1, minsize=170)
        self.controller.columnconfigure(0, weight=1)
        self.controller.rowconfigure(4, weight=1)

        self.note = ttk.Notebook(self.controller)
        
        self.create = Win_create(self.note)
        self.query = Win_query(self.note)
        self.list = Win_list(self.note)
        self.delete = Win_delete(self. note)
        self.edit = Win_edit(self.note)

        self.note.add(self.create, text='Crear', padding=20)
        self.note.add(self.query, text='Consulta')
        self.note.add(self.delete, text='borrar')
        # self.note.add(self.edit, text='Modificar')

        self.note.grid(row=0, column=0, columnspan=2)

        self.return_button = tk.Button(self.controller, text='crear', command=lambda:self._manager.home_to_create())
        self.return_button.grid(row=1, column=1, sticky=tk.E)

        self.controller.grid(column=1, row=0, sticky='nsew', pady=10, padx=10)


    
    def controllers(self):
        self.grid(row=1, column=0, sticky=tk.NSEW)
        # self.columnconfigure(1, weight=1)
        self.columnconfigure(0, weight=1, minsize=600)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, weight=1)
        self.rowconfigure(0, weight=1)
        