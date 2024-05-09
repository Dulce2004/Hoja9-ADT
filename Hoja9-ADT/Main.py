#HOJA DE TRABAJO #9 - ADT
#
#Dulce Ambrosio - 231143
#Daniel Chet - 231177


import networkx as nx  # Importa la librería NetworkX para trabajar con grafos
import heapq  # Importa el módulo heapq para trabajar con colas de prioridad


#Lee un archivo de rutas y construye un grafo.
def leer_archivo_rutas(archivo):
    grafo = nx.Graph()  # Crea un nuevo grafo 

    with open(archivo, 'r') as file:  # Abre el archivo en modo lectura
        for linea in file:  # Itera sobre cada línea del archivo
            origen, destino, costo = [s.strip().strip('"') for s in linea.split(',')]# Eliminar comillas y dividir por comas
            costo = int(costo)  # Convierte el costo a entero

            grafo.add_edge(origen, destino, weight=costo)  # Añade una ruta de origen a destino con el costo
            grafo.add_edge(destino, origen, weight=costo)  # Añade una ruta de destino a origen con el mismo costo

    return grafo  # Devuelve el grafo construido

def dijkstra(grafo, origen):
    distancias = {nodo: float('inf') for nodo in grafo.nodes()}
    distancias[origen] = 0
    cola = [(0, origen)]  # (costo_actual, nodo)

    while cola:
        costo_actual, nodo_actual = heapq.heappop(cola)

        if costo_actual > distancias[nodo_actual]:
            continue

        for vecino in grafo.neighbors(nodo_actual):
            costo = grafo[nodo_actual][vecino]['weight']
            nuevo_costo = distancias[nodo_actual] + costo

            if nuevo_costo < distancias[vecino]:
                distancias[vecino] = nuevo_costo
                heapq.heappush(cola, (nuevo_costo, vecino))

    return distancias