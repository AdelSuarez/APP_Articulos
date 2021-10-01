import tkinter as tk
from tkinter import messagebox
from conexion.conexion import conexion
from os import remove

def cerrar_ap(ap):
	valor = messagebox.askquestion('Salir', 'Deseas salir de la aplicacion')
	if valor == 'yes':
		ap.destroy()

def acerca_de_funcion():
	messagebox.showinfo('Acerca de...', 'Version 1.1 | Desarrollado por Adel Suarez' )

def borrar_lista_completa():
	valor = messagebox.askquestion('Borrar lista', 'Deseas borrar la lista completa')
	if valor == 'yes':
		# query = 'DELETE FROM ARTICULOS'
		# conexion(query)
		remove('Articulos')

	
