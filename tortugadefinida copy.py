import turtle

# Definir el grafo como un diccionario de adyacencia con pesos
graph = {
    "ANA": [("CARLA", 3), ("DANIEL", 2), ("OSCAR", 3), ("HUGO", 1)],
    "BETO": [("DANIEL", 1), ("CARLA", 3), ("ELENA", 3)],
    "CARLA": [("ANA", 3), ("BETO", 3), ("DANIEL", 1), ("ISABEL", 2)],
    "DANIEL": [("BETO", 1), ("CARLA", 1), ("ANA", 2)],
    "ELENA": [("FELIPE", 1), ("BETO", 3), ("OSCAR", 1)],
    "FELIPE": [("ELENA", 1), ("GABRIELA", 2), ("HUGO", 3)],
    "GABRIELA": [("FELIPE", 2), ("HUGO", 3)],
    "HUGO": [("GABRIELA", 3), ("ANA", 1), ("FELIPE", 3)],
    "ISABEL": [("CARLA", 2), ("JORGE", 2)],
    "JORGE": [("ISABEL", 3), ("KAREN", 3)],
    "KAREN": [("JORGE", 3), ("LUIS", 1)],
    "LUIS": [("KAREN", 1), ("MARTA", 2)],
    "MARTA": [("LUIS", 2), ("NORA", 3)],
    "NORA": [("MARTA", 3), ("OSCAR", 1)],
    "OSCAR": [("ANA", 3), ("NORA", 1), ("ELENA", 1)]
}


# Definir la posición de los nodos
positions = {
    "ELENA": (-200, 100),
    "OSCAR": (-100, 100),
    "NORA": (-300, 0),
    "MARTA": (-300, -100),
    "LUIS": (-200, -200),
    "KAREN": (100, -200),
    "HUGO": (0, 100),
    "FELIPE": (100, 200),
    "GABRIELA": (200, 100),
    "ANA": (0, 0),
    "CARLA": (100, 0),
    "ISABEL": (200, 0),
    "JORGE": (300, 0),
    "DANIEL": (0, -100),
    "BETO": (100, -100)
}

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
    t.fillcolor("blue")  # Establecer el color de relleno a blanco
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
