import Arista


class Grafo:

    def __init__(self):

        self.nodos = []
        self.Arista = []
        pass

    def addNodo(self, nodo):

        self.nodos.append(nodo)

    
    def addArista(self, nodoI, nodoF, peso):

        if (len(args)==1):
            self.Arista.append(args[0])
        else:

            self.Arista.append(Arista.Arista(args[0],args[1],args[2]))

        pass

    def getRelacionados(self, nodo):

        nodosTotales = []

        for arista in self.Arista:
            if(arista.tieneNodo(nodo)):
                nodosTotales.append(arista.devolverOtro(nodo))
            
        return nodosTotales

        

'''
    def addArista(self, nodoI, nodoF, peso):

        self.Arista.append(Arista.Arista(nodoI,nodoF,peso))

        pass
    def addArista(self, arista):

        self.Arista.append(arista)

        pass 
'''