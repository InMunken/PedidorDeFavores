import os
current_file_path  = os.path.abspath(__file__)
directory_path  = os.path.dirname(current_file_path)
file_path  = os.path.join(directory_path, 'entrada.in')

tipos_palabras = {
    "AmigoPersonal": 3,
    "Compañero": 2,
    "Conocido": 1
}


with open(file_path, 'r') as file:
    for line in file:
        details = line.strip().split()

        cantidadNodos = int(details[0])
        cantidadRelaciones = int(details[1])



        for detail in details:
            print(detail)
