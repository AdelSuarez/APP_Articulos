from conexion.conexion import conexion
from constantes import style

def consultar_articulo(codigo, nombre, precio, mensaje):
	'''
	Funcion que realiza la consulta a la base de datos, en la cual realiza en el entry del codigo
	realiza la verificacion si el usuario a introducido el respectivo codigo y si dicho codigo 
	existe en la base de datos
	'''
	if len(codigo.get()) != 0:
		query = 'SELECT * FROM ARTICULOS WHERE ID=?'
		serial_sin_espacios = (codigo.get()).strip()
		parameter = (serial_sin_espacios, )
		articulo = conexion(query, parameter).fetchall()
		if (articulo == []):
			nombre.set('')
			precio.set('')
			mensaje['fg'] = style.MENSAJE_FALLA
			mensaje['text'] = '¡El código no éxiste!'
		else: 
			for i in articulo:
				nombre.set(i[1])
				precio.set(i[2])	

			mensaje['fg'] = style.MENSAJE_APROBADO
			mensaje['text'] = '¡Consulta realizada con éxito!'

	else:
		nombre.set('')
		precio.set('')
		mensaje['fg'] = style.MENSAJE_FALLA
		mensaje['text'] = '¡El código es requerido!'