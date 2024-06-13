import turtle
import random
import math

# Definir el grafo como un diccionario de adyacencia con pesos
graph = {
    "ELENA": [("OSCAR", 1), ("NORA", 1)],
    "OSCAR": [("ELENA", 1), ("HUGO", 1), ("ANA", 3), ("NORA", 3)],
    "NORA": [("ELENA", 1), ("OSCAR", 3), ("MARTA", 3)],
    "MARTA": [("NORA", 3), ("LUIS", 2)],
    "LUIS": [("MARTA", 2), ("KAREN", 1)],
    "KAREN": [("LUIS", 1)],
    "HUGO": [("OSCAR", 1), ("ANA", 3), ("FELIPE", 3)],
    "FELIPE": [("HUGO", 3), ("GABRIELA", 2)],
    "GABRIELA": [("FELIPE", 2), ("HUGO", 3)],
    "ANA": [("OSCAR", 3), ("HUGO", 3), ("CARLA", 3)],
    "CARLA": [("ANA", 3), ("ISABEL", 2), ("DANIEL", 1)],
    "ISABEL": [("CARLA", 2), ("JORGE", 2)],
    "JORGE": [("ISABEL", 2)],
    "DANIEL": [("CARLA", 1), ("BETO", 2)],
    "BETO": [("DANIEL", 2), ("KAREN", 1)]
}

# Inicializar las posiciones de los nodos aleatoriamente
positions = {node: (random.randint(-900, 900), random.randint(-900, 900)) for node in graph}

# Parámetros del algoritmo de fuerza de resorte
width, height = 900, 900
k = math.sqrt(width * height / len(graph))  # Constante de resorte
iterations = 40
temperature = width / 10.0

# Función de distancia
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Definir una distancia mínima entre nodos
min_distance = 50

# Algoritmo de fuerza de resorte
for _ in range(iterations):
    disp = {node: [0, 0] for node in graph}
    
    # Calcular las distancias mínimas entre todos los pares de nodos
    min_distances = {(v, u): min_distance for v in graph for u in graph if v != u}
    
    # Calcular las fuerzas de repulsión
    for v in graph:
        for u in graph:
            if v != u:
                delta = (positions[v][0] - positions[u][0], positions[v][1] - positions[u][1])
                dist = distance(positions[v], positions[u])
                if dist > 0:
                    min_distances[(v, u)] = min(dist, min_distances[(v, u)])
                    repulsive_force = k * k / dist
                    if dist < min_distance:
                        repulsive_force *= min_distance / dist  # Ajustar la fuerza si la distancia es menor que la mínima
                    disp[v][0] += delta[0] / dist * repulsive_force
                    disp[v][1] += delta[1] / dist * repulsive_force
    
    # Ajustar las fuerzas de repulsión para mantener la distancia mínima entre todos los nodos
    for v in graph:
        for u in graph:
            if v != u:
                delta = (positions[v][0] - positions[u][0], positions[v][1] - positions[u][1])
                dist = distance(positions[v], positions[u])
                if dist > 0:
                    if dist < min_distances[(v, u)]:
                        repulsive_force = k * k / dist
                        repulsive_force *= (min_distances[(v, u)] - dist) / dist
                        disp[v][0] += delta[0] / dist * repulsive_force
                        disp[v][1] += delta[1] / dist * repulsive_force
    
    # Resto del algoritmo de fuerza de resorte...


    
    # Calcular las fuerzas de atracción
    for v in graph:
        for u, weight in graph[v]:
            delta = (positions[v][0] - positions[u][0], positions[v][1] - positions[u][1])
            dist = distance(positions[v], positions[u])
            if dist > 0:
                attractive_force = dist * dist / k
                disp[v][0] -= delta[0] / dist * attractive_force
                disp[v][1] -= delta[1] / dist * attractive_force
    
    # Actualizar las posiciones
    for v in graph:
        positions[v] = (
            positions[v][0] + disp[v][0] * 0.1,
            positions[v][1] + disp[v][1] * 0.1
        )
    
    # Limitar las posiciones a la ventana
    for v in positions:
        positions[v] = (
            min(width / 2, max(-width / 2, positions[v][0])),
            min(height / 2, max(-height / 2, positions[v][1]))
        )
    
    temperature *= 0.95

# Configurar la ventana de turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Grafo")

# Crear una tortuga
t = turtle.Turtle()
t.speed(0)

# Dibujar los nodos
def draw_node(name, pos):
    t.penup()
    t.goto(pos[0], pos[1] - 30)
    t.pendown()
    t.fillcolor("white")  # Establecer el color de relleno a blanco
    t.begin_fill()
    t.circle(30)  # Controlar el tamaño del nodo aquí
    t.end_fill()
    t.penup()
    t.goto(pos[0], pos[1] - 10)
    t.write(name, align="center", font=("Arial", 12, "normal"))

# Dibujar las aristas
def draw_edge(start, end, weight):
    t.penup()
    t.goto(positions[start])
    t.pendown()
    t.goto(positions[end])
    # Calcular la posición del texto del peso
    mid_x = (positions[start][0] + positions[end][0]) / 2
    mid_y = (positions[start][1] + positions[end][1]) / 2
    t.penup()
    t.goto(mid_x, mid_y)
    t.circle(15)
    t.fillcolor("white")
    t.write(weight, align="center", font=("Arial", 10, "normal"))

# Dibujar el grafo
for node, edges in graph.items():
    for edge, weight in edges:
        draw_edge(node, edge, weight)

for node, pos in positions.items():
    draw_node(node, pos)

# Ocultar la tortuga y mostrar la ventana
t.hideturtle()
turtle.done()