import os

# Obtener el path del archivo actual
current_file_path  = os.path.abspath(__file__)
directory_path  = os.path.dirname(current_file_path)
file_path  = os.path.join(directory_path, 'entrada.in')

# Traduzco los tipos de palabras a pesos de aristas
tipos_palabras = {
    "AmigoPersonal": 3,
    "Compañero": 2,
    "Conocido": 1
}

#Lectura del archivo
with open(file_path, 'r') as file:
    #leo el archivo en líneas
    for line in file:
        #Separa cada línea en sus detalles
        details = line.strip().split()

        #Obtengo la cantidad de nodos y relaciones
        cantidadNodos = int(details[0])
        cantidadRelaciones = int(details[1])
     
        for i in range(2, cantidadNodos):
              print(i)
