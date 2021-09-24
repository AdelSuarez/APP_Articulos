import tkinter as tk
from tkinter import messagebox
import sqlite3

def crear_conexion():
	'''
	Fucion que solo realiza la creacion de la base de tados
	'''
	try:
		conexion = sqlite3.connect('Articulos')
		cursor = conexion.cursor()

		cursor.execute('CREATE TABLE ARTICULOS (ID VARCHAR(5) UNIQUE, NOMBRE_ARTICULO VARCHAR(20), PRECIO INTEGER)')

		messagebox.showinfo('Conexion', "Lista de artículos creada con éxito")
	except:
		messagebox.showwarning("¡Atención!", "La lista ya exite")