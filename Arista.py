class Arista:

    def __init__(self, nodoin, nodofin, peso ):
        self.nodoin = nodoin
        self.nodofin = nodofin
        self.peso = peso

    def tieneNodo(self, nodo):

        return nodo==self.nodoin or nodo==self.nodofin
    
    def devolverOtro(self,nodo):
        if(nodo==self.nodoin):
            return self.nodofin
        elif(nodo==self.nodofin):
            return self.nodoin
    
