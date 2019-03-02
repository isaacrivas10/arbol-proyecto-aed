# NO MODIFICAR!
# SE EFECTUAN PRUEBAS

class ListaEnlazada:

	def __init__(self):
		self.first= None # Es un nodo
	
	def add(self, addV):
		c = self.first
		if c is None:
			self.first = addV
		else:
			exist= True
			while exist: # Mientras exista el nodo
				if c.getNext() is None: # Si despues de c no hay un nodo
					c.setNext(addV) # Asignamos como siguiente
					exist= False
				else: # Si no
					c = c.getNext() # Pasamos al siguiente de c
	
	def remove(self, remV): # remV hace referencia al NODO a borrar
	# Es independiente al tipo
	# De acuerdo a remV se buscara el nodo
		if remV is self.first:
			self.first= self.first.getNext()
		else:
			searched_list = self.search(remV)
			node = self.first
			for j in range(searched_list[2]-1):
				node= node.getNext() # Me localizo al nodo que esta
				# antes del que voy a borrar
			node.setNext(searched_list[1])
	   

	def search(self, searchValue):
		found= None
		node= self.first
		for o in range(self.len()):
			before= node
			if node is searchValue:
				return [node, node.getNext(), o]
			else:
				node= node.getNext()
		

	def len(self):
		len = 0
		i= True
		t= self.first
		while t is not None:			
			len += 1
			t= t.getNext()
		return len


class Node():
	"""
		Un nodo es una estrucutra personal de un arbol, lista enlazada.
		Cada nodo puede contener cualquier cosa, en este caso, Carpetas y Archivos.
		
	"""

	def __init__(self, value):	
		self.value= value # Contiene una instancia de una Carpeta o Archivo, no es una variable comun
		self.next= None
			
	def type(self): # Retorna el nombre de la clase a la que pertenece
		return self.value.__class__.__name__

	def getValue(self):
		return self.value

	def getName(self): # Retorna el nombre del valor que contiene el nodo
		return self.value.name

	def setNext(self, nextNode):
		self.next= nextNode

	def getNext(self):
		return self.next


class Carpeta:

	def __init__(self, name):
		self.name = name
		self.branches = ListaEnlazada()
		
	def add(self, addValue):
		self.branches.add(addValue)
	
	def remove(self, remValue):
		self.branches.remove(remValue)

class Archivo:

	def __init__(self, name):
		self.name = name		
