

class Node(object, value):
	"""
		Un nodo es una estrucutra personal de un arbol, lista enlazada.
		Cada nodo puede contener cualquier cosa, en este caso, Carpetas y Archivos.
		
	"""
	def __init__(self):	
		self.value= value # Contiene una instancia de una Carpeta o Archivo, no es una variable comun
		self.next= None
			
	def getType(self):
		return self.value

	def getName(self):
		return self.value.name

	def setNext(self, nextNode):
		self.next= nextNode

	def getNext(self):
		return self.next
