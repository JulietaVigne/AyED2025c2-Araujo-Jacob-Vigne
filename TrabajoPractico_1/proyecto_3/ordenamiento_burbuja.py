# -*- coding: utf-8 -*-
from random import randint
def ordenamientoBurbuja(unaLista):
    for extremo in range(len(unaLista)-1,0,-1):
        for i in range(extremo):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
                
if __name__ == "__main__":
    def lista_500():
        lista = []
        for _ in range(500):
            lista.append(randint(10000, 99999))
        return lista

    lista_prueba = lista_500()
    lista_copia = lista_prueba.copy()
    ordenamientoBurbuja(lista_prueba)
    lista_sorted = sorted(lista_copia)
    
    if lista_prueba == lista_sorted:
        print("¡El ordenamiento burbuja funciona correctamente!")
    else:
        print("El ordenamiento burbuja NO funciona correctamente.")
# Ejercicio:
#   Mejorar el algoritmo para que detecte si la lista 
#   ya se encuentra ordenada.
