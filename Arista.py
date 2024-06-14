class Arista:   

    # Constructor de la clase Arista 
    def __init__(self, nodoin, nodofin, peso ):
        self.nodoin = nodoin #a
        self.nodofin = nodofin #b
        self.peso = peso

    # Devuelve True si el nodo esta en la arista
    def tieneNodo(self, nodo):

        return nodo==self.nodoin or nodo==self.nodofin
  
    def devolverOtro(self,nodo):
        try:
            if(nodo==self.nodoin):
                return self.nodofin
            elif(nodo==self.nodofin):
                return self.nodoin
        except:
            return 'No esta conectado, o no existe ', nodo
   
    def getPeso(self):
        return self.peso

    def getNodoI(self):
        return self.nodoin

    def getNodoF(self):
        return self.nodofin
