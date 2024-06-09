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
    lines = file.readlines()

    details = lines[0].strip().split() # Guardamos los detalles de la primera línea
    cantidadNodos = int(details[0])  # Guardamos la cantidad de nodos
    cantidadRelaciones = int(details[1])  # Guardamos la cantidad de relaciones

    # Lee los nodos
    for i in range(1, cantidadNodos+1):
        print(lines[i])

    # Lee las relaciones
    for i in range(cantidadNodos+1, cantidadNodos+cantidadRelaciones+1):
        for line in lines[i].split():
            print(line)