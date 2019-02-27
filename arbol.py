# -*- coding: utf-* -*-

from nodes import *

class Arbol:

	def __init__(self):
		# El constructor define la raiz de el directorio
		self.root = Root("root")
		self.currentNode= self.root

	def getRoot(self):
		return self.root.getValue()

	def add(self, addValue):
		addValue.father= self.currentNode
		self.currentNode.add(addValue)

	def getBranches(self):
		# Retorna todas las ramas que siguen la raiz
		b= self.currentNode.branches
		if len(b) > 0:
			for branch in b:
				print "/%s/%s" % (self.currentNode.getValue(),branch.getValue())
		else:
			print "/%s/" % (self.currentNode.getValue())

	def searchInNode(self, current, carpeta):

		if len(current.branches) > 0: # Si tiene hijos
			for node in current.branches: # Para cada nodo en sus ramas
				if node.iAm == "carpeta": # Verifico si es una carpeta
					if node.getValue() == carpeta: # Si su nombre es igual a la carpeta que busco
						return node # Retorno el nodo encontrado
				# De primeras si no es una carpeta se descarta
			return False # Si tiene hijos pero su carpeta no se encontro
		else:
			return False # Si no tiene hijos, no hay donde buscar

	def moveTo(self, *params):
		"""
			Solamente puede haber movimiento entre nodos de arriba a abajo
		"""
		current = self.currentNode
		executedParams= list(params)
		if len(executedParams) == 0:
			print "Sin parametros"
			pass
		else:
			if executedParams[0] != "..":
				r= self.searchInNode(current, executedParams[0])
				if r is False:
					print "La carpeta no existe en este directorio"
				else:
					self.currentNode= r
			else:
				if current.getValue() == "root":
					print "raiz"
				else:
					self.currentNode= current.father

	def getCurrentNode(self):
		return self.currentNode

# Crea una instancia del arbol
arbol = Arbol()

# Crea un archivo y una carpeta
ar= Archivo("hola")
#ar2= Archivo("hola")
ca= Carpeta("pruebaCarpeta")
ca2= Carpeta("esta es una carpeta")

#Retorna el contenido en la raiz
#arbol.getBranches()



arbol.add(ca) # Agrego carpeta al arbol
arbol.add(ar) # Agrego archivo al arbol
arbol.moveTo("pruebaCarpeta") # Me muevo a esta carpeta
arbol.add(ca2) # Agrego carpeta al arbol
arbol.moveTo("esta es una carpeta") # Me muevo a esta carpeta
arbol.moveTo("..") # Me muevo una posicion arriba del arbol
arbol.getBranches() # Imprimo las cosas dentro del directorio actual
print arbol.getCurrentNode().value # Retorno el nombre de la carpeta