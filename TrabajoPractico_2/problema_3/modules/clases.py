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
            if self.listaMonticulo[i][0] < self.listaMonticulo[i // 2][0]:
                self.listaMonticulo[i], self.listaMonticulo[i // 2] = self.listaMonticulo[i // 2], self.listaMonticulo[i]
            i = i // 2
        
      def eliminarminimo(self):
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
            if self.listaMonticulo[i][0] > self.listaMonticulo[mc][0]:
                self.listaMonticulo[i], self.listaMonticulo[mc] = self.listaMonticulo[mc], self.listaMonticulo[i]
            i = mc

      def hijoMenor(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2][0] < self.listaMonticulo[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

      def minimo(self):
        if self.tamanoActual == 0:
            return None
        return self.listaMonticulo[1]

      def decrementarClave(self, elemento_viejo, elemento_nuevo):
       
    #"""Reemplaza elemento_viejo por elemento_nuevo y lo mueve hacia arriba (decrease-key).
    #Búsqueda O(n) del elemento y percolate-up O(log n). No requiere diccionario de posiciones."""
    # Busco la posición (índice) del elemento_viejo en la lista interna (saltando índice 0)
        indice= None
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == elemento_viejo:
                indice = i
                break
        # Si no lo encontré, informo el error al llamador
        if indice is None:
            raise KeyError("elemento a decrementar no está en el montículo")
        if elemento_nuevo>self.listaMonticulo[indice][0]:
            raise ValueError("el nuevo elemento es mayor que el elemento viejo")
        self.listaMonticulo[indice] = (elemento_nuevo, elemento_viejo)
        self.infiltArriba(indice)
        # Reemplazo el valor antiguo por el nuevo en la misma posición
        # self.listaMonticulo[indice][1] = elemento_nuevo
        # # Mientras no esté en la raíz y el nuevo sea menor que su padre, lo subo (percolate-up)
        # while indice > 1 and self.listaMonticulo[indice] < self.listaMonticulo[indice // 2]:
        #     # Intercambio con el padre
        #     self.listaMonticulo[indice], self.listaMonticulo[indice // 2] = self.listaMonticulo[indice // 2], self.listaMonticulo[indice]
        #     # Actualizo el índice al del padre para seguir subiendo si hace falta
        #     indice //= 2
            
      def __contains__(self, elemento):
        for i in range(1, self.tamanoActual + 1):
            if self.listaMonticulo[i][1] == elemento:
                return True
        return False
    
      def estavacio(self):
            """Devuelve True si el montículo está vacío."""
            return self.tamanoActual == 0