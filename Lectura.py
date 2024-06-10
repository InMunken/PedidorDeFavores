import os

class Lector:
    
    def __init__(self, path):
        # Obtener el path del archivo actual
        current_file_path  = os.path.abspath(__file__)
        directory_path  = os.path.dirname(current_file_path)
        file_path  = os.path.join(directory_path, 'entrada.in') #TODO cambiar por path

        # Traduzco los tipos de palabras a pesos de aristas
        tipos_palabras = {
        "AmigoPersonal": 3,
        "Compañero": 2,
        "Conocido": 1
        }

        #Lectura del archivo
        with open(file_path, 'r') as file:
            self.lines = file.readlines()

            details = self.lines[0].strip().split() # Guardamos los detalles de la primera línea
            self.cantidadNodos = int(details[0])  # Guardamos la cantidad de nodos
            self.cantidadRelaciones = int(details[1])  # Guardamos la cantidad de relaciones

            self.listadenodos = []
            self.listadeRelaciones = []

            # Lee los nodos
            for i in range(1, self.cantidadNodos+1):
                self.listadenodos.append(self.lines[i].strip())

            # Lee las relaciones            
            for i in range(self.cantidadNodos+1, self.cantidadNodos+self.cantidadRelaciones+1):
                self.listadeRelaciones.append(self.lines[i].strip().split())  # Separa cada línea en una lista de palabras


    
    def get_cantidadNodos(self):
        return self.cantidadNodos
    
    def get_cantidadAristas(self):
        return self.cantidadRelaciones
    
    def get_nodes(self):
        return self.listadenodos
    
    def get_edges(self):
        return self.listadeRelaciones


#lectura = Lector("hell")
