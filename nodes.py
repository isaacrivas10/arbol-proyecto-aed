
class Nodes:

	def __init__(self, value):	
		self.value= value
		self.iAm= None
		self.branches= None
		self.father= None

	def getValue(self):
		return self.value

	def setNext(self, nextValue):
		self.next= nextValue

	def getNext(self):
		return self.next

	def getType(self):
		return self.iAm


class Archivo(Nodes):

	def __init__(self, value, father=None):
		self.father= father
		self.iAm = "archivo"
		self.value = value

class Carpeta(Nodes):

	def __init__(self, value, father=None):
		self.iAm = "carpeta"
		self.value = value
		self.branches = list()

	def add(self, addValue):
		self.branches.append(addValue)

class Root(Nodes):

	def __init__(self, value):
		self.iAm= "root"
		self.value= value
		self.branches = list()

	def add(self, addValue):
		self.branches.append(addValue)
