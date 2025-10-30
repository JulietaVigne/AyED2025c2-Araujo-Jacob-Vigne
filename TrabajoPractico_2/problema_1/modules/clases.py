# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
class Monticulo:
    def __init__(self):
        self.listaMonticulo = [0]  
        self.tamanoActual = 0

    def insertar(self,k):
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
    
    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2
        
    def eliminar_min(self):
        if self.tamanoActual == 0:
            return None
        minimo = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.listaMonticulo.pop()
        self.tamanoActual -= 1
        self.infiltAbajo(1)
        return minimo

    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            mc = self.hijoMenor(i)
            if self.listaMonticulo[i] > self.listaMonticulo[mc]:
                self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]
            i = mc

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

if __name__ == "__main__":
    from modules.paciente import Paciente 
    cola = ColaDePrioridad()
    cola.insertar_cola(Paciente())
    cola.insertar_cola(Paciente())
    cola.insertar_cola(Paciente())
    print(cola.eliminar_cola())  # Debería imprimir 3
    #print(cola.primero())        # Debería imprimir 5