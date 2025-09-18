# -*- coding: utf-8 -*-
from random import randint
def RadixSort(unaLista, exponente=1):
    n = len(unaLista)
    arreglo = [0] * n  # arreglo de salida
    contador = [0] * 10  # para dígitos 0-9

    # Contar ocurrencias de dígitos en la posición exponente
    for i in range(n):
        indice = (unaLista[i] // exponente) % 10
        contador[indice] += 1

    # Cambiar contador[i] para que contenga la posición real de este dígito en arreglo
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    # Construir el arreglo de salida de derecha a izquierda para mantener estabilidad
    i = n - 1
    while i >= 0:
        indice = (unaLista[i] // exponente) % 10
        arreglo[contador[indice] - 1] = unaLista[i]
        contador[indice] -= 1
        i -= 1

    # Copiar el arreglo de salida a unaLista
    for i in range(n):
        unaLista[i] = arreglo[i]

def ordenamientoResiduos(unaLista):
    maximo = max(unaLista)
    exponente = 1
    while maximo // exponente > 0:
        RadixSort(unaLista, exponente)
        exponente *= 10

if __name__ == "__main__":
    def lista_500():
        lista = []
        for _ in range(500):
            lista.append(randint(10000, 99999))
        return lista

    lista_prueba = lista_500()
    lista_copia = lista_prueba.copy()
    ordenamientoResiduos(lista_prueba)
    lista_sorted = sorted(lista_copia)

    if lista_prueba == lista_sorted:
        print("¡El ordenamiento Residuo funciona correctamente!")
    else:
        print("El ordenamiento Residuo NO funciona correctamente.")
