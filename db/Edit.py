from tkinter import messagebox
from db.Connection import DataBase
from setting import config
from db.Create import Create
import tkinter as tk
from tkinter import messagebox

class Edit():
    def __init__(self, serial, name, price, new_name, new_price, message):
        self._serial = serial
        self._name = name
        self._price = price
        self._new_name = new_name
        self._new_price = new_price
        self._message = message
        self.edit_item()

    def edit_item(self):
        if Create.field_validation(self, self._new_name, self._new_price):
            if Create.price_validation(self, self._new_price):
                value = messagebox.askquestion('Modificar', 'Deseas modificar el artículo')
                if value == 'yes':
                    query = 'UPDATE ARTICULOS SET NOMBRE_ARTICULO = ?, PRECIO = ? WHERE ID = ?'
                    parameters = (self._new_name.get(), self._new_price.get(), self._serial.get())
                    DataBase(query, parameters)
                    print(DataBase)
                    self._name.set('')
                    self._price.set('')
                    self._new_name.delete(0, tk.END)
                    self._new_price.delete(0, tk.END)
                    self._serial.delete(0, tk.END)
                    self._new_name.config(state = 'readonly')
                    self._new_price.config(state = 'readonly')
                    self._message['fg'] = config.READY
                    self._message['text'] = '¡Artículo modificado!'
                    
        else:
            self._message['fg'] = config.WARNINGS
            self._message['text'] = '¡Nombre y precio son requeridos!'