from matplotlib import pyplot as plt
from random import randint
import time
from modules.LDE import ListaDobleEnlazada


tamanos = [1000, 2000, 3000, 4000, 5000]

tiempos_len= []
tiempos_copiar=[]
tiempos_invertir= []

for n in tamanos:
    lde = ListaDobleEnlazada()
    for _ in range(n): 
        dato = randint(1, 100)
        lde.agregar_al_final(dato)
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        len(lde)
        fin = time.perf_counter()
        contador += (fin - inicio)
    tiempos_len.append(contador)

    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        lde.copiar()
        fin = time.perf_counter()
        contador += (fin - inicio)
    tiempos_copiar.append(contador)
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        lde.invertir()
        fin = time.perf_counter()
        contador += (fin - inicio)
    tiempos_invertir.append(contador)
    
# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_len, marker='o', label="Método len - O(1)", color='green')
plt.plot(tamanos, tiempos_invertir, marker='o', label="Método invertir- O(n)", color='purple')
plt.plot(tamanos, tiempos_copiar, marker='o', label="Método copiar - O(n)", color='red')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de métodos len, copiar e insertar en LDE')
plt.legend()
plt.grid()
plt.show()
