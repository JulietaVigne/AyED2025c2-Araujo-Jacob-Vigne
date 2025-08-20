
class Nodo: #creamos los nodos
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None
        self.anterior=None
        
class ListaDoblementeEnlazada: #creamos la lista
    def __init__(self):
        self.cabeza=None
        self.cola=None
        self.tamanio=0
        
#creamos las funciones     
    def esta_vacia(self):
        return self.cabeza is None
    
    def _agregar_al_inicio(self,dato):
        nuevo_nodo=Nodo(dato)
        if self.cabeza is None:
            self.cabeza=nuevo_nodo
            self.cola=nuevo_nodo
        else:
            nuevo_nodo.siguiente=self.cabeza
            self.cabeza.anterior=nuevo_nodo
            self.cabeza=nuevo_nodo
        self.tamanio+=1

    def _agregar_al_final(self,dato):
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
    
    def extraer(self,posicion):
        if posicion<0 or posicion >self.tamanio:
            raise Exception("Posición inválida") 
        if posicion==None:
            #HAY QUE USR LO MISM,O QUE INSERTAR PARA UBICARNOS EN EL LUGAR CORRECTO
            
            
    def copiar(self):
        copia=ListaDobleEnlazada() 
        actual=self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual_dato)
            actual=actual.siguiente
        return copia
    
    