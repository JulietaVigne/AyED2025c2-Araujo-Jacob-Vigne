# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Monticulo:
    def __init__(self, key=None):
        self.lista = [None]
        self.tamanoActual = 0
        # key: función que dado un elemento devuelve el valor a comparar. Por defecto identidad.
        self.key = (key if key is not None else (lambda x: x))


    def insertar(self,k):
        self.lista.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self._infiltArriba(self.tamanoActual)


#NO ME ANDA EN GRAFOS
    def _menor(self, a, b):
        try:
            if callable(self.key):
                return self.key(a) < self.key(b)
            elif isinstance(self.key, str):
                val_a = getattr(a, self.key)
                val_b = getattr(b, self.key)
                # Si son métodos, llamalos
                if callable(val_a): val_a = val_a()
                if callable(val_b): val_b = val_b()
                return val_a < val_b
            else:
                return a < b
        except AttributeError as e:
            raise RuntimeError(f"Error en _menor: uno de los elementos no tiene el atributo {self.key}") from e
        except Exception as e:
            raise RuntimeError(f"Error en _menor: {e}")

    
    def _infiltArriba(self, i):
        while i // 2 > 0:
            if self._menor(self.lista[i], self.lista[i // 2]):
                self.lista[i], self.lista[i // 2] = self.lista[i // 2], self.lista[i]
            i //= 2
    
    def _obtener_valor(self, elem,):
        if isinstance(self.key, str):
            attr = getattr(elem, self.key)
            return attr() if callable(attr) else attr
        if callable(self.key):
            return self.key(elem)
        return elem

    def _comparar(self, a, b):
        v1a = self._obtener_valor(a)
        v1b = self._obtener_valor(b)
        if v1a < v1b:
            return True
        elif v1a == v1b:
            return True # Para prim no importa el segundo parámetro
        else:
            return False
        
    def eliminarminimo(self):
        if self.estavacio():
            return None
        minimo = self.lista[1]
        self.lista[1] = self.lista[self.tamanoActual]
        self.lista.pop()
        self.tamanoActual -= 1
        if self.tamanoActual > 0:
            self._infiltAbajo(1)
        return minimo

    def _infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hijo = i * 2
            if hijo + 1 <= self.tamanoActual and self._menor(self.lista[hijo + 1], self.lista[hijo]):
                hijo += 1
            if self._menor(self.lista[hijo], self.lista[i]):
                self.lista[i], self.lista[hijo] = self.lista[hijo], self.lista[i]
                i = hijo
            else:
                break

    def hijoMenor(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.lista[i * 2] < self.lista[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def minimo(self):
        if self.tamanoActual == 0:
            return None
        return self.lista[1]
    
    def estavacio(self):
        """Devuelve True si el montículo está vacío."""
        return self.tamanoActual == 0

    def tamano(self):
        """Devuelve el número de elementos en el montículo."""
        # Mantener compatibilidad con ambos nombres de atributo
        return getattr(self, "tamanoActual", None) or getattr(self, "tam", 0)

    def construirMonticulo(self, unaLista, key=None):
        """
        Construye el montículo a partir de una lista.
        - unaLista: lista de elementos (no debe incluir el None inicial).
        - key: opcional, actualiza self.key si se proporciona.
        """
        if key is not None:
            self.key = key if (callable(key) or isinstance(key, str)) else (lambda x: x)
        # construir lista compartida para compatibilidad
        self.lista = [None] + unaLista[:]
        self.listaMonticulo = self.lista
        self.tam = len(unaLista)
        self.tamanoActual = len(unaLista)
        # Infiltrar desde la mitad hacia la raíz
        i = len(unaLista) // 2
        while i > 0:
            # usar el método que implementa infiltAbajo
            # algunos nombres usan _infiltAbajo, otros infiltAbajo; intentar ambos
            if hasattr(self, "_infiltAbajo"):
                self._infiltAbajo(i)
            elif hasattr(self, "infiltAbajo"):
                self.infiltAbajo(i)
            i -= 1
        
    def __contains__(self, elemento):
        """Verifica si un elemento está en el montículo."""
        # return elemento in self.lista[1:self.tamanoActual + 1][1]
        for i in range(1, self.tamanoActual + 1):
            if self.lista[i] == elemento:
                return True
        return False
        
    def __in__(self, dato):
     return dato in self.lista
    
    def decrementar_clave(self, dato, nuevo_valor): # Para vertices de grafos y prim
    # Busca el índice del dato
    # Cambia el valor de distancia de un vertice a nuevo_vertice
        for i in range(1, self.tam + 1):
            if self.lista[i] == dato:
                # Actualiza la distancia del vertice
                dato.asignar_distancia(nuevo_valor)
                self._infiltArriba(i) # Infiltra hacia arriba el vertice
                break

    def __iter__(self):
        return iter(self.lista[1:]) 
    

if __name__ == "__main__":
    monticulo1 = Monticulo()
    monticulo1.insertar(5)
    monticulo1.insertar(3)
    monticulo1.insertar(8)
    monticulo1.insertar(1)
    monticulo1.insertar(4)
    print(monticulo1.lista)  # Output: [None, 1, 3, 4, 5, 8]
    print(monticulo1.minimo())  # Output: 1
    monticulo1.eliminarminimo()
    print(monticulo1.lista)  # Output: [None, 3, 4, 5, 8]
    print(monticulo1.tamano())  # Output: 4
    monticulo2 = Monticulo()
    unalista = [7, 2, 6, 4, 1]
    monticulo2.construirMonticulo(unalista)
    print(monticulo2.tamano())  # Output: 5
    print(monticulo2.lista)  # Output: [None, 1, 2, 6, 4, 7]
    print(monticulo2.estavacio())  # Output: False
    print(20 in monticulo1)
