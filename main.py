import Arista
import Grafo
import Lectura

### Se leen los datos del archivo de entrada

lector = Lectura.Lector("entrada.in") 

nodos = lector.get_nodes()
aristas = lector.get_edges()


### Se crea el grafo
grafo = Grafo.Grafo()


### Se añaden los nodos y las aristas al grafo
for nodo in nodos:
    grafo.addNodo(nodo)
    #print("añandido el nodo", nodo)

for arista in aristas:
    grafo.addArista(arista[0], arista[1], int(arista[2]))
    print(arista[0])
    print(arista[1])
    print(arista[2])



Grafo.Grafo.Dijkstra(grafo,"Pitusas","Pola")