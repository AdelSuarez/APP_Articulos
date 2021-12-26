from db.Connection import DataBase
import sqlite3 as sql



class Table():
    def __init__(self, table):
        self._table = table

    def item_table(self):
        try:
            query = 'SELECT * FROM ARTICULOS'
            articles = DataBase(query, )

            for serial, name, price in articles:
                item = self._table.insert("", text=f'{serial}', values=(f'{name}', f'{price}'))
                self._table.set(item)

        except sql.OperationalError:
            print('Error')



    # def complete_list(self):
    #     try:
    #         query = 'SELECT * FROM ARTICULOS'
    #         articles = DataBase(query, ).fetchall()
    #         print(articles)
    #         for serial, name, price in articles:
    #             item = self._table.insert("", text=f'{serial}', values=(f'{name}', f'{price}'))
    #             self._list.insert(1.0, f'CÓDIGO: {serial} | Descripción: {name} -- Precio: {price} $\n')

    #     self._message['text'] = ''

    #     except sql.OperationalError:
    #     	self._message['fg'] = config.WARNINGS
    #     	self._message['text'] = 'No se a conectado a la base de datos'

	# 	self._list.config(state = tk.DISABLED)	