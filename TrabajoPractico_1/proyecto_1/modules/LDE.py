# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Nodo: #creamos los nodos
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
        
class ListaDobleEnlazada: #creamos la clase LDE
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.tamanio=0
        
#creamos las funciones     
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar_al_inicio(self,dato):
        nuevo_nodo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo_nodo
            self.cabeza=nuevo_nodo
        self.tamanio+=1

    def agregar_al_final(self,dato):
        nuevo_nodo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.anterior=self.cola
            self.cola.siguiente=nuevo_nodo
            self.cola=nuevo_nodo
        self.tamanio+=1
        
    def insertar(self,dato,posicion):
        if posicion<0 or posicion >self.tamanio:
            raise Exception("Posición inválida") 
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo=Nodo(dato)
            actual=self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
        
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1
    
    def extraer(self,posicion=None):
        if posicion is None:
            posicion=self.tamanio-1
        elif posicion < 0:
            posicion=self.tamanio+posicion
            if posicion <0: 
                raise Exception("Posición inválida")    
        if self.esta_vacia():
            raise Exception("La lista está vacía")
        if posicion >self.tamanio:
            raise Exception("Posición inválida") 
        if posicion==0:
            nodo_a_extraer = self.cabeza
            dato = nodo_a_extraer.dato
            self.cabeza = nodo_a_extraer.siguiente
            if self.cabeza is not None:
               self.cabeza.anterior = None
            else:
               self.cola = None
        elif posicion==self.tamanio-1:  #extrae la cola osea extrae extremos
            nodo_a_extraer = self.cola
            dato = nodo_a_extraer.dato
            self.cola = nodo_a_extraer.anterior
            if self.cola is not None:
               self.cola.siguiente = None
            else:
                self.cabeza = None
        
        else:
            actual=self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato=actual.dato    
            actual.anterior.siguiente=actual.siguiente
            actual.siguiente.anterior=actual.anterior
        self.tamanio -= 1    
        return dato
    
    def copiar(self):
        copia=ListaDobleEnlazada() 
        actual=self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual=actual.siguiente
        return copia
    
    def invertir(self): #falta ver las exepciones
        actual=self.cabeza
        while actual is not None:
            actual.siguiente,actual.anterior=actual.anterior,actual.siguiente
            actual=actual.anterior
        self.cabeza,self.cola=self.cola,self.cabeza #para hacerlo a la vez
        
    def concatenar (self,lista): #falta ver las exepciones
        # Recibe una lista como argumento y retorna la lista actual 
        # con la lista pasada como parámetro concatenada al final de la primera.
        if self.esta_vacia():
            self.cabeza=lista.cabeza
            self.cola=lista.cola
            self.tamanio=lista.tamanio
            return self 
        elif lista.esta_vacia():
            return self
        self.cola.siguiente=lista.cabeza
        lista.cabeza.anterior=self.cola
        self.cola=lista.cola
        lista.cabeza.anterior=None
        self.cola.siguiente=None
        self.tamanio+=lista.tamanio
        return self
    
    def __len__(self):#PREGUNTAR PARAMETRO
        return self.tamanio
    
    def __add__(self,lista1):
        lista_nueva=ListaDobleEnlazada()
        lista_nueva= self.concatenar(lista1)
        return (lista_nueva)
    
    def __iter__(self): #PREGUNTAR PARAMTERO
        actual=self.cabeza
        lista=[]
        for _ in range(self.tamanio):
            lista.append(actual.dato)
            actual=actual.siguiente
        return lista 

    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

if __name__ == "__main__":
        
    #PRUEBAS DE USO

    lista1=ListaDobleEnlazada()
    lista2=ListaDobleEnlazada()

    #AGREGAR ELEMENTOS
    #Agregar al inicio
    lista1.agregar_al_inicio(10)
    lista1.agregar_al_inicio(20)
    lista1.agregar_al_inicio(30)

     #Agregar al final

    lista1.agregar_al_final(40)
    lista1.agregar_al_final(50)

    print("Lista despues de agregar al inicio y al final:")
    print(lista1)

    lista1.esta_vacia()
    print("¿La lista está vacía?", lista1.esta_vacia())

    lista1.insertar(26,3)
    print(lista1)

    lista1.extraer(4)
    print(lista1)  
    lista1.copiar()
    print(lista1)

    lista1.invertir()
    print(lista1)
    for _ in range(3):
        lista2.agregar_al_inicio(_)
    print(lista2)    
    # lista1.concatenar(lista2)
    # print(lista1)

    print(lista1.__len__())
    lista1
    lista1.__add__(lista2)
    print(lista1)
