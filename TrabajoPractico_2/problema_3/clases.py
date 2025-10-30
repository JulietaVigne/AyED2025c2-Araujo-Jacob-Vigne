# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Monticulo:
    def __init__(self, key=None):
        self.lista = [None]
        self.tam = 0
        # key: función que dado un elemento devuelve el valor a comparar. Por defecto identidad.
        self.key = (key if key is not None else (lambda x: x))


    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def _menor(self, a, b):
        return self.key(a) < self.key(b)    
    
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
        self.lista[1] = self.lista[self.tam]
        self.lista.pop()
        self.tam -= 1
        if self.tam > 0:
            self._infiltAbajo(1)
        return minimo

    def _infiltAbajo(self, i):
        while (i * 2) <= self.tam:
            hijo = i * 2
            if hijo + 1 <= self.tam and self._menor(self.lista[hijo + 1], self.lista[hijo]):
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
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def minimo(self):
        if self.tamanoActual == 0:
            return None
        return self.listaMonticulo[1]
    
    def estavacio(self):
        """Devuelve True si el montículo está vacío."""
        return self.tamano() == 0

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

class ColaDePrioridad:
    def __init__(self):
        self.monticulo = Monticulo()
        self.contador = 0

    def insertar_cola(self, elemento):
        self.contador += 1
        self.monticulo.insertar(elemento)

    def eliminar_cola(self):
        resultado = self.monticulo.eliminar_min()
        return resultado  # Devolver solo el elemento

    
    def primero(self):
        minimo = self.monticulo.minimo()
        if minimo:
            return minimo[2]
        return None
    
    def __len__(self):
        return self.monticulo.tamanoActual
   
    def __iter__(self):
        return iter(self.monticulo.listaMonticulo[1:])  # Saltea el primer elemento (0)

# if __name__ == "__main__":
#     from modules.paciente import Paciente 
#     cola = ColaDePrioridad()
#     cola.insertar_cola(Paciente())
#     cola.insertar_cola(Paciente())
#     cola.insertar_cola(Paciente())
#     print(cola.eliminar_cola())  # Debería imprimir 3
#     #print(cola.primero())        # Debería imprimir 5