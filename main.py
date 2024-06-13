import Arista
import Grafo
import Lectura
import Dijkstra

### Defino metodos para añadir al grafo
def agregar_nodos(nodos):
    for nodo in nodos:
        grafo.addNodo(nodo)
        #print("añandido el nodo", nodo)

def agregar_aristas(aristas):
    for arista in aristas:
        # print(arista[0])    
        # print(arista[1])
        # print(arista[2])
        grafo.addArista(arista[0], arista[1], int(arista[2]))

### Se leen los datos del archivo de entrada

lector = Lectura.Lector("Entrada/entrada2.in") 

nodos = lector.get_nodes()
aristas = lector.get_edges()

print("Ingrese los nodos inciales y finales dada esta lista de nodos: ", nodos)

nodoInicial = input("Ingrese el nodo inicial: ")
nodoFinal = input("Ingrese el nodo final: ")


### Se crea el grafo
grafo = Grafo.Grafo()
dijkstra = Dijkstra.Dijkstra(grafo, nodoInicial, nodoFinal)

### Se añaden los nodos y las aristas
agregar_nodos(nodos)
agregar_aristas(aristas)

# Grafo.Grafo.Dijkstra(grafo,"Ana","Marta")
print(dijkstra.getCamino())

print("La distancia de amistad entre " , nodoInicial , " y " , nodoFinal , " es: " , dijkstra.getDistancia())
