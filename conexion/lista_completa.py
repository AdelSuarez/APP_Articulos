from conexion.conexion import conexion
import tkinter as tk

def listado_completo(lista):
	'''
	Funcion que inserta todos los articulos de la base de datos en el tk.text, para
	visualizar todos los articulos de la base de datos 
	'''
	lista.config(state=tk.NORMAL)
	query = 'SELECT * FROM ARTICULOS'
	resultado = conexion(query).fetchall()
	lista.delete(1.0, tk.END)
	for codigo, nombre, precio in resultado:
		lista.insert(1.0, 'CÓDIGO: {} | Descripción: {} -- Precio: {} $\n'.format(codigo, nombre, precio))

	lista.config(state=tk.DISABLED)
