# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from random import randint
import time

#LISTA PARA PRUEBAS
def lista_500():
    lista = []
    for _ in range(500):
        lista.append(randint(10000, 99999))
    return lista
#HACEMOS EL ORDENAMIENTO BURBUJA


ordenamiento_burbuja=ordenamientoBurbuja(unaLista)
#print(unaLista)
# ordenamiento_sorted = sorted(unaLista)

#TIEMPO Y GRAFICACIÓN
tiempos_burbuja= []
tiempos_quicksort=[]
tiempos_residuos= []

contador = 0
for _ in range(n):
    inicio = time.perf_counter()
    ordenamiento_burbuja(unaLista)
    fin = time.perf_counter()
    contador += (fin - inicio)
tiempos_burbuja.append(contador)

contador = 0
for _ in range(n):
    inicio = time.perf_counter()
    lde.copiar()
    fin = time.perf_counter()
    contador += (fin - inicio)
tiempos_quicksort.append(contador)

contador = 0
for _ in range(n):
    inicio = time.perf_counter()
    lde.invertir()
    fin = time.perf_counter()
    contador += (fin - inicio)
tiempos_residuos.append(contador)
# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanos, tiempos_burbuja, marker='o', label="Método len - O(1)", color='green')
plt.plot(tamanos, tiempos_quicksort, marker='o', label="Método invertir- O(n)", color='purple')
plt.plot(tamanos, tiempos_residuos, marker='o', label="Método copiar - O(n)", color='red')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de métodos len, copiar e insertar en LDE')
plt.legend()
plt.grid()
plt.show()