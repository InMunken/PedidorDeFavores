import Arista
import Grafo

#prueba
arista1 = Arista.Arista("A","B", 5)

grafo = Grafo.Grafo()
grafo.addArista(arista1)
grafo.addArista("A","c", 3)
grafo.addArista("c","B", 1)

for nodo in grafo.getRelacionados("A"):
    print(nodo)


