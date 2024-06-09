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

        pass

    class Dijkstra:

        

        def getAristaLiviana(self,nodo):

            aristaMin = self.grafo.getAristasDeNodo(nodo)

            for arista in self.grafo.getAristasDeNodo(nodo):

                arista.getPeso(self)


                pass

'''
    def addArista(self, nodoI, nodoF, peso):

        self.Arista.append(Arista.Arista(nodoI,nodoF,peso))

        pass
    def addArista(self, arista):

        self.Arista.append(arista)

        pass 
'''