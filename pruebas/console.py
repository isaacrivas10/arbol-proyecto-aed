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

[Versión 3.0]:
    -Completación de la función execute(), lista para ser implementada
     con clase arbol.
    -Adición de función exitMessage(), para dar un mensaje de salida.
     En esta se agregó un arreglo con diferentes mensajes de salida para 
     que no sea lo mismo.
    -Adición de mensaje de bienvenida al usuario.

[Versión 4.0]:
   -Continuación entre la función execute() y printExcept()
   -Se le cambia el nombre de printException() a printExcept()
   -Se le agregan bloques elif en verify() para compensar otros casos especiales
   -Faltan mas bloques en execute() y en printExcept()

[Versión 5.0]:
   -Cambios en algunas funciones y en el mensaje de bienvenida asimismo como el
    despedida.
   -Implementación completa de clase Arbol (exceptuando find)
   -Ciertas correcciones en base a pruebay error
"""
from tempArbol import *
import random

class Console:
	# Crea las variables seguirCorriendo y pone el primer directorio
	def __init__(self):
		self.tree = Arbol()
		self.keepRunning = True
		self.currentDirectory = self.tree.getRoot()
		self.command = None

	"""
       Setters y getters del directorio actual. Esto se pensó asi para que la función run
       sea más dinamica en cuanto a lo que se muestre en la consola.
    """
	def setCurrentDirectory(self):
		self.currentDirectory = self.tree.currentPath

	def getCurrentDirectory(self):
		return self.currentDirectory

	"""
	   Esta es la función que se correrá desde main.py, no ocupa parametros y viene con un
	   mensaje de bienvenida al usuario.
	"""
	def start(self):

		print("\n *************************Terminal de Linux************************\n")
		print("Integrantes del grupo: -Rosa Ávila (20161000265)")
		print("                       -Isaac Rivas (20181004937)")
		print("                       -Kevin Gerardo Bueno (20171000254)")
		print("                       -Josué Ariel Izaguirre (20171034157)")


		self.run()

	"""
	   La consola siempre debe de ser llamada al final de cada función para que siga corriendo.
       Esta función revisa constantemente que el comando ingresado no sea 'exit'. Si un comando 
       es ingresado, este pasará a la función process()
     """
	def run(self):
		while self.keepRunning:

			self.getCurrentDirectory()

			command = raw_input("\nH4ck3rM4n@NASA:%s$ " %(self.currentDirectory))

			if command == 'exit':
				self.keepRunning = False
				self.exitMessage()

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
		if (len(self.commandParts) > 1):
			#¿Existe?
			if self.commandExists(self.commandParts[0]):
				#¿Es 'ls -l' con parametros o es 'rm -r' con parametros?
				if (len(self.commandParts) > 2) and (((self.commandParts[1] == "-l") or (self.commandParts[1] == "-r"))):
					self.command = self.commandParts[0] + " " + self.commandParts[1]
					self.value = self.commandParts[2]

				#¿Es 'ls -l' sin parametros?
				elif (len(self.commandParts) == 2) and (self.commandParts[1] == "-l"):
					self.command = self.commandParts[0] + " " + self.commandParts[1]
					self.execute(command)

				#¿Es 'rm -r' y no tiene parametros? Entonces tirar error.
				elif (len(self.commandParts) == 2) and (self.commandParts[1] == "-r"):
					self.printExcept(command, "rm -r no param")#Se necesita un parametro y se le indica al usuario

				#¿Es mv y no agrega la direccion a la cual desea mover el objeto? Tirar Error siendo este el caso.
				elif (len(self.commandParts) == 2) and (self.commandParts[0] == "mv"):
					self.printExcept(self.commandParts[0], "mv no path", self.commandParts[1])

				elif (len(self.commandParts) == 3) and (self.commandParts[0] == "mv"):
					self.command = self.commandParts[0]
					self.value = self.commandParts[1] + self.commandParts[2]
					self.execute(self.command, self.value)

				#Si existe el comando y no son los otros casos, pasa a ejecución
				else:
					self.command = self.commandParts[0]
					self.value = self.commandParts[1]
					self.execute(self.command, self.value)

			#Si no existe el comando se le indica al usuario
			else:
				self.printExcept(self.commandParts[0], "Inexistente")

		#Si lo dado por el usuario es solamente un comando, se verifica que existe y se ejecuta
		elif (len(self.commandParts) == 1):
			if self.commandExists(self.commandParts[0]):
				self.command = self.commandParts[0]
				self.execute(command)

			else:
				self.printExcept(command, "Inexistente")

	"""
	   execute() puede o no puede recibir el parametro valor, esto depende del comando dado.
	   las funciones ya vienen "empaquetadas" por la funcion process(). Dependiendo del comando
	   que el usuario escribe, se revisará si los parametros son los indicados (si fueron dados)
	   y al final dará un mensaje de exito o de error para hacerle saber al usuario del estado
	   de su instrucción.
	"""
	def execute(self, command, value = None):

		if (self.command == "pwd"):
			print self.tree.currentPath

		elif (self.command == "cd"):
			#Si solo se escribe cd, se recurre a devolver al usuario a la raiz
			if value is None:
				self.currentDirectory = self.tree.getRoot()

			#Si no solo escribió cd, se procede a moverse al nodo deseado
			else:
				path = ""
				pathParts = value.split("/")
				moveV = pathParts[(len(pathParts))-1]
				
				if (len(pathParts) == 2):
					path = "/"

				elif(len(pathParts) > 2):
					for i in range (len(pathParts)-2):
						path = path + "/" + pathParts[i]

				"""
				Si el cambio se logró hacer, se le informa al usuario. Asimismo se 
				procede a cambiar el directorio que se muestra en la consola.
				"""
				if self.tree.moveToPosition(moveV, path):
					print ("Se ha cambiado de directorio exitosamente.")
					self.setCurrentDirectory()

					#De no lograrse el movimiento, se le informa al usuario.
				else:
					self.printExcept(command, "InvalidMovement", path)

		elif (self.command == "ls"):
			#De escribirse solamente ls, se procede sin parametros a llamar a la función
			if value is None:
				branchArray = self.tree.getBranches()

			#Ls con un valor, los parametros son enviados
			else:
				branchArray = self.tree.getBranches(value)

			path = " "

			#Se imprimen las ramas de manera horizontal
			for i in range (0, (len(branchArray))):
				path = path + " " + branchArray[i]

			print path

		elif (self.command == "ls -l"):
			if value is None:
				branchArray = self.tree.getBranches()

			else:
				branchArray = self.tree.getBranches(value)

			#Se procede a hace casi lo mismo que con ls, la unica diferencia es que se
			#enlista de manera vertical
			for i in range (0, (len(branchArray)-1)):
				print branchArray[i]

		elif (self.command == "touch"):
			self.tree.add(value, "-a")
			print ("Archivo %s exitosamente creado.")%(value)

		elif (self.command == "mkdir"):
			self.tree.add(value, "-c")
			print ("Carpeta %s exitosamente creada.")%(value)


		elif (self.command == "mv"):
			valueParts = value.split(" ")
			pathToMove = valueParts[0]
			where = valueParts[1]

			if self.tree.moveNodeTo(pathToMove, where):
				print ("%s: %s movido con exito al directorio: %s")%(command, pathToMove, where)

		elif (self.command == "rm") and (folderChecker(value) == False):
			if(self.tree.remove(value)):
				print("%s: %s borrado con exito.")%(command, value)
			else:
				self.printExcept(command, "rm -r no param")

		elif (self.command == "rm -r"):
			if(self.tree.remove(value)):
				print("%s: %s borrado con exito.")%(command, value)

			else:
				self.printExcept(command, "rm -r no param")

		elif (self.command == "find"):
			pass #sin consluir

	"""
	   printExcept() recibe el comando (si este no existe incluso) y el tipo de error.
	   al encontrar el caso especifico, se le da un mensaje especifico al error, simulando
	   una terminal de Linux
	"""
	def printExcept(self, command, exception, path = None):
		#Aun en construcción
		if (exception == "Inexistente"):
			print ("%s: comando no encontrado.")%(command)

		elif (exception == "rm -r no param"):
			print ("%s: operando restante. Ingrese parametros si desea utilizar rm -r.")%(command)

		elif (exception == "mv no path"):
			print ("%s: falta la ruta de destino del archivo '%s' ")%(command, path)

		elif (exception == "InvalidMovement"):
			print ("bash: %s: %s: no existe tal archivo o directorio")%(command, path)

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

	def exitMessage(self):
		messages = ["Fin de la Linea.",
		            "Terminando programa...", "Gracias por hackear con nosotros.",
		            "Guardando datos..."
		           ]

		n = (len(messages)-1)

		pick = random.randrange(n)

		print ("\n*\ %s \*\n\n")%(messages[pick])
