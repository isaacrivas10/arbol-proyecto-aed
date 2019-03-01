# -*- coding: utf-* -*-

"""
[Versión 2.0]: 
     -Se le cambia el idioma de las funciones de español a ingles para
      que todo el programa sea coherente con las otras clase.
     -Se implementan funciones con la clase Arbol.
     -Mejor manejo de impresión de errores.
     -Creaciñon de funciones extra para alivianar otras funciones con 
      la repetición de instrucciones
"""
from tempArbol import *

class Console:
	# Crea las variables seguirCorriendo y pone el primer directorio
	def __init__(self):
		self.keepRunning = True
		self.currentDirectory = "~"
		self.tree = Arbol()

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

		#¿Tiene el comando algun parametro?
		if ' ' in command:
			commandParts = command.split(" ")
			self.command = commandParts[0]

			#¿Existe?
			if self.commandExists(self.command):
				#¿Es 'ls -l' con parametros o es 'rm -r'?
				if (len(commandParts) > 2) and (((splittedCommand[1] == "-l") or (splittedCommand[1] == "-r"))):
					self.command = commandParts[0] + " " + commandParts[1]
					self.value = commandParts[2]

				#¿Es 'ls -l' sin parametros?
				elif (len(commandParts) == 2) and (splittedCommand[1] == "-l"):
					self.command = commandParts[0] + " " + commandParts[1]
					self.executeWithoutParameters(command)

				#¿Es 'rm -r' y no tiene parametros?
				elif (len(commandParts) == 2) and (splittedCommand[1] == "-r"):
					self.printException("rm -r no param")#Se necesita un parametro y se le indica al usuario

				else:
					self.value = commandParts[1]

			else:
				self.printException(command, "Inexistente")

		#Si no tiene parametro se ejecuta sin parametro (se dará error de ocuparse un parametro)
		else:
			if self.commandExists(command):
				self.executeWithoutParameters(command)
			else:
				self.printException(command, "Inexistente")

	"""
	   executeWithoutParameters() recibe el comando y si cumple con alguno de los casos dados
	   se procedera a llamar alguna función de arbol que haga lo pedido. Si no cumple se procede
	   a imprimir el error de que ocupa un parametro
	"""
	def executeWithoutParameters(self, command):

		currentDirectory = self.getCurrentDirectory()

		if (command == "pwd"):
			print self.tree.getBranches()

		elif (command == "ls"):
			pass

	def executeWithParameters(self, command, value):
		
		path = getCurrentDirectory

		if (command == touch):
			arbol.add(value, "-a")

		elif(command == mkdir):
			arbol.add(value, "-c")

	"""
	   printException() recibe el comando (si este no existe incluso) y el tipo de error.
	   al encontrar el caso especifico, se le da un mensaje especifico al erro, simulando
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
	   y disponible para su uso.
	"""
	def commandExists(self, command):
		existingCommands = ["pwd", "cd", "ls", "ls -l", "touch", "mkdir", "mv", "rm", "rm -r", "find"]

		for i in range (len(existingCommands)):

			if (existingCommands[i] == command):
				return True