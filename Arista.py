class Arista:   

    # Constructor de la clase Arista 
    def __init__(self, nodoin, nodofin, peso ):
        self.nodoin = nodoin
        self.nodofin = nodofin
        self.peso = peso
        self.final = False

    # Devuelve True si el nodo esta en la arista
    def tieneNodo(self, nodo):

        return nodo==self.nodoin or nodo==self.nodofin
    
    # TODO agregar cláusla par manejar posible error de no encontrar el nodo
    def devolverOtro(self,nodo):
        try:
            if(nodo==self.nodoin):
                return self.nodofin
            elif(nodo==self.nodofin):
                return self.nodoin
        except Exception as e:
            return 'No esta conectado, o no existe ', nodo
   
    def getPeso(self):
        return self.peso

    def getNodoI(self):
        return self.nodoin

    def getNodoF(self):
        return self.nodofin
