#HOJA DE TRABAJO #9 - ADT
#
#Dulce Ambrosio - 231143
#Daniel Chet - 231177

import networkx as nx  # Importa la librería NetworkX para trabajar con grafos
import heapq  # Importa el módulo heapq para trabajar con colas de prioridad
import matplotlib.pyplot as plt # Importa la libreria matplotlib para graficar

#Lee un archivo de rutas y construye un grafo.
def leer_archivo_rutas(archivo):
    grafo = nx.Graph()  # Crea un nuevo grafo 

    with open(archivo, 'r') as file:  # Abre el archivo en modo lectura
        for linea in file:  # Itera sobre cada línea del archivo
            # Eliminar comillas y dividir por comas
            origen, destino, costo = [s.strip().strip('"') for s in linea.split(',')]
            costo = int(costo)  # Convierte el costo a entero
            grafo.add_edge(origen, destino, weight=costo)  # Añade una ruta de origen a destino con el costo
            grafo.add_edge(destino, origen, weight=costo)  # Añade una ruta de destino a origen con el mismo costo

    return grafo  # Devuelve el grafo construido

def dijkstra(grafo, origen):
    
    distancias = {nodo: float('inf') for nodo in grafo.nodes()}  # Inicializa las distancias a infinito para todos los nodos
    distancias[origen] = 0  # La distancia desde el origen a sí mismo es cero
    cola = [(0, origen)]  # Crea una cola de prioridad con la (costo_actual, nodo)

    # Dibuja el grafo antes de ejecutar Dijkstra utilizando networkx
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(grafo)
    nx.draw_networkx(grafo, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_color='black', font_weight='bold', edge_color='gray')
    plt.title('Grafo de Rutas')
    plt.show()

    while cola:  # Mientras la cola no esté vacía
        costo_actual, nodo_actual = heapq.heappop(cola)  # Obtén el nodo con el menor costo actual

        if costo_actual > distancias[nodo_actual]:  # Si el costo actual es mayor que la distancia almacenada
            continue  # Salta a la siguiente iteración

        for vecino in grafo.neighbors(nodo_actual):  # Itera sobre los vecinos del nodo actual
            costo = grafo[nodo_actual][vecino]['weight']  # Obtiene el costo de la arista hacia el vecino
            nuevo_costo = distancias[nodo_actual] + costo  # Calcula el nuevo costo desde el origen hasta el vecino

            if nuevo_costo < distancias[vecino]:  # Si el nuevo costo es menor que la distancia almacenada
                distancias[vecino] = nuevo_costo  # Actualiza la distancia más corta al vecino
                heapq.heappush(cola, (nuevo_costo, vecino))  # Agrega el vecino a la cola de prioridad

    return distancias  # Devuelve las distancias más cortas


# Función principal que solicita al usuario la estación de salida, calcula las mejores rutas desde esa estación
#utilizando el algoritmo de Dijkstra, y muestra los resultados.

def main():
 
    archivo_rutas = 'Rutas.txt'  # Nombre del archivo de rutas
    grafo = leer_archivo_rutas(archivo_rutas)  # Lee el archivo y construye el grafo

    print("Estaciones disponibles:")
    print(list(grafo.nodes()))  # Muestra la lista de estaciones disponibles

    estacion_salida = input("Ingrese la estación de salida: ").strip()  # Solicita la estación de salida al usuario

    if estacion_salida not in grafo.nodes():  # Verifica si la estación de salida es válida
        print("Estación de salida no válida.")  # Muestra un mensaje de error y termina la ejecución
        return

    distancias_desde_origen = dijkstra(grafo, estacion_salida)  # Calcula las distancias más cortas desde la estación de salida

    print("\nMejores rutas desde", estacion_salida)  # Muestra un encabezado con la estación de salida
    for destino, costo in distancias_desde_origen.items():  # Itera sobre las distancias más cortas
        if destino != estacion_salida and costo != float('inf'):  # Verifica que no sea la estación de salida y que el costo no sea infinito
            print(f"Hacia {destino}: Costo = {costo}")  # Muestra la mejor ruta y su costo

main()  # Llama a la función principal