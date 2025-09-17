import random
from TrabajoPractico_1.proyecto_3.ordenamiento_burbuja import ordenamientoBurbuja

# test_ordenamiento_burbuja.py


def test_burbuja_random_5digit():
    lista = [random.randint(10000, 99999) for _ in range(500)]
    esperado = sorted(lista)
    ordenamientoBurbuja(lista)
    assert lista == esperado

def test_burbuja_empty():
    lista = []
    esperado = []
    ordenamientoBurbuja(lista)
    assert lista == esperado

def test_burbuja_one_element():
    lista = [12345]
    esperado = [12345]
    ordenamientoBurbuja(lista)
    assert lista == esperado

def test_burbuja_sorted():
    lista = [10000, 20000, 30000, 40000, 50000]
    esperado = [10000, 20000, 30000, 40000, 50000]
    ordenamientoBurbuja(lista)
    assert lista == esperado

def test_burbuja_reverse():
    lista = [50000, 40000, 30000, 20000, 10000]
    esperado = [10000, 20000, 30000, 40000, 50000]
    ordenamientoBurbuja(lista)
    assert lista == esperado