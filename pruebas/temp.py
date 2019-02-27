

class ListaEnlazada:

	def __init__(self, father):
		self.father= father # Con father hago referencia un ente superior a la lista enlazada
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
			
	def getFather(self):
		return sefl.first


class Nodes(object):

	def __init__(self):	
		self.value= None
		self.iAm= None
		self.branches= None
		#self.next= None
	
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
		self.branches = ListaEnlazada(self)
		self.next= None
		
	def add(self, addValue):
		self.branches.add(addValue)
	
	
class Archivo(Nodes):

	def __init__(self, value):
		self.iAm = "archivo"
		self.value = value

c = Carpeta("carpeta1")
c.add(Carpeta("carpeta2"))
c.add(Carpeta("carpeta3"))
c.add(Carpeta("carpeta4"))
#c.branches.first.setNext(Carpeta("car"))
#c.branches.first.getNext().setNext(Carpeta("hola"))
c.branches.first.add(Carpeta("h"))
print c.branches.first.branches.first.getValue()