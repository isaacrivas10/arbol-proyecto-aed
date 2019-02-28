# ESTO FUNCIONA NO MODIFICAR

"""
CAMBIOS:
	27/02/19	
	Se deprecia father al no necesitar conocer quien esta arriba
	Se deprecia la clase Root al ser un derivado de nodo y una carpeta a la vez
	

"""

class ListaEnlazada:

	def __init__(self):
		self.first= None
	
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
	
	def remove(self, remV): # remV hace referencia al VALOR de el objeto, NO es un nodo
		pass


class Nodes(object):

	def __init__(self):	
		self.value= None
		self.iAm= None
		self.branches= None
			
	def getType(self):
		return self.iAm

	def getValue(self):
		return self.value

	def setNext(self, nextNode):
		self.next= nextNode

	def getNext(self):
		return self.next


class Carpeta(Nodes):

	def __init__(self, value):
		self.iAm = "carpeta"
		self.value = value
		self.branches = ListaEnlazada()
		self.next= None
		
	def add(self, addValue):
		self.branches.add(addValue)
	
	
class Archivo(Nodes):

	def __init__(self, value):
		self.iAm = "archivo"
		self.value = value
