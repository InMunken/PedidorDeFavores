import Arista


class Grafo: # Defincion de la clase grafo


    # Constructor
    def __init__(self):

        self.nodos = []
        self.aristas = []

    # Metodos añade nodo
    def addNodo(self, nodo):

        self.nodos.append(nodo)

    # Metodos añade arista
    def addArista(self, *args):
        
        # Si solo hay un argumento añade una arista
        if (len(args)==1):
            self.aristas.append(args[0])
        # Sino construye una arista
        else:
            self.aristas.append(Arista.Arista(args[0],args[1],args[2]))


    # Devuelve los nodos relacionados
    def getRelacionados(self, nodo):

        nodosTotales = []

    # Recorre todas las aristas
        for arista in self.aristas:

            # Si el nodo esta en la arista añade el otro nodo
            if(arista.tieneNodo(nodo)):
                nodosTotales.append(arista.devolverOtro(nodo))
            
        return nodosTotales

    # Devuelve las aristas de un nodo especifico
    def getAristasDeNodo(self, nodo):

        aristaTotales = []
        
        for arista in self.aristas:  

            if(arista.tieneNodo(nodo)):

                aristaTotales.append(arista)

        return aristaTotales

    
        
    