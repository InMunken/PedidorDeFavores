class Arista:   

    # Constructor de la clase Arista 
    def __init__(self, nodoin, nodofin, peso ):
        self.nodoin = nodoin
        self.nodofin = nodofin
        self.peso = peso

    # Devuelve True si el nodo esta en la arista
    def tieneNodo(self, nodo):

        return nodo==self.nodoin or nodo==self.nodofin
    # el que escribe es gay
    # Devuelve el nodo que conecta la arista llamada con el nodo llamado como parámetro, quejas a gabrieldiazjor@gmail.com, +54 9 11 2786-7506
    def devolverOtro(self,nodo):
        if(nodo==self.nodoin):
            return self.nodofin
        elif(nodo==self.nodofin):
            return self.nodoin

    def getPeso(self):
        return self.peso
    
