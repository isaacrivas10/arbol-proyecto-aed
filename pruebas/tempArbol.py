
from temp import *


class Arbol:

	def __init__(self):
		# El constructor define la raiz de el directorio
		self.root = Carpeta("root")
		self.currentNode= self.root

	def getRoot(self):
		return self.root.getValue()

	def add(self, addValue, _type):
		"""
			Objetivo: Agregar objetos

			Uso:
				add("nombre_del_archivo", *param)
				*param puede ser -c de carpeta o -a de archivo
		"""
		new= None
		if _type == "-c":
			new= Carpeta(addValue)
		else:
			new= Archivo(addValue)
		self.currentNode.add(new)

	def remove(self, remValue):
		b= self.searchInNode(self.root, remValue)
		if b != False:
			print b.getValue()
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
		checked= self.checkPath(path)
		print checked
		if checked[0] == "relative":
			if checked[1] == self.currentNode.getValue():				
				m_dir= self.searchInNode(self.currentNode, moveV)
				if m_dir != False:
					if m_dir.iAm == "carpeta":
						self.currentNode= m_dir
						return True
					else:
						return False
		elif checked[0] == "absolute":
			# Buscamos el valor que esta dentro de root
			if len(checked) > 2: # Una o mas carpetas despues de root
				temp = self.searchInNode(self.root, checked[2])				
				for i in range(3, len(checked)):
					if temp != False:
						temp= self.searchInNode(temp, checked[i])
				if  temp != False:
					if temp.iAm == "carpeta":
						self.currentNode = temp
						return True
					else:
						return False
				else:
					return False
			else: 
				self.currentNode= self.root
			

	def checkPath(self, path):
		# Uso: /path/to/move <-- respetar / al incio
		try:
			pathCheck= path.split("/")
			if pathCheck[1] == "root":
				return ["absolute"] + pathCheck[1:]
			else:
				return ["relative"] + pathCheck[1:]
		except:
			return ["error", 1] # 1 = error

	def getBranches(self):
		# Retorna todas las ramas relativas al nodo actual
		b= self.currentNode.branches
		b_len= b.len()
		b_node= b.first
		if b_len> 0:
			for i in range(b_len):
				print "/%s/%s" % (self.currentNode.getValue(),b_node.getValue())
				b_node= b_node.getNext()
		else:
			print "/%s/" % (self.currentNode.getValue())

	def searchInNode(self, current, value):
		# Solo busca en un nodo especifico
		if current.branches.len() > 0: # Si tiene hijos
			node = current.branches.first
			for i in range(current.branches.len()): # Para cada nodo en sus ramas
				if node.getValue() == value: # Si su nombre es igual a lo que busco
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
arbol.add("carpeta", "-c") # /root/carpeta/
arbol.add("node", "-c") # /root/node/
arbol.add("archivo", "-a") # /root/archivo
#arbol.getBranches()
arbol.root.branches.first.branches.add(Carpeta("node")) # /root/carpeta/node/
arbol.root.branches.first.branches.add(Carpeta("asd")) # /root/carpeta/asd/
arbol.root.branches.first.branches.add(Carpeta("dsa")) # /root/carpeta/dsa

arbol.root.branches.first.branches.first.add(Carpeta("qwer")) # /root/carpeta/node/qwer/

#print arbol.root.branches.first.branches.first.getValue()
arbol.moveTo("carpeta", "/root/carpeta/node/qwer")
print arbol.currentNode.getValue()




