
from tempArbol import *

# Crea una instancia del arbol
arbol = Arbol()
arbol.add("carpeta", "-c") # /carpeta/
arbol.add("node", "-c") # /node/
arbol.add("archivo", "-a") # /archivo

print arbol.currentPath

arbol.moveToPosition("node", "/") # cd /node

print arbol.currentPath

arbol.add("carpeta2", "-c") # mkdir carpeta2

arbol.moveNodeTo("/archivo", "/node") # mv /carpeta /node
# Si te das cuenta movimos carpeta que se ubica en / estando en /node
# Osea que moveNodeTo mueve el path en si no si es archivo,
# si hay problema hay que cambiarlo

arbol.add("carpeta3", "-c")

#arbol.moveToPosition("/", "/") # por si hace cd /

arbol.moveToPosition("carpeta3", "node") # cd carpeta3 estando en /node

print arbol.currentPath

arbol.add("hola", "-c")

arbol.moveToPosition("hola", "carpeta3") # cd hola estando en carpeta3

arbol.add("archivoHEHE", "-a")

arbol.moveToPosition("/", "/")

print arbol.currentPath

arbol.moveToPosition("hola", "/node/carpeta3") # cd /node/carpeta3/hola

print arbol.currentPath
