
from temp import *


class Arbol:

	def __init__(self):
		# El constructor define la raiz de el directorio
		self.root = Node(Carpeta("/")) # Root es un nodo,contiene una carpeta adentro
		self.currentNode= self.root

	def getRoot(self):
		return self.root.getName()

	def add(self, addValue, _type):
		"""
			Objetivo: Agregar objetos

			Uso:
				add("nombre_del_archivo", *param)
				*param puede ser -c de carpeta o -a de archivo
		"""
		new= None
		if _type == "-c":
			new= Node(Carpeta(addValue)) # Se crea un nodo, seguidamente su valor como carpeta
		else:
			new= Node(Archivo(addValue))
		self.currentNode.getValue().add(new)

	def remove(self, remValue):
		b= self.searchInNode(self.root, remValue)
		if b != False:
			print b.getName()
		else:
			print False

	def moveTo(self, moveV, path):
		"""
			Tipos de movimiento:
				- Movimiento en si mismo: Nos direccionamos del nodo actual
					hacia abajo 
				- Moviemiento absoluto: Desplazamiento desde la raiz 

			Retorna True si el movimiento se realizo, de lo contrario False
		"""
		if moveV is self.currentNode.getName():
			return False

		checked= self.checkPath(path)
		if checked[0] == "relative":
			if checked[1] == self.currentNode.getName():				
				temp= self.searchInNode(self.currentNode, moveV)
				if temp != False:
					if temp.type() == "Carpeta":
						self.currentNode= temp
						return True
					else:
						return False
		elif checked[0] == "absolute":
			# Buscamos el valor que esta dentro de root
			if len(checked) > 1: # Una o mas carpetas despues de root
				temp = self.searchInNode(self.root, checked[2])
				for i in range(2, len(checked)):
					if temp is not False:
						temp= self.searchInNode(temp, checked[i])
				if temp is not False:
					if temp.type() is "Carpeta":
						self.currentNode = temp
						return True
					else:
						return False
				else:
					return False
			elif len(checked) is 1: 
				temp = self.searchInNode(self.root, moveV)
				if temp is not False:
					if temp.type() is "Carpeta":
						self.currentNode = temp
						return True
					else:
						return False
				else:
					return False
		else: # Si recibe algun error (?)
			return False

	def checkPath(self, path):
		# Uso: /path/to/move <-- respetar / al incio
		try:
			pathCheck= path.split("/")
			if path[0] == "/":
				return ["absolute"] + [i for i in pathCheck if i != ""]
			elif any("/" for s in path):
				return ["relative"] + [i for i in pathCheck if i != ""]
			else:
				#return ["error", 1] # 1 = error
				pass
		except:
			return ["error", 1] # 1 = error

	def getBranches(self):
		# Retorna todas las ramas relativas al nodo actual
		# En forma de array para mas comodidad
		b= self.currentNode.getValue().branches
		b_len= b.len()
		b_node= b.first
		b_listed= []
		if b_len > 0:
			if self.currentNode is self.root:
				for k in range(b_len):
					stack = "/%s" % (b_node.getName())
					b_listed.append(stack)
					b_node= b_node.getNext()
				return b_listed
			else:
				for i in range(b_len):
					stack ="%s/%s" % (self.currentNode.getName(),b_node.getName())
					b_listed.append(stack)
					b_node= b_node.getNext()
				return b_listed
		else:
			#b_listed.append("%s/" % (self.currentNode.getName()))
			return b_listed

	def searchInNode(self, current, value):
		# Solo busca en un nodo especifico
		# current  es un nodo, necesitamos trabajar con el valor
		# que contiene
		if current.getValue().branches.len() > 0: # Si tiene hijos
			node = current.getValue().branches.first
			for i in range(current.getValue().branches.len()): # Para cada nodo en sus ramas
				if node.getName() == value: # Si su nombre es igual a lo que busco
					return node # Retorno el nodo encontrado
				else:
					node= node.getNext()
			return False # Si tiene hijos pero su carpeta no se encontro
		else:
			return False # Si no tiene hijos, no hay donde buscar

	def searchInPath(self, path, value):

		self.checkPath(path)

	
	def getCurrentNode(self):
		return self.currentNode


# Crea una instancia del arbol
arbol = Arbol()
arbol.add("carpeta", "-c") # /carpeta/
arbol.add("node", "-c") # /node/
arbol.add("archivo", "-a") # /archivo

print arbol.moveTo("carpeta", "/")

arbol.add("carpeta1", "-c")
print arbol.currentNode.getValue().branches.len()
print arbol.getBranches()



