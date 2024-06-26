import sys

class Dijkstra:

        def __init__(self,grafo,nodoInicial,nodoFinal):
            
            #inicializacion de variables necesarias para el algoritmo de dijkstra

            self.grafo = grafo
            self.nodoInicial = nodoInicial
            self.nodoFinal = nodoFinal
            self.nodoActual = nodoInicial
            self.nodosVisitados = []
            self.nodosVisitados.append(self.nodoActual)

            #mapa de distancias
            self.DistanciasAux = {
                self.nodoActual:0
            }

        #devuelve el camino mas corto entre el nodo inicial y final
        def getCamino(self):

            aristas = self.grafo.getAristasDeNodo(self.nodoActual)

            for arista in aristas:

                self.DistanciasAux[arista.devolverOtro(self.nodoActual)] = arista.getPeso()
                
            
            if(self.recorre()):
                
                return self.DistanciasAux[self.nodoActual]

            
        #Devuelve el nodo de menor distancia que no se haya visitado
        def nodoMenor(self):

            valores_ordenados = dict(sorted(self.DistanciasAux.items(), key=lambda item: item[1]))

            for clave, valor in valores_ordenados.items():
                if (clave not in self.nodosVisitados):
                    return clave


        # recorre la arista mas liviana y reemplaza el nodo si la distancia es mas corta
        def recorre(self):

            self.nodoActual = self.nodoMenor()
            self.distanciaActual = self.DistanciasAux[self.nodoActual]

            if (self.nodoActual == self.nodoFinal):

                return True

            aristas = self.grafo.getAristasDeNodo(self.nodoActual)

            for arista in aristas:

                if arista.devolverOtro(self.nodoActual) not in self.nodosVisitados:

                    try:

                        if (self.DistanciasAux[arista.devolverOtro(self.nodoActual)] > self.distanciaActual + arista.getPeso()):

                            self.DistanciasAux[arista.devolverOtro(self.nodoActual)] = (self.distanciaActual + arista.getPeso())

                    # TODO agragar comentario explicativo        
                    except:
                        self.DistanciasAux[arista.devolverOtro(self.nodoActual)] = self.distanciaActual + arista.getPeso()
                    
            
            self.nodosVisitados.append(self.nodoActual)

            return self.recorre()
            
        #devuelve el peso de la arista mas liviana que su otro nodo no haya sido visitado 
        def getAristaLiviana(self,nodo):

            aristaMin = sys.maxsize

            for arista in self.grafo.getAristasDeNodo(nodo):

                if (arista.getPeso()<aristaMin and arista.devolverOtro() not in self.nodosVisitados):

                    aristaMin=arista.getPeso()
            
            return aristaMin
