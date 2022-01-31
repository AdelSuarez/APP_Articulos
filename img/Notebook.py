import tkinter as tk
from tkinter import ttk


from components.Win_create import Win_create
from components.Win_delete import Win_delete
from components.Win_edit import Win_edit
from components.Win_list import Win_list
from components.Win_query import Win_query

class Notebook(ttk.Frame):
    def __init__(self,*args, **kwargs):
        super(Notebook, self).__init__(*args, **kwargs)
        self.grid(row=1, column=1, sticky=tk.NSEW)
        self.notebook()

    def notebook(self):
        self.note = ttk.Notebook(self)
        
        self.create = Win_create(self.note)
        self.query = Win_query(self.note)
        self.list = Win_list(self.note)
        self.delete = Win_delete(self. note)
        self.edit = Win_edit(self.note)

        self.note.add(self.create, text='Crear', padding=20)
        self.note.add(self.query, text='Consulta')
        self.note.add(self.delete, text='borrar')
        # self.note.add(self.edit, text='Modificar')

        self.note.grid(row=0, column=0, pady=10, padx=10)

        self.return_button = tk.Button(self, text='volver')
        self.return_button.grid(row=1, column=0, sticky=tk.E, padx=10)