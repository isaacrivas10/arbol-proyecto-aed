
from temp import *


"""
Cambios a realizar hoy
Poder retornar direccion absoluta del nodo actual - NO COMPLETADO
Poder retonrar direccion abosoluta desde el nodo actual hasta el final - NO COMPLETADO
ejemplo: find sin parametros
"""

class Arbol:

	def __init__(self):
		# El constructor define la raiz de el directorio
		self.root = Node(Carpeta("/")) # Root es un nodo,contiene una carpeta adentro
		self.currentNode= self.root
		self.currentPath= self.getRoot()

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

	def remove(self, remValue, _positionNode=None):
		if _positionNode is not None:
			deleteNode=  _positionNode
		else:
			deleteNode= self.currentNode
		b= self.searchInNode(deleteNode, remValue)
		
		if b != False:
			deleteNode.getValue().remove(b)
			return True
		else:
			return False

	def moveNodeTo(self, pathToMove, where):
		where= self.checkPath(where)
		pathToMove= self.checkPath(pathToMove)
		
		if len(pathToMove) < 2: # Si la direccion no tiene al menos una carpeta
			return False

		# Primero trato de ubicarme donde quiero moverme
		# Si me quiero mover a un lugar que no existe, error
		if where[0] is "absolute":
			if len(where) > 1:
				tempWhere= self.walk(self.root, where[1:])
				if tempWhere is not False:
					if self.folderChecker(tempWhere) is False:
						return False
				else:
					return tempWhere
			else:
				tempWhere= self.root
		elif where[0] is "relative":
			tempWhere= self.walk(self.currentNode, where[1:])
			if tempWhere is not False:
				if self.folderChecker(tempWhere) is False:
					return False
			else:
				return tempWhere
		
		# Luego ubico que quiero mover
		# Si quiero mover algo que no existe, error
		if pathToMove[0] is "absolute":
			tempToMove= self.walk(self.root, pathToMove[1:])

			if tempToMove is not False:
				if len(pathToMove) is 2:
					deleteFrom= self.root
				else:
					deleteFrom= self.walk(self.root, pathToMove[1:-1])
			else:
				return tempToMove
		elif pathToMove[0] is "relative":
			tempToMove= self.walk(self.currentNode, pathToMove[1:])

			if tempToMove is not False:
				deleteFrom= self.walk(self.currentNode, pathToMove[1:-1])
			else:
				return tempToMove
		
		# Si llega hasta aqui significa que paso ambas pruebas
		destinationBranch= tempWhere.getValue().branches

		#	Pasos
		#	1. Obtengo el primero de los children en el destino
		#	2. Identifico al ultimo
		#	3. Posiciono el nodo en el final, el sig es None
		#	4. Lo elimino de donde vino			
		#

		tempNode= destinationBranch.first

		if tempNode is not None:
			for i in range(destinationBranch.len()): #1
				before= tempNode #2
				if tempNode is not None:
					tempNode= tempNode.getNext()

			before.setNext(Node(Carpeta(tempToMove.getName())))#3
			if self.folderChecker(tempToMove):
				before.getNext().branches = tempToMove.getValue().branches
		else:
			destinationBranch.first= Node(Carpeta(tempToMove.getName()))
			if self.folderChecker(tempToMove):
				destinationBranch.first.branches= tempToMove.getValue().branches
		
		self.remove(tempToMove.getName(), deleteFrom) #4

	def moveToPosition(self, moveV, path):
		"""
			Tipos de movimiento:
				- Movimiento en si mismo: Nos direccionamos del nodo actual
					hacia abajo 
				- Moviemiento absoluto: Desplazamiento desde la raiz 

			Retorna True si el movimiento se realizo, de lo contrario False

			El codigo esta demasiado largo y complicado, se me ocurrio una idea
			mas facil hasta el final pero no la hare, no hay tiempo.
		"""
		if moveV is self.currentNode.getName() and moveV != "/":
			return False

		checked= self.checkPath(path)
		if checked[0] == "relative":
			if checked[1] == self.currentNode.getName():
				temp= self.searchInNode(self.currentNode, moveV)
				if temp != False:
					self.currentPath= "%s/%s" % (self.currentPath, moveV)
					return self.folderChecker(temp, True)
				else:
					return False
			else:
				return False

		elif checked[0] == "absolute":
			# Buscamos el valor que esta dentro de root
			if len(checked) > 1: # Una o mas carpetas despues de root
				temp= self.walk(self.root, checked[1:])
				# Si llego hasta aqui es por que el path ingresado es correcto
				if temp is not False:# Verifico ahora su el moveV existe
					moveDir= self.searchInNode(temp, moveV)
					if moveDir is not False:
						self.currentPath= "%s/%s" % (path, moveV)
						return self.folderChecker(moveDir, True)
					else:
						return False
				else:
					return False
			elif len(checked) is 1:
				if moveV is "/" :
					self.currentPath= self.getRoot()
					self.currentNode= self.root
					return True
				else:
					temp = self.searchInNode(self.root, moveV)
					if temp is not False:
						self.currentPath= "/%s" % (moveV)
						return self.folderChecker(temp, True)
					else:
						return False
		else: # Si recibe algun error (?)
			return False

	def checkPath(self, path):
		"""
			Se encarga de tomar un string que sera interpretado como
			un path, este lo divide en sus secciones y retorna un arreglo
			en orden de nivel con el nombre de los directorios.
			Verifica si es un absolute o relative path.
			Sin recursividad

			Ejemplo:
				[in] path = /path/to/move
				[out] = ['absolute', 'path', 'to', 'move']

				[in] path = path/to/move
				[out] = ['relative', 'path', 'to', 'move']
		"""
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

	def getBranches(self, _node=None, _getNodes=False):
		# Retorna todas las ramas relativas al nodo actual
		# En forma de array para mas comodidad
		
		if _node is None:
			_node= self.currentNode

		b= _node.getValue().branches
		b_len= b.len()
		b_node= b.first
		b_listed= [[],[]]
		if b_len > 0:
			if _node is self.root:
				for k in range(b_len):
					stack = "/%s" % (b_node.getName())
					b_listed[0].append(stack)
					b_listed[1].append(b_node)
					b_node= b_node.getNext()
			else:
				for o in range(b_len):
					stack ="./%s" % (b_node.getName())
					b_listed[0].append(stack)
					b_node= b_node.getNext()
			if _getNodes is not False:
				return b_listed
			else:
				return b_listed[0]
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

	
	def getCurrentNodeValueName(self):
		return self.currentNode.getName()

	def walk(self, node, value):
		# Nos movemos entre un arreglo de valores comenzando en un nodo
		# Hasta que el valor se encuentre, retorna o el nodo que se busca 
		# value[-1] o False
		temp = self.searchInNode(node, value[0])
		# Verifica si existe el primero
		for i in range(1, len(value)):# Lee desde el segundo si hay
			if temp is not False:
				temp= self.searchInNode(temp, value[i])
		return temp

	def folderChecker(self, node, _setCurrentNode=False):
		if node.type() is "Carpeta":
			if _setCurrentNode:
				self.currentNode = node
			return True
		else:
			return False

