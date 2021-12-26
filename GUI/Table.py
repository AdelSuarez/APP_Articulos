from db.Connection import DataBase
import tkinter as tk
from tkinter import ttk
import sqlite3 as sql

class Table(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)
        self.grid(row=1, column=0, sticky=tk.NSEW)
        self.configure_win()
        self.table()

    
    def table(self):
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
        
        self.item_table()

    def configure_win(self):
        """Table setting to expand horizontally and vertically"""
        self.columnconfigure(0, weight=1) #Horizontally
        self.rowconfigure(0, weight=1) #Vertically
        # self.columnconfigure(0, minsize=100)

    def item_table(self):
        try:
            query = 'SELECT * FROM ARTICULOS'
            articles = DataBase(query, ).fetchall()

            for serial, name, price in articles:
                item = self.table.insert("", tk.END, text=f'{serial}', values=(f'{name}', f'{price}'))
                self.table.set(item)

        except sql.OperationalError:
            print('Error')
