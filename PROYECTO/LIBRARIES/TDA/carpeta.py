

class Carpeta:
	"""
		Tipo de Dato Abstracto:
				Carpeta
	"""

	def __init__(self, name):
		self.name = name
		self.branches = ListaEnlazada(self)
		
	def add(self, addValue):
		self.branches.add(addValue)
	