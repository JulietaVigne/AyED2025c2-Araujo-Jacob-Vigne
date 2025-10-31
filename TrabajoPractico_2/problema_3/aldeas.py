from grafos import*
import csv

with open("data/aldeas.txt", "r", encoding="utf-8") as archivo: #Abrimos el archivo de aldeas y volcamos su contenido en una lista
    lector = csv.reader(archivo)
    datos = []
    for fila in lector:
        if fila:  # Verifica que la fila no esté vacía
            datos.append([fila[0], fila[1].strip(), int(fila[2])]) # Convierte la distancia a entero y elimina espacios en blanco

grafo_aldeas = Grafo() # Crea un grafo vacío
for fila in datos: # Recorre cada fila de datos y agrega las aristas al grafo (se crean vértices si no existen)
    origen = fila[0]
    destino = fila[1]
    distancia = fila[2]
    grafo_aldeas.agregarArista(origen, destino, distancia) 
    
lista_aldeas = [] # Crea una lista para almacenar los nombres de las aldeas
for v in grafo_aldeas:
    lista_aldeas.append(v.id) # Añade el nombre de cada aldea a la lista
lista_aldeas = sorted(lista_aldeas) # Ordena alfabéticamente

prim(grafo_aldeas, grafo_aldeas.obtenerVertice("Peligros"))  # Inicia el algoritmo Prim desde la aldea "Peligros"

# Presentación de los resultados
print('\n--- Resultados del algoritmo ---')

print("\nAldeas en orden alfabético:")
for a in lista_aldeas:  # Imprime la lista de aldeas
    print(a)

print('\nRecorrido de los mensajes:')
predecesores_sucesores_aldeas(grafo_aldeas) # Imprime los predecesores y sucesores de cada vértice

print(f'\nLa suma de todas las distancias recorridas por todas las palomas enviadas desde cada palomar es de {distanciatotal(grafo_aldeas)} leguas\n')  # Imprime la distancia total del árbol de expansión mínima    