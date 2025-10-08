# -*- coding: utf-8 -*-
class NodoArbol:
    def __init__(self, clave, valor=None, izquierdo=None,derecho=None, padre=None):
        self.__clave = clave
        self.__valor = valor
        self.__hijo_izquierdo = izquierdo
        self.__hijo_derecho = derecho
        self.__padre = padre