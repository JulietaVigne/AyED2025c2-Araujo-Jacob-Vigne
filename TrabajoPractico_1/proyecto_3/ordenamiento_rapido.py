# -*- coding: utf-8 -*-
from random import randint
def ordenamientoRapido(unaLista):
   ordenamientoRapidoAuxiliar(unaLista, 0, len(unaLista)-1)


def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:

       puntoDivision = particion(unaLista,primero,ultimo)

       ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
       ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]

   marcaIzq = primero+1
   marcaDer = ultimo

   hecho = False
   while not hecho:

       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp

   return marcaDer

if __name__ == "__main__":
    def lista_500():
        lista = []
        for _ in range(500):
            lista.append(randint(10000, 99999))
        return lista

    lista_prueba = lista_500()
    lista_copia = lista_prueba.copy()
    ordenamientoRapido(lista_prueba)
    lista_sorted = sorted(lista_copia)

    if lista_prueba == lista_sorted:
        print("¡El ordenamiento Quicksort funciona correctamente!")
    else:
        print("El ordenamiento Quicksort NO funciona correctamente.")