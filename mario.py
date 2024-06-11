import networkx as nx
import matplotlib.pyplot as plt

# Definimos los valores de las amistades, en un DICCIONARIO:
Valor_Amistad = {"amigo personal": 3, "conocido": 2, "compañero": 1}

# Definimos las relaciones para el primer grafo, con una LISTA de TUPLAS:
relaciones_1 = [
    ('Juan', 'Pedro', 'amigo personal'),
    ('Juan', 'Jose', 'amigo personal'),
    ('Pedro', 'Maria', 'conocido'), 
    ('Pedro', 'Ana', 'conocido'), 
    ('Maria', 'Carlos', 'compañero'),
    ('Carlos', 'Luis', 'amigo personal'),
    ('Carlos', 'Juan', 'conocido'),
    ('Luis', 'Ana', 'conocido'),
    ('Ana', 'Jose', 'compañero'),
    ('Ana', 'Maria', 'amigo personal')
]
# Definimos las relaciones para el segundo grafo, con otra LISTA de TUPLAS:
relaciones_2 = [
    ('Alan', 'Toby', 'compañero'),
    ('Alan', 'Maxi', 'amigo personal'),
    ('Toby', 'Carlos', 'conocido'),
    ('Carlos', 'Fede', 'amigo personal'),
    ('Fede', 'Ely', 'conocido'),
    ('Fede', 'Gaby', 'amigo personal'),
    ('Ely', 'Fran', 'compañero'),
    ('Fran', 'Gonza', 'amigo personal'),
    ('Gonza', 'Gaby', 'conocido'),
    ('Gaby', 'Ivan', 'compañero'),
    ('Ivan', 'Maxi', 'amigo personal'),
    ('Maxi', 'Ely', 'conocido')
]
# Creamos el grafo basado en las relaciones que le vamos a pasar por parametros:
def Crear_Grafo(relaciones):

    Grafo = nx.Graph()
    for persona_1, persona_2, relacion in relaciones:
        Grafo.add_edge(persona_1, persona_2, weight = Valor_Amistad[relacion])
    return Grafo
# Creamos los grafos:
Grafo_1 = Crear_Grafo(relaciones_1)
Grafo_2 = Crear_Grafo(relaciones_2)

# Calculamos la distancia mínima de amistad con Dijkstra:
def AplicarDijkstra(Grafo, persona_1, persona_2):

    try:
        distancia = nx.dijkstra_path_length(Grafo, persona_1, persona_2, weight='weight')
        return distancia
    except nx.NetworkXNoPath:
        return 'No se conocen'  # No hay camino entre persona_1 y persona_2

# Armamos la Visualizacion del grafo:
def Mostrar_grafo(Grafo, titulo):

    posicion = nx.spring_layout(Grafo, k=0.1, iterations=40)
    plt.figure(figsize=(12, 6), edgecolor= '1')
    nx.draw(Grafo, posicion, with_labels=True, node_color='lightgreen', node_shape = 'o' , edge_color='gray', node_size=1500, font_size=13, font_weight='bold')
    etiquetas = nx.get_edge_attributes(Grafo, 'weight')
    nx.draw_networkx_edge_labels(Grafo, posicion, edge_labels = etiquetas)
    plt.title(titulo)
    plt.show()

# Visualizamos los grafos:
Mostrar_grafo(Grafo_1, "Grafo 1: Relaciones de Amistad")
Mostrar_grafo(Grafo_2, "Grafo 2: Relaciones de Amistad")

# Casos de prueba para el primer grafo:
print("Dijkstra en Grafo 1:")
aux = AplicarDijkstra(Grafo_1, 'Juan', 'Maria')
print("Juan a Maria:  Esperado: 3, Recibido:", aux, '=', 3 == aux)
aux = AplicarDijkstra(Grafo_1, 'Juan', 'Luis')
print("Juan a Luis:  Esperado: 5, Recibido: ", aux, '=', 5 == aux)
aux = AplicarDijkstra(Grafo_1, 'Ana', 'Juan')
print("Ana a Juan:  Esperado: 4, Recibido: ", aux, '=', 4 == aux)

# Casos de prueba para el segundo grafo:
print("Dijkstra en Grafo 2:")
aux = AplicarDijkstra(Grafo_2, 'Alan', 'Fede')
print("Alan a Fede: Esperado: 6, Recibido: ", aux, '=', 6 == aux)
aux = AplicarDijkstra(Grafo_2, 'Gonza', 'El Profe')
print("Gonza a Ely: Esperado: No se conocen, Recibido: ", aux, '=', 'No se conocen' == aux)
aux = AplicarDijkstra(Grafo_2, 'Maxi', 'Toby')
print("Maxi a Beto: Esperado: 17, Recibido: ", aux, '=', 4 == aux)