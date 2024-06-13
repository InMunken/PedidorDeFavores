class Nodo:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []

    def agregar_nodo(self, id, x, y):
        self.nodos[id] = Nodo(id, x, y)

    def agregar_arista(self, desde, hacia, peso):
        self.aristas.append((desde, hacia, peso))

    def generar_svg(self, archivo):
        with open(archivo, 'w') as f:
            f.write('<?xml version="1.0" standalone="no"?>\n')
            f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n')

            # Dibujar aristas
            for desde, hacia, peso in self.aristas:
                nodo_desde = self.nodos[desde]
                nodo_hacia = self.nodos[hacia]
                f.write(f'<line x1="{nodo_desde.x}" y1="{nodo_desde.y}" x2="{nodo_hacia.x}" y2="{nodo_hacia.y}" ')
                f.write(f'style="stroke:rgb(0,0,0);stroke-width:2" />\n')
                # Dibujar peso
                mid_x = (nodo_desde.x + nodo_hacia.x) / 2
                mid_y = (nodo_desde.y + nodo_hacia.y) / 2
                f.write(f'<text x="{mid_x}" y="{mid_y}" fill="red">{peso}</text>\n')

            # Dibujar nodos
            for nodo in self.nodos.values():
                f.write(f'<circle cx="{nodo.x}" cy="{nodo.y}" r="10" fill="blue" />\n')
                f.write(f'<text x="{nodo.x + 12}" y="{nodo.y}" fill="black">{nodo.id}</text>\n')

            f.write('</svg>\n')

# Crear el grafo
grafo = Grafo()
grafo.agregar_nodo('A', 100, 100)
grafo.agregar_nodo('B', 300, 100)
grafo.agregar_nodo('C', 200, 300)

grafo.agregar_arista('A', 'B', 5)
grafo.agregar_arista('A', 'C', 10)
grafo.agregar_arista('B', 'C', 3)

# Generar archivo SVG
grafo.generar_svg('grafo.svg')
