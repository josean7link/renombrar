#!/usr/bin/env python3
#Programa para renombrar archivos, intuitivo usando las mismas funciones
#de buscar y reemplazar de editores de textos abituales.

print("Programa para Buscar y Reemplazar partes en los nombres de archivos.")
def renombrar(parte_a_buscar, parte_a_reemplazar):
	import os
	path=os.getcwd()
	filenames=os.listdir(path)

	parte_a_buscar=input("Introduce parte a buscar: ")
	parte_a_reemplazar=input("Introduce parte a reemplazar: ")

	for filename in filenames:
		os.rename(filename, filename.replace(str(parte_a_buscar), str(parte_a_reemplazar)))
#	repetir(funcion, *args)

def repetir(funcion, *args):
	opcion=input("Marque Si para continuar, No para terminar: ")
	seguir=opcion.lower()

	if seguir in ("si", "si "):
		print("Continuando...")
		lista_parametros=[]
		i=0
		for i in args:
			lista_parametros.append(i)
			i=+1
		parametros=tuple(lista_parametros)
		funcion(*parametros)
		repetir(funcion, *args)

	elif seguir in ("no", "no "):
		print("Terminado.")

	else:
		print("Por favor, intentelo otra vez.")
		repetir(funcion, *args)

#-----------------------------------------------------------------------------------------------#
#			Para renombrar una vez los archivos, pasar la siguiente funcion:					#
#-----------------------------------------------------------------------------------------------#
#renombrar("", "")
#-----------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------#
#			Para renombrar varias veces los archivos, pasar la siguiente funcion:				#
#-----------------------------------------------------------------------------------------------#
#repetir(renombrar, "", "")
#-----------------------------------------------------------------------------------------------#