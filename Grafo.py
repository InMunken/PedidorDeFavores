import sys
import Arista


class Grafo: # Defincion de la clase grafo


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

                aristaTotales.append(arista)
                #print(arista.toString())

        return aristaTotales

    class Dijkstra:

        def __init__(self,grafo,nodoInicial,nodoFinal):
            
            #inicializacion de variables

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

            aristas = self.grafo.getAristasDeNodo(self.nodoActual)
            print(self.nodoActual)

            for arista in aristas:

                self.DistanciasAux[arista.devolverOtro(self.nodoActual)] = arista.getPeso()

            

            if(self.recorre()):
                print(self.DistanciasAux)
                print("Entre " ,nodoInicial , " y " , nodoFinal , " hay una distancia de amistad de: " , self.DistanciasAux[self.nodoActual])
                #print("Entre " ,nodoInicial , " y " , nodoFinal , " hay una distancia de amistad de: " , self.distanciaActual)
                #print(self.nodosVisitados)

            #return self.DistanciasAux[self.nodoActual]

            

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

            #print("el nodo actual es: ", self.nodoActual)

            #print(self.nodoActual == self.nodoFinal)

            if (self.nodoActual == self.nodoFinal):

                return True


            aristas = self.grafo.getAristasDeNodo(self.nodoActual)

            for arista in aristas:

                if arista.devolverOtro(self.nodoActual) not in self.nodosVisitados:

                    #print(arista.getNodoI())
                    try:

                        if (self.DistanciasAux[arista.devolverOtro(self.nodoActual)] > self.distanciaActual + arista.getPeso()):

                            self.DistanciasAux[arista.devolverOtro(self.nodoActual)] = (self.distanciaActual + arista.getPeso())
                            
                    except:
                        self.DistanciasAux[arista.devolverOtro(self.nodoActual)] = self.distanciaActual + arista.getPeso()
                    
            
            self.nodosVisitados.append(self.nodoActual)

            return self.recorre()
            
            
        
        def getAristaLiviana(self,nodo):

            aristaMin = sys.maxsize

            for arista in self.grafo.getAristasDeNodo(nodo):

                if (arista.getPeso()<aristaMin and arista.getNodoF() not in self.nodosVisitados):

                    aristaMin=arista.getPeso()
            
            return aristaMin

        
    