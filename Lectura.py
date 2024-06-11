import os

class Lector:
    
    def __init__(self, path):
        # Obtener el path del archivo actual
        current_file_path  = os.path.abspath(__file__)
        directory_path  = os.path.dirname(current_file_path)
        file_path  = os.path.join(directory_path, path)

        # Diccionario de palabras a pesos de aristas
        tipos_palabras = {
        "AmigoPersonal": 3,
        "Conocido": 2,
        "Companero": 1
        }

        #Lectura del archivo
        with open(file_path, 'r') as file:
            self.lines = file.readlines()

            details = self.lines[0].strip().split() # Guardamos los detalles de la primera línea

            self.cantidadNodos = int(details[0])  # Guardamos la cantidad de nodos
            self.cantidadRelaciones = int(details[1])  # Guardamos la cantidad de relaciones

            self.listadenodos = [] # Creo una lista vacía para guardar los nodos
            self.listadeRelaciones = [] # Creo una lista vacía para guardar las relaciones

            # Lee los nodos
            for i in range(1, self.cantidadNodos+1):
                self.listadenodos.append(self.lines[i].strip()) 
                # Repasa la lista vacía de nodos y agrega los nodos a la lista. (de la valiable lines hace un strip que es para quitar los espacios)

           # Lee las relaciones
            for i in range(self.cantidadNodos+1, self.cantidadNodos+self.cantidadRelaciones+1):
                relacion = self.lines[i].strip().split() 
                for palabra in relacion:
                    if palabra in tipos_palabras:
                    # Asignar el peso correspondiente al tipo de palabra
                        relacion[relacion.index(palabra)] = str(tipos_palabras[palabra])
                self.listadeRelaciones.append(relacion)

    
    def get_cantidadNodos(self):
        return self.cantidadNodos
    
    def get_cantidadAristas(self):
        return self.cantidadRelaciones
    
    def get_nodes(self):
        return self.listadenodos
    
    def get_edges(self):
        return self.listadeRelaciones


#lectura = Lector("hell")
