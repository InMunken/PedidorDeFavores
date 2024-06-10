import Arista
import Grafo
import Lectura

#prueba más importante que la de Ñandú:

lector = Lectura.Lector("eventualmente esto servirá para algo")

# print(lector.get_cantidadNodos())
# print(lector.get_cantidadAristas())
# print(lector.get_nodes())
# print(lector.get_edges())


#prueba
arista1 = Arista.Arista("A","B", 5)

grafo = Grafo.Grafo()

for i in range(lector.get_cantidadNodos()):
    




grafo.addArista(arista1)
grafo.addArista("A","c", 3)
grafo.addArista("c","B", 1)

for nodo in grafo.getRelacionados("A"):
    print(nodo)


