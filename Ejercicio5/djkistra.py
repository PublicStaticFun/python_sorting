import heapq

def dijkstra(grafo, inicio, destino):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    previo = {nodo: None for nodo in grafo}

    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual == destino:
            break

        for vecino, peso in grafo[nodo_actual].items():
            nueva_dist = distancia_actual + peso

            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                previo[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_dist, vecino))

    camino = []
    nodo = destino
    while nodo:
        camino.insert(0, nodo)
        nodo = previo[nodo]

    return distancias[destino], camino

grafo_metro = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2, "F": 6},
    "E": {"C": 10, "D": 2, "F": 3},
    "F": {"D": 6, "E": 3}
}

distancia, ruta = dijkstra(grafo_metro, "A", "F")
print("Tiempo minimo: ", distancia, "minutos")
print("Ruta: ", " -> ".join(ruta))