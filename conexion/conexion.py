import sqlite3

def conexion(query, parameter = ()):
	'''
	Funcion principal para realizar las diversas operaciones con la base de datos, en la cual
	recibe como argumentos, la query a realizar y los parametros que que se van a utilizar segun 
	la canculta que se realizara a la base de datos
	'''
	conexion = sqlite3.connect('Articulos')
	cursor = conexion.cursor()
	resultado = cursor.execute(query, parameter)
	conexion.commit()

	return resultado