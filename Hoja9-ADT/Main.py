#HOJA DE TRABAJO #9 - ADT
#
#Dulce Ambrosio - 231143
#Daniel Chet - 231177


import networkx as nx 
import heapq 

def leer_archivo_rutas(archivo):
    grafo = nx.Graph()   

    with open(archivo, 'r') as file:  
        for linea in file:  
            origen, destino, costo = [s.strip().strip('"') for s in linea.split(',')]
            costo = int(costo)  
            grafo.add_edge(origen, destino, weight=costo)              
            grafo.add_edge(destino, origen, weight=costo)  
    return grafo