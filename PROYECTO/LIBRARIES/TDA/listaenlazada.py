
class ListaEnlazada:
	"""
		Tipo de dato abstracto:
				Lista Enlazada
	"""
	
	def __init__(self, father):
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

	def len(self):
		len = 0
		i= True
		t= self.first
		while t is not None:			
			len += 1
			t= t.getNext()
		return len
