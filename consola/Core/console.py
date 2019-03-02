# -*- coding: utf-* -*-

"""
[Versión 2.0]: 
     -Se le cambia el idioma de las funciones de español a ingles para
      que todo el programa sea coherente con las otras clase.
     -Se implementan funciones con la clase Arbol.
     -Mejor manejo de impresión de errores.
     -Creación de funciones extra para alivianar otras funciones con 
      la repetición de instrucciones
[Versión 2.5]:
    -Algunos cambios en base a prueba y error.
    -Reestructuración de algunas funciones y sus operaciones en base
     a recomendaciones dadas.
    -Trabajé esto en Windows y no en la maquina virtual asi que por eso
     hago este commit, para poder seguir trabajando en Ubuntu.
"""
from tempArbol import *

class Console:
	# Crea las variables seguirCorriendo y pone el primer directorio
	def __init__(self):
		self.keepRunning = True
		self.currentDirectory = "~"
		self.tree = Arbol()
		self.command = None
		self.value = None

	"""
       Setters y getters del directorio actual. Esto se pensó asi para que la función run
       sea más dinamica en cuanto a lo que se muestre en la consola.
    """
	def setCurrentDirectory(self, currentDirectory):
		self.currentDirectory = tree.getBranches() #Aun no está en su uso optimo

	def getCurrentDirectory(self):
		return self.currentDirectory

	"""
	   Esta es la función que se correrá desde main.py, no ocupa parametros y le agrega el
	   parametro a la función run()
	"""
	def start(self):
		self.run("~")

	"""
	   La consola siempre debe de ser llamada al final de cada función para que siga corriendo.
       Esta función revisa constantemente que el comando ingresado no sea 'exit'. Si un comando 
       es ingresado, este pasará a la función process()
     """
	def run(self, currentDirectory):
		while self.keepRunning:
			#self.currentDirectory = arbol.getAbsolutePath()
			command = raw_input("_H4ck3rM4n@NASA:%s$ " %(self.currentDirectory))

			if command == 'exit':
				self.keepRunning = False

			elif not command:
				self.keepRunning = True

			else:
				self.process(command)

	"""
	   process() obtiene el comando ingresado por el usuario, verifica si es un comando valido y 
	   procede a 'empaquetar' la instrucción junto con el valor(o parametro o path) para su debida
	   ejecución
	"""
	def process(self, command):

		self.commandParts = command.split(" ")

		#Lo ingresado por el usuario tiene mas de una palabra?
		if (len(commandParts) > 1):
			#¿Existe?
			if self.commandExists(self.commandParts[0]):
				#¿Es 'ls -l' con parametros o es 'rm -r' con parametros?
				if (len(commandParts) > 2) and (((commandParts[1] == "-l") or (commandParts[1] == "-r"))):
					self.command = commandParts[0] + " " + commandParts[1]
					self.value = commandParts[2]

				#¿Es 'ls -l' sin parametros?
				elif (len(commandParts) == 2) and (commandParts[1] == "-l"):
					self.command = commandParts[0] + " " + commandParts[1]
					self.execute(command)

				#¿Es 'rm -r' y no tiene parametros? Entonces tirar error.
				elif (len(commandParts) == 2) and (commandParts[1] == "-r"):
					self.printException("rm -r no param")#Se necesita un parametro y se le indica al usuario

				#Si existe el comando y no son los otros casos, pasa a ejecución
				else:
					self.command = commandParts[0]
					self.value = commandParts[1]
					self.execute(self.command, self.value)

			#Si no existe el comando se le indica al usuario
			else:
				printException(self.commandParts[0], "Inexistente")

		#Si lo dado por el usuario es solamente un comando, se verifica que existe y se ejecuta
		else:
			if self.commandExists(self.commandParts[0]):
				self.execute(command)

			else:
				self.printException(command, "Inexistente")

	def execute(self, command, value = None):
		self.value = value

	"""
	   printException() recibe el comando (si este no existe incluso) y el tipo de error.
	   al encontrar el caso especifico, se le da un mensaje especifico al error, simulando
	   una terminal de Linux
	"""
	def printException(self, command, exception):
		#Aun en construcción
		if (exception == "Inexistente"):
			print ("%s: comando no encontrado.")%(command)

		elif (exception == "rm -r no param"):
			print ("%s: operando restante. Ingrese parametros si desea utilizar rm -r.")%(command)

	"""
	   commandExists() revisa si el comando dado por el usuario es un comando existente
	   y disponible para su uso. Comandos existentes están ubicados en un arreglo para 
	   mayor conveniencia.
	"""
	def commandExists(self, command):
		existingCommands = ["pwd", "cd", "ls", "ls -l", "touch", "mkdir", "mv", "rm", "rm -r", "find"]

		for i in range (len(existingCommands)):

			if (existingCommands[i] == command):
				return True