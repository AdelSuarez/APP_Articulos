from conexion.conexion import conexion
import tkinter as tk
from tkinter import messagebox
from constantes import style

def borrar_articulo(codigo, mensaje, nombre, precio):
	'''
	Funcion que realiza primero la verificaion si hay caracteres en el entry, luego verifica
	si se encuentra el codigo en la base de datos, y por ultimo borra el articulo de la base
	de datos
	'''
	if len(codigo.get()) != 0:
		query = 'SELECT * FROM ARTICULOS WHERE ID=?'
		serial_sin_espacios = (codigo.get()).strip()
		parameter = (serial_sin_espacios, )
		articulo = conexion(query, parameter).fetchall()

		if (articulo == []):
			mensaje['fg'] = style.MENSAJE_FALLA
			mensaje['text'] = '¡El código no éxiste!'

		else:
			for i in articulo:
				nombre.set(i[1])
				precio.set(i[2])	
			valor = messagebox.askquestion('Borrar artículo', 'Deseas borrar le artículo')

			if valor == 'yes':
				query = 'DELETE FROM ARTICULOS WHERE ID = ?'
				serial_sin_espacios = (codigo.get()).strip()
				parameter = (serial_sin_espacios, )
				conexion(query, parameter)
				codigo.delete(0, tk.END)
				mensaje['fg'] = style.MENSAJE_APROBADO
				mensaje['text'] = '¡Artículo borrado con éxito!'
				nombre.set('')
				precio.set('')

	else:
		mensaje['fg'] = style.MENSAJE_FALLA
		mensaje['text'] = '¡El código es requerido!'


