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
   
    def max_temp_rango(self, fecha1, fecha2):  # Devuelve la temperatura máxima en el rango [fecha1, fecha2] inclusive
        fecha1_convertida = self.convertir_fecha(fecha1)
        fecha2_convertida = self.convertir_fecha(fecha2)
        max_temp = float('-inf')
        # Recorre el árbol y filtra por rango
        for fecha, temp in self.arbol:
            if fecha1_convertida <= fecha <= fecha2_convertida:
                if temp > max_temp:
                    max_temp = temp
        return max_temp if max_temp != float('-inf') else None # Retorna None si no hay temperaturas en el rango


    def min_temp_rango(self, fecha1, fecha2):  # Devuelve la temperatura mínima en el rango [fecha1, fecha2] inclusive
        fecha1_convertida = self.convertir_fecha(fecha1)
        fecha2_convertida = self.convertir_fecha(fecha2)
        min_temp = float('inf')
        # Recorre el árbol y filtra por rango
        for fecha, temp in self.arbol:
            if fecha1_convertida <= fecha <= fecha2_convertida:
                if temp < min_temp:
                    min_temp = temp
        return min_temp if min_temp != float('inf') else None # Retorna None si no hay temperaturas en el rango

    def temp_extremos_rango(self, fecha1, fecha2):  # Devuelve una tupla (min, max) en el rango [fecha1, fecha2] inclusive
       fecha1_convertida = self.convertir_fecha(fecha1)
       fecha2_convertida = self.convertir_fecha(fecha2)
       min_temp = float('inf')
       max_temp = float('-inf')
       # Recorre el árbol y filtra por rango
       for fecha, temp in self.arbol:
           if fecha1_convertida <= fecha <= fecha2_convertida:
               if temp < min_temp:
                   min_temp = temp
               if temp > max_temp:
                   max_temp = temp
       if min_temp == float('inf') or max_temp == float('-inf'):
           return (None, None)  # Retorna (None, None) si no hay temperaturas en el rango
       return (min_temp, max_temp)

        
    def borrar_temperatura(self,fecha): #recibe una fecha y elimina del árbol la medición correspondiente a esa fecha.
        fecha_convertida= self.convertir_fecha(fecha)
        self.arbol.eliminar(fecha_convertida)  # Elimina el nodo del árbol AVL. Podemos agregarle return si queremos
    
    def devolver_temperaturas(self,fecha1, fecha2): #devuelve un listado de las mediciones de temperatura en el rango recibido por parámetro con el formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 
        fecha1_convertida= self.convertir_fecha(fecha1)
        fecha2_convertida= self.convertir_fecha(fecha2)
        lista = []
        
       # Recorre el árbol filtra por rango
        for fecha, temp in self.arbol:
           if fecha1_convertida <= fecha <= fecha2_convertida:
               fecha_str = fecha.strftime("%d/%m/%Y")
               lista.append(f"{fecha_str}: {temp} ºC")
        return lista  # Retorna la lista para que se pueda imprimir o usar
    
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


    # print("Cantidad de muestras en la base de datos:", temp.cantidad_muestras())
    # fecha_consulta = "15/03/2025"
    # temperatura = temp.devolver_temperatura(fecha_consulta)
    # print(temperatura)
   
#PROBAR TODOS LOS METODOS CREADOS
   
    #convertir_fecha
    # fecha_str="15/11/2025"
    # fecha_convertida=temp.convertir_fecha(fecha_str)
    # print(f"Entrada: {fecha_str}")
    # print(f"Salida: {fecha_convertida}, es de tipo {type(fecha_convertida)})")
   
    # #guardar temperatutra
    
    # print("datos guardados en el árbol:", temp.arbol)
   
    #devolver_temp
    #      #"consultar fecha inexistente"
    # fecha_inex="5/11/2025"
    # temperatura=temp.devolver_temperatura(fecha_inex)
    # print(f"Temperatura registrada el {fecha_ex}: {temperatura} °C")
   
    #      #"consultar fecha existente"
    # fecha_ex="2/04/2025"
    # temperaturaI=temp.devolver_temperatura(fecha_ex)
    # print(f"Temperatura registrada el {fecha_ex}: {temperatura}")
   
    #max_temp_rango, min, extremos
    # Consultas el rango de fechas
    # fecha_inicio = "5/04/2025"
    # fecha_fin = "29/04/2025"
    # # print("Temperaturas en rango:")
    # temp.devolver_temperaturas(fecha_inicio, fecha_fin)
    # print("Temperatura máxima en rango:", temp.max_temp_rango(fecha_inicio, fecha_fin), '°C')
    # print("Temperatura mínima en rango:", temp.min_temp_rango(fecha_inicio, fecha_fin), '°C')
    # print("Temperaturas extremas en rango:", temp.temp_extremos_rango(fecha_inicio, fecha_fin), '°C')
    # # Consultar cantidad de muestras
    # print("Cantidad de muestras:", temp.cantidad_muestras())


    # Borrar algunas temperaturas
    # Define fechas de inicio y fin para el rango (ajusta según tus datos)
    fecha_inicio ="6/04/2025"  # Ejemplo: 6 de abril de 2025
    fecha_fin = "20/04/2025"    # Ejemplo: 20
    
    # Borrar algunas temperaturas (verifica existencia)
    temp_borrada1 = temp.borrar_temperatura("8/04/2025")  # Retorna la temp borrada o None
    temp_borrada2 = temp.borrar_temperatura("14/04/2025")
    
    # Opcional: Imprime las temperaturas borradas --> none si anda bien
    print(f"Temperatura borrada en 8/04/2025: {temp_borrada1} °C")
    print(f"Temperatura borrada en 14/04/2025: {temp_borrada2} °C")
    
    # Se muestran las temperaturas después de borrar algunas
    print("Temperaturas después de borrar:")
    temp.devolver_temperaturas(fecha_inicio, fecha_fin)  # Pasa fechas válidas
    
    # Cantidad de muestras después de borrar
    print("Cantidad de muestras después de borrar:", temp.cantidad_muestras())