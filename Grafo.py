import Arista


class Grafo:

    def __init__(self):

        self.nodos = []
        self.Arista = []
        pass

    def addNodo(self, nodo):

        self.nodos.append(nodo)

    
    def addArista(self, nodoI, nodoF, peso):

        self.Arista.append(Arista.Arista(nodoI,nodoF,peso))

        pass
    def addArista(self, arista):

        self.Arista.append(arista)

        pass

    def getRelacionados(self, nodo):

        nodosTotales = []

        for arista in self.Arista:
            if(arista.tieneNodo(nodo)):
                nodosTotales.append(arista.devolverOtro(nodo))
            
        return nodosTotales

        

