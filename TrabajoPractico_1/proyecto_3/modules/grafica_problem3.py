# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from random import randint
import time

# Importa tus funciones de ordenamiento
from modules.ordenamiento_burbuja import ordenamientoBurbuja
from modules.ordenamiento_rapido import ordenamientoRapido
from modules.ordenamiento_radix import ordenamiento_radix  

# Tamaños de listas a probar
tamanos = list(range(1, 1000, 150))  

# Listas para guardar tiempos
tiempos_burbuja = []
tiempos_quicksort = []
tiempos_residuos = []

# Número de repeticiones para promediar tiempos
repeticiones = 5

for tamaño in tamanos:
    # Generar lista aleatoria para este tamaño
    lista_original = [randint(0, 100) for _ in range(tamaño)]

    # # --- Burbuja ---
    # tiempo_total = 0
    # for _ in range(repeticiones):
    #     lista = lista_original.copy()
    #     inicio = time.perf_counter()
    #     ordenamientoBurbuja(lista)
    #     fin = time.perf_counter()
    #     tiempo_total += (fin - inicio)
    # tiempos_burbuja.append(tiempo_total / repeticiones)

    # # --- Quicksort ---
    # tiempo_total = 0
    # for _ in range(repeticiones):
    #     lista = lista_original.copy()
    #     inicio = time.perf_counter()
    #     ordenamientoRapido(lista)
    #     fin = time.perf_counter()
    #     tiempo_total += (fin - inicio)
    # tiempos_quicksort.append(tiempo_total / repeticiones)

    # # --- Radix Sort (residuos) ---
    # tiempo_total = 0
    # for _ in range(repeticiones):
    #     lista = lista_original.copy()
    #     inicio = time.perf_counter()
    #     ordenamientoResiduos(lista)
    #     fin = time.perf_counter()
    #     tiempo_total += (fin - inicio)
    # tiempos_residuos.append(tiempo_total / repeticiones)
    
    inicio = time.perf_counter()
    ordenamientoBurbuja(lista_original.copy())
    fin = time.perf_counter()
    tiempos_burbuja.append(fin - inicio)
    
    inicio = time.perf_counter()
    ordenamiento_radix(lista_original.copy())
    fin = time.perf_counter()
    tiempos_residuos.append(fin - inicio)
    
    inicio = time.perf_counter()
    ordenamientoRapido(lista_original.copy())
    fin = time.perf_counter()
    tiempos_quicksort.append(fin - inicio)

# Graficar resultados
plt.figure(figsize=(12, 7))
plt.plot(tamanos, tiempos_burbuja, marker='o', label="Burbuja - O(n²)", color='green')
plt.plot(tamanos, tiempos_quicksort, marker='o', label="Quicksort - O(n log n)", color='purple')
plt.plot(tamanos, tiempos_residuos, marker='o', label="Radix Sort (residuos) - O(d·(n + k))", color='red')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo promedio (segundos)')
plt.title('Comparación de tiempos de ejecución de algoritmos de ordenamiento')
plt.legend()
plt.grid(True)
plt.show()
