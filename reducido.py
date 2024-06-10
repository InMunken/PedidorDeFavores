# Definimos la distancia de cada tipo de relación
distancia = {
    "amigo personal": 3,
    "conocido": 2,
    "compañero": 1
}

# Función para agregar una relación al grafo
def agregar_relacion(grafo, persona1, persona2, tipo_relacion):
    if persona1 not in grafo:
        grafo[persona1] = []
    if persona2 not in grafo:
        grafo[persona2] = []
    grafo[persona1].append((persona2, distancia[tipo_relacion]))
    grafo[persona2].append((persona1, distancia[tipo_relacion]))

# Función para encontrar la distancia mínima sin usar heapq
def distancia_minima(grafo, inicio, fin):
    if inicio not in grafo or fin not in grafo:
        return float('inf')
    
    # Inicializar las distancias y el conjunto de nodos no visitados
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    no_visitados = set(grafo.keys())
    
    while no_visitados:
        # Seleccionar el nodo con la menor distancia
        nodo_actual = min(no_visitados, key=lambda nodo: distancias[nodo])
        
        # Si hemos llegado al nodo final, terminamos
        if nodo_actual == fin:
            return distancias[fin]
        
        # Si la distancia al nodo actual es infinita, no hay camino
        if distancias[nodo_actual] == float('inf'):
            break
        
        # Actualizar las distancias de los vecinos
        for vecino, peso in grafo[nodo_actual]:
            if vecino in no_visitados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
        
        # Marcar el nodo actual como visitado
        no_visitados.remove(nodo_actual)
    
    return float('inf')

# Crear el grafo y agregar relaciones
grafo = {}
agregar_relacion(grafo, "Juan", "Pedro", "amigo personal")
agregar_relacion(grafo, "Pedro", "María", "compañero")
agregar_relacion(grafo, "Juan", "María", "compañero")


# Probar la distancia mínima entre dos personas
inicio = "Juan"
fin = "Pedro"
distancia_amistad = distancia_minima(grafo, inicio, fin)
print(f"La mínima distancia de amistad entre {inicio} y {fin} es: {distancia_amistad}")
