# arbol-proyecto-aed


CAMBIOS :
	
	GENERAL:
		Cambia formato de cambios, se previsualizara facilmente desde aqui.
	
	Node:
		27/02/19	
		Se deprecia father al no necesitar conocer quien esta arriba
		Se deprecia la clase Root al ser un derivado de nodo y una carpeta a la vez
		
		28/02/19
		Descomposicion de archivo nodes.py en TDAs especificos
		Clase Nodes deja de ser padre de Archivo y Carpeta, estos se vuelven independientes. Por lo tanto, el valor de un nodo puede ser una Carpeta o un Archivo, ya que estos se transforman en TDA.
		
	Arbol:
		27/02/18
		Re-estructuracion del metodo add, moveTo, getBranches,
		seachInNode
		Nuevo metodo checkPath
		Metodo remove sin terminar
		
		28/02/19
		*REACOMODADO*Aun en re acomodacion de los cambios efectuados en Node
		El Arbol trabaja con forme a nodos, toda su estructura esta compuesta por listas enlazadas. Cada nodo contiene un valor, que es una instancia de una clase. Las clase carpeta es la unica con el atributo branches (lista enlazada)
		Metodos actualizados:
			moveTo*
			getBranches*
			checkPath
			add
			*Ver archivo temp para pruebas
			remove aun inconcluso


	Lista Enlazada:
		28/02/19
		Se crea como TDA separado, trabaja con nodos en su interior
	
