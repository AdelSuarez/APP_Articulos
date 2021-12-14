from conexion.conexion import conexion
from constantes import style
import tkinter as tk
from tkinter import messagebox
from conexion.crear_articulo import validacion_campos, validacion_precio

def verificacion_articulo(codigo, nombre, precio, mensaje, boton, entry_nombre, entry_precio):
	'''
	Funcion que verifica que el articulo exista, muestra el articulo que se va modificar, 
	y activa el los entry del nuevo nombre y precio y el boton para que se pueda modificar
	'''

	codigo_espacios = (codigo.get()).strip()

	if len(codigo_espacios) != 0:
		query = 'SELECT * FROM ARTICULOS WHERE ID=?'
		parameter = (codigo_espacios, )
		articulo = conexion(query, parameter).fetchall()
		if (articulo == []):
			mensaje['fg'] = style.MENSAJE_FALLA
			mensaje['text'] = '¡El código no éxiste!'
		else:
			for i in articulo:
				nombre.set(i[1])
				precio.set(i[2])	

			mensaje['fg'] = style.MENSAJE_APROBADO
			mensaje['text'] = '¡Consulta realizada con éxito!'
			boton['state'] = tk.NORMAL
			entry_nombre.config(state=tk.NORMAL)
			entry_precio.config(state=tk.NORMAL)

	else:
		mensaje['fg'] = style.MENSAJE_FALLA
		mensaje['text'] = 'El código es requerido'

def modificar_articulos(codigo, nombre, precio, nombre_nuevo, precio_nuevo, mensaje):
	'''
	'''
	if validacion_campos(nombre_nuevo, precio_nuevo):
		if validacion_precio(precio_nuevo, mensaje):
			valor = messagebox.askquestion('Modificar', 'Deseas modificar el artículo')
			if valor == 'yes':
				parameters = (nombre_nuevo.get(), precio_nuevo.get(), codigo.get())
				query = 'UPDATE ARTICULOS SET NOMBRE_ARTICULO = ?, PRECIO = ? WHERE ID = ?'
				conexion(query, parameters)
				nombre.set('')
				precio.set('')
				nombre_nuevo.delete(0, tk.END)
				precio_nuevo.delete(0, tk.END)
				codigo.delete(0, tk.END)
				nombre_nuevo.config(state='readonly')
				precio_nuevo.config(state='readonly')
				mensaje['fg'] = style.MENSAJE_APROBADO
				mensaje['text'] = '¡Artículo modificado!'

	else:
		mensaje['fg'] = style.MENSAJE_FALLA
		mensaje['text'] = '¡Nombre y precio son requeridos!'
