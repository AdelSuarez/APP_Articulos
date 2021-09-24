import tkinter as tk
from conexion.conexion import conexion
from constantes import style
import random



def serial():
	'''
	Funcion que crea una serial aleatorio, para indentificar de forma unica
	a los articulos creados
	'''
	serial = ('')

	for i in range(5):
		serial_random  = random.randint(0, 9)
		serial = serial + str(serial_random)

	for i in range(1):
		letra = random.choice('AEIOU')
		serial = serial + letra

		return(serial)



def validacion_campos(nombre, precio):
	'''
	Funcion que valida que el usuario no deje campos vacios 
	'''
	return len(nombre.get()) != 0 and len(precio.get()) != 0



def validacion_precio(precio, mensaje):
	'''
	Funcion que valida los caracteres introducidos en el Entry del precio
	verificando que no se halla introducido valores alfanumericos

	"Observacion: todavia falta pulir la funcions para que reciva valores float"
	'''
	try:
		return isinstance(int(precio.get()), int)
	except ValueError:
			mensaje['fg'] = style.MENSAJE_FALLA
			mensaje['text'] = '¡El precio no acepta letras!'



def articulo_creado(nombre, precio, mensaje):
	'''
	Funcion que introduce los datos dados por el usuario a la base de datos,
	en la cual se realizan las validacion anteriores, y muestra medainte mensajes,
	si a ocurrido un error o si el articulo se introdujo correctamente
	'''
	if validacion_campos(nombre, precio):
		if validacion_precio(precio, mensaje):
			query = 'INSERT INTO ARTICULOS VALUES(?,?,?)'
			parameters = (serial(), nombre.get(), precio.get())
			conexion(query, parameters)
			nombre.delete(0, tk.END)
			precio.delete(0, tk.END)
			mensaje['fg'] = style.MENSAJE_APROBADO
			mensaje['text'] = '¡Artículo cargado con éxito!'
	else:
		mensaje['fg'] = style.MENSAJE_FALLA
		mensaje['text'] = '¡Nombre y precio son requeridos!'