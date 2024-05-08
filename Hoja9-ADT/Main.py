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