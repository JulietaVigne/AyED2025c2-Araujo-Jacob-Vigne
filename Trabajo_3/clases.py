# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Monticulo:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def insertar(self, k):
        self.listaMonticulo.append(k)
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual)

    def infiltArriba(self, i, param1=None, param2=None):
        while i // 2 > 0:
            padre = i // 2
            if param1 is not None:
                if self._comparar(self.listaMonticulo[i], self.listaMonticulo[padre], param1, param2):
                    self.listaMonticulo[i], self.listaMonticulo[padre] = self.listaMonticulo[padre], self.listaMonticulo[i]
            else:
                if self.listaMonticulo[i] < self.listaMonticulo[padre]:
                    self.listaMonticulo[i], self.listaMonticulo[padre] = self.listaMonticulo[padre], self.listaMonticulo[i]
            i = padre

    def eliminar_min(self):
        if self.tamanoActual == 0:
            return None
        minimo = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.listaMonticulo.pop()
        self.tamanoActual -= 1
        if self.tamanoActual > 0:
            self.infiltAbajo(1)
        return minimo

    def infiltAbajo(self, i, param1=None, param2=None):
        while (i * 2) <= self.tamanoActual:
            mc = self.hijoMenor(i, param1, param2)
            if param1 is not None:
                if self._comparar(self.listaMonticulo[mc], self.listaMonticulo[i], param1, param2):
                    self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]
            else:
                if self.listaMonticulo[i] > self.listaMonticulo[mc]:
                    self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]
            i = mc

    def hijoMenor(self, i, param1=None, param2=None):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            izq = i * 2
            der = i * 2 + 1
            if param1 is not None:
                if self._comparar(self.listaMonticulo[izq], self.listaMonticulo[der], param1, param2):
                    return izq
                else:
                    return der
            else:
                if self.listaMonticulo[izq] < self.listaMonticulo[der]:
                    return izq
                else:
                    return der

    def minimo(self):
        if self.tamanoActual == 0:
            return None
        return self.listaMonticulo[1]

    def _comparar(self, a, b, param1, param2):
        v1a = self._obtener_valor(a, param1)
        v1b = self._obtener_valor(b, param1)
        if v1a is None and v1b is None:
            return False
        if v1a is None:
            return False
        if v1b is None:
            return True
        if v1a < v1b:
            return True
        elif v1a == v1b:
            return True  # desempate simple; ajustar si se necesita usar param2
        else:
            return False

    def _obtener_valor(self, elem, param):
        if param is None:
            return elem
        if isinstance(param, str):
            attr = getattr(elem, param, None)
            if callable(attr):
                try:
                    return attr()
                except Exception:
                    return None
            else:
                return attr
        try:
            # intentar indexar (lista/tupla/dict)
            return elem[param]
        except Exception:
            return None

    def buscarminimo(self):
        if self.tamanoActual == 0:
            return None
        return self.listaMonticulo[1]

    def estavacio(self):
        return self.tamanoActual == 0

    def tamano(self):
        return self.tamanoActual

    def construirMonticulo(self, unaLista, param1=None, param2=None):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while i > 0:
            self.infiltAbajo(i, param1, param2)
            i -= 1

    def __contains__(self, dato):
        return dato in self.listaMonticulo

    def decrementar_clave(self, dato, nuevo_valor):
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i] == dato:
                if hasattr(dato, "asignar_distancia"):
                    try:
                        dato.asignar_distancia(nuevo_valor)
                    except Exception:
                        pass
                # infiltrar usando getters esperados; ajustar nombres si su objeto usa otros
                self.infiltArriba(i, "obtener_distancia", "obtenerId")
                break

    def __iter__(self):
        return iter(self.listaMonticulo[1:])
# pruebas rápidas para ejecutar desde la terminal: python clases.py
if __name__ == "__main__":
    print("Pruebas rápidas de Monticulo")

    m = Monticulo()
    for x in [5, 3, 8, 1, 6]:
        m.insertar(x)
    salida = []
    while not m.estavacio():
        salida.append(m.eliminar_min())
    print("Orden esperado (enteros):", salida)  # debería ser [1,3,5,6,8]

    # prueba con objetos que usan obtener_distancia
    class DummyV:
        def __init__(self, id, dist):
            self.id = id
            self.distancia = dist
        def obtener_distancia(self):
            return self.distancia
        def asignar_distancia(self, d):
            self.distancia = d
        def obtenerId(self):
            return self.id
        def __repr__(self):
            return f"V({self.id},d={self.distancia})"

    v1 = DummyV("A", 10)
    v2 = DummyV("B", 5)
    v3 = DummyV("C", 7)

    m2 = Monticulo()
    m2.construirMonticulo([v1, v2, v3], param1="obtener_distancia")
    orden = []
    while not m2.estavacio():
        orden.append(m2.eliminar_min())
    print("Orden esperado (objetos por distancia):", orden)  # B, C, A

    # probar decrementar_clave
    v4 = DummyV("D", 20)
    v5 = DummyV("E", 15)
    m3 = Monticulo()
    m3.construirMonticulo([v4, v5], param1="obtener_distancia")
    print("Antes decrementar:", list(m3))
    m3.decrementar_clave(v4, 2)  # baja la distancia de D a 2
    print("Después decrementar y extraer:", [m3.eliminar_min(), m3.eliminar_min()])