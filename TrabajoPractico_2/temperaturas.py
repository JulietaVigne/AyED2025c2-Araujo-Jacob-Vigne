# -*- coding: utf-8 -*-

from datetime import datetime
from modules.avl import ArbolAVL

class Temperaturas_DB:
    def __init__ (self):
        self.arbol = ArbolAVL() #aca le digo que es un dato tipo ArbolAVL
    def convertir_fecha (self,fecha): #convierte una fecha en formato "dd/mm/aaaa" a un objeto date.
        return datetime.strptime(fecha, "%d/%m/%Y").date() #lo hacemos para poder comparar fechas.
    
    def guardar_temperatura(self,temperatura, fecha): #guarda la medida de temperatura asociada a la fecha.
       fecha_convertida= self.convertir_fecha(fecha)
       self.arbol.agregar(fecha_convertida,temperatura)#agrega un nodo al arbol con la clave fecha y el valor temperatura.
        
    def devolver_temperatura(self,fecha): #devuelve la medida de temperatura en la fecha determinada.
        fecha_convertida= self.convertir_fecha(fecha)
        return self.arbol.obtener(fecha_convertida) #devuelve el valor asociado(temperatura) a la clave fecha.
    
    def max_temp_rango(self,fecha1, fecha2): #devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        fecha1_convertida= self.convertir_fecha(fecha1)
        fecha2_convertida= self.convertir_fecha(fecha2)
        max_temp = None
            
    def min_temp_rango(self,fecha1, fecha2): #devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2). Esto no implica que los intervalos del rango deban ser fechas incluidas previamente en el árbol.
        fecha1_convertida= self.convertir_fecha(fecha1)
        fecha2_convertida= self.convertir_fecha(fecha2)
    def temp_extremos_rango(self,fecha1, fecha2): #devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2).
        fecha1_convertida= self.convertir_fecha(fecha1)
        fecha2_convertida= self.convertir_fecha(fecha2)
        
    def borrar_temperatura(self,fecha): #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        fecha_convertida= self.convertir_fecha(fecha)
    def devolver_temperaturas(self,fecha1, fecha2): #devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        fecha1_convertida= self.convertir_fecha(fecha1)
        fecha2_convertida= self.convertir_fecha(fecha2)
    def cantidad_muestras(self): #devuelve la cantidad de muestras de la BD.
        return self.arbol.tamano