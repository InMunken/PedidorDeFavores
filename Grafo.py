import sys
import Arista


class Grafo: #instancia de la clase grafo


    # Constructor
    def __init__(self):

        self.nodos = []
        self.Arista = []
        pass

    # Metodos añade nodo
    def addNodo(self, nodo):

        self.nodos.append(nodo)

    # Metodos añade arista
    def addArista(self, *args):

        # Si solo hay un argumento añade una arista
        if (len(args)==1):
            self.Arista.append(args[0])
        # Sino construye una arista
        else:
            self.Arista.append(Arista.Arista(args[0],args[1],args[2]))

        pass

    # Devuelve los nodos relacionados
    def getRelacionados(self, nodo):

        nodosTotales = []

    # Recorre todas las aristas
        for arista in self.Arista:

            # Si el nodo esta en la arista añade el otro nodo
            if(arista.tieneNodo(nodo)):
                nodosTotales.append(arista.devolverOtro(nodo))
            
        return nodosTotales

    # Devuelve las aristas de un nodo especifico
    def getAristasDeNodo(self, nodo):

        aristaTotales = []
        
        for arista in self.Arista:

            if(arista.tieneNodo(nodo)):

                aristaTotales.append(arista.devolverOtro(nodo))

        return aristaTotales

    class Dijkstra:

        def __init__(self,grafo,nodoInicial,nodoFinal):
            
            self.grafo = grafo
            self.nodoInicial = nodoInicial
            self.nodoFinal = nodoFinal

            nodoActual = nodoInicial

            self.nodosVisitados = []
            self.nodosVisitados.append(nodoActual)

            #mapa de distancias
            self.DistanciasAux = {
                nodoActual:0
            }

            self.DistanciasVisitados = {
                nodoActual:0
            }

            nodosVecinos = self.grafo.getAristasDeNodo(nodoActual)

            print(aristas)

            for nodo in nodosVecinos:

                self.DistanciasAux[arista.getNodoF()] = arista.getPeso()

            print("ante del if final")

            if(self.recorre(nodoActual)):
                print(self.DistanciasAux)

            



        def nodoMenor(self):

            valores_ordenados = sorted(self.DistanciasAux)

            for clave, valor in valores_ordenados.items():
                if (valor not in self.nodosVisitados):
                    return clave



        def recorre(self, nodoActual):

            #distanciaActual = self.getAristaLiviana(nodoActual).getPeso() + self.DistanciasAux[nodoActual]
            distanciaActual = self.DistanciasAux[nodoActual]
            #self.nodoActual= self.getAristaLiviana(nodoActual).getNodoF()
            self.nodoActual= self.nodoMenor()

            if (self.nodoActual == self.nodoFinal):

                return True

                

            aristas = self.grafo.getAristasDeNodo(nodoActual)

            print(aristas)

            for arista in aristas:

                if arista.getNodoF() not in self.nodosVisitados:

                    if (self.DistanciasAux[arista.getNodoF()] < distanciaActual + arista.getPeso()):

                        self.DistanciasAux[arista.getNodoF()] = distanciaActual + arista.getPeso()
            
            self.nodosVisitados.append(nodoActual)

            return self.recorre(nodoActual)
            
            
        
        def getAristaLiviana(self,nodo):

            aristaMin = sys.maxsize

            for arista in self.grafo.getAristasDeNodo(nodo):

                if (arista.getPeso()<aristaMin and arista.getNodoF() not in self.nodosVisitados):

                    aristaMin=arista.getPeso()
            
            return aristaMin

        
    