# -*- coding: utf-8 -*-


class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0  # <-- Agregado


    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo


    def tieneHijoDerecho(self):
        return self.hijoDerecho


    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self


    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self


    def esRaiz(self):
        return not self.padre


    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)


    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo


    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo
   
#Operaciones auxiliares del Árbol AVL
    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
   
    def empalmar(self):
       if self.esHoja(): #si cumple esta condicion se elimina directamente
           if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
           else:
                self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo(): #si tiene un solo hijo, se lo conecta al padre
           if self.tieneHijoIzquierdo(): #si tiene hijo izquierdo, se conecta ese
                  if self.esHijoIzquierdo(): #si es hijo izquierdo, se conecta al padre por la izquierda, el sucesor es hijo izquierdo
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else: #si tiene hijo derecho, se conecta ese
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre


    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc


    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual
 
    def __iter__(self): #para iterar sobre el nodo y sus hijos con inorden
        if self.hijoIzquierdo:
            yield from self.hijoIzquierdo # Se ejecuta sobre el hijo izquierdo
        yield self.clave, self.cargautil # Devuelve la clave y la carga util del nodo
        if self.hijoDerecho:
            yield from self.hijoDerecho # Se ejecuta sobre el hijo derecho