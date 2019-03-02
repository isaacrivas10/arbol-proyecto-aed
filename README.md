# arbol-proyecto-aed


CAMBIOS :
	
	GENERAL:
		Cambia formato de cambios, se previsualizara facilmente desde aqui.
	
	Node:
		27/02/19- Isaac Rivas
		Se deprecia father al no necesitar conocer quien esta arriba
		Se deprecia la clase Root al ser un derivado de nodo y una carpeta a la vez
		
		28/02/19- Isaac Rivas
		Descomposicion de archivo nodes.py en TDAs especificos
		Clase Nodes deja de ser padre de Archivo y Carpeta, estos se vuelven independientes. Por lo tanto, el valor de un nodo puede ser una Carpeta o un Archivo, ya que estos se transforman en TDA.
		
	Arbol:
		27/02/18- Isaac Rivas
		Re-estructuracion del metodo add, moveTo, getBranches,
		seachInNode
		Nuevo metodo checkPath
		Metodo remove sin terminar
		
		28/02/19- Isaac Rivas
		*REACOMODADO*Aun en re acomodacion de los cambios efectuados en Node
		El Arbol trabaja con forme a nodos, toda su estructura esta compuesta por listas enlazadas. Cada nodo contiene un valor, que es una instancia de una clase. Las clase carpeta es la unica con el atributo branches (lista enlazada)
		Metodos actualizados:
			moveTo*
			getBranches*
			checkPath
			add
			*Ver archivo temp para pruebas
			remove aun inconcluso

		01/03/19- Isaac Rivas
		Metodos actualizados:
			moveTo --> moveToPosition
			getBranches
		Metodos nuevos:
			remove
			moveNodeTo: Traslada un nodo de una posicion a otra,
			luego lo elimina de su posicion original.
			folderChecker
			walk: Trasladarse mediante un path, no utilizable fuera del
			arbol, no lo recomiendo.
		Se necesita:
			Mejor documentacion
			Crear metodo que retorne el path absoluto de un nodo
			Y de todos los nodos en un path relativo



	Lista Enlazada:
		28/02/19
		Se crea como TDA separado, trabaja con nodos en su interior

    Consola:
		01/03/19 - Josue Izaguirre
		Consola trabaja unicamente con arbol y es llamada con una sola función sin agregarle parametros. Puede manejar ciertos errores y ciertos casos con los comandos. No obstante, le falta implementación con arbol. Consola corre en su propia carpeta con el ultimo commit hasta la fecha (hoy 1 de marzo 2019 a las 00:14).
	
