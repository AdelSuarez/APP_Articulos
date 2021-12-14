from db.Connection import DataBase
from setting import config
import tkinter as tk


class Edit_query():
    def __init__(self, serial, name, price, message, button, entry_name, entry_price):
        self._serial = serial
        self._name = name
        self._price = price
        self._message = message
        self._button = button
        self._entry_name = entry_name
        self._entry_price = entry_price
        self.check_item()

    def check_item(self):
        serial_space = (self._serial.get()).strip()

        if len(serial_space) != 0:
            query = 'SELECT * FROM ARTICULOS WHERE ID=?'
            parameters = (serial_space, )
            articles = DataBase(query, parameters).fetchall()
            print(articles)
            if articles != []:
                for i in articles:
                    self._name.set(i[1])
                    self._price.set(i[2])

                self._button['state'] = tk.NORMAL
                self._entry_name.config(state = tk.NORMAL)
                self._entry_price.config(state = tk.NORMAL)
                self._message['fg'] = config.READY
                self._message['text'] = '¡Consulta realizada con éxito!'
            
            else:
                self._message['fg'] = config.WARNINGS
                self._message['text']='¡El código no éxiste!'
        
        else:
            self._message['fg'] = config.WARNINGS
            self._message['text'] = 'El código es requerido'





    

