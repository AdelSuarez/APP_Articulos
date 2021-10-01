from conexion.conexion import conexion
import tkinter as tk
import sqlite3
from constantes import style
from os import remove

def listado_completo(lista, mensaje):
	'''
	Funcion que inserta todos los articulos de la base de datos en el tk.text, para
	visualizar todos los articulos de la base de datos 
	'''
	lista.config(state=tk.NORMAL)
	query = 'SELECT * FROM ARTICULOS'
	try: 
		articulos = conexion(query).fetchall()
		lista.delete(1.0, tk.END)
		for codigo, nombre, precio in articulos:
			lista.insert(1.0, 'CÓDIGO: {} | Descripción: {} -- Precio: {} $\n'.format(codigo, nombre, precio))
		mensaje['text'] = ''
	except sqlite3.OperationalError:
		mensaje['fg'] = style.MENSAJE_FALLA
		mensaje['text'] = 'No se a conectado a la base de datos'


	lista.config(state=tk.DISABLED)
