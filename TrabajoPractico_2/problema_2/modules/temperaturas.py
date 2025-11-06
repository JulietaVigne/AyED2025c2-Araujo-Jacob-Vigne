#  -*- coding: utf-8 -*-

from datetime import datetime
from avl import ArbolAVL


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



if __name__ == "__main__":
    temp = Temperaturas_DB()
    # Cargar muestras desde archivo y guardarlas en el árbol
    with open("data/muestras.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            fecha, temperatura = linea.strip().split(";")
            temperatura = float(temperatura)
            temp.guardar_temperatura(temperatura, fecha)


    print("Cantidad de muestras en la base de datos:", temp.cantidad_muestras())
    fecha_consulta = "15/03/2025"
    temperatura = temp.devolver_temperatura(fecha_consulta)
    print(temperatura)
   
#PROBAR TODOS LOS METODOS CREADOS
   
    #convertir_fecha
    fecha_str="15/11/2025"
    fecha_convertida=temp.convertir_fecha(fecha_str)
    print(f"Entrada: {fecha_str}")
    print(f"Salida: {fecha_convertida}, es de tipo {type(fecha_convertida)})")
   
    #guardar temperatutra
    temp.guardar_temperatura(25.6,"5/11/2025")
    temp.guardar_temperatura(30.6,"5/11/2025")
    temp.guardar_temperatura(25.1,"7/11/2025")
    temp.guardar_temperatura(27.9,"10/11/2025")
    temp.guardar_temperatura(24.3,"20/11/2025")
    temp.guardar_temperatura(23.9,"14/11/2025")
    temp.guardar_temperatura(19.6,"8/11/2025")
    temp.guardar_temperatura(17.5,"29/11/2025")
    temp.guardar_temperatura(23.3,"6/11/2025")
    temp.guardar_temperatura(30.2,"9/11/2025")
    temp.guardar_temperatura(24.9,"13/11/2025")
    temp.guardar_temperatura(21.7,"15/11/2025")
    print("datos guardados en el árbol:", temp.arbol)
   
    #devolver_temp
         #"consultar fecha existente"
    fecha_ex="5/11/2025"
    temperatura=temp.devolver_temperatura(fecha_ex)
    print(f"Temperatura registrada el {fecha_ex}: {temp} °C")
   
         #"consultar fecha inexistente"
    fecha_inex="2/11/2025"
    temperaturaI=temp.devolver_temperatura(fecha_inex)
    print(f"Temperatura registrada el {fecha_inex}: {temp}")
   
    #max_temp_rango, min, extremos
    # Consultas el rango de fechas
    fecha_inicio = "5/11/2025"
    fecha_fin = "29/11/2025"
    print("Temperaturas en rango:")
    temp.devolver_temperaturas(fecha_inicio, fecha_fin)
    print("Temperatura máxima en rango:", temp.max_temp_rango(fecha_inicio, fecha_fin), '°C')
    print("Temperatura mínima en rango:", temp.min_temp_rango(fecha_inicio, fecha_fin), '°C')
    print("Temperaturas extremas en rango:", temp.temp_extremos_rango(fecha_inicio, fecha_fin), '°C')
    # Consultar cantidad de muestras
    print("Cantidad de muestras:", temp.cantidad_muestras())


    # Borrar algunas temperaturas
    temp.borrar_temperatura("8/11/2025")
    temp.borrar_temperatura("14/11/2025")


    # Se muestran las temperaturas después de borrar algunas
    print("Temperaturas después de borrar:")
    temp.devolver_temperaturas()


    # Cantidad de muestras después de borrar
    print("Cantidad de muestras después de borrar:", temp.cantidad_muestras())