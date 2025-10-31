from clases import Monticulo
#del libro hasta obtenerPonderacion
class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {} # Diccionario de adyacencias
        # Atributos extra para la implementacion de prim
        self.distancia = float('inf')  # Incicialmente infinita, distancia al predecesor
        self.predecesor = None  # 
        
    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])# Representacion del vertice en string

    def obtenerConexiones(self):
        return self.conectadoA.keys() # Devuelve los vertices vecinos

    def obtenerId(self):
        return self.id # Clave del vertice

    def obtenerPonderacion(self,vecino):
        return self.conectadoA.get(vecino,float('inf')) # Ponderacion de la arista hacia un vecino especifico Esto evita un KeyError si se pide una conexión inexistente (mejor manejo de excepciones).

    def obtenerconectados(self):
        return self.conectadoA # Devuelve el diccionario de adyacencias (vertices vecinos y sus ponderaciones)

    def asignar_distancia(self, distancia):
        self.distancia = distancia

    def obtener_distancia(self): #Una vez expresado el arbol de expansion minima, devuelve la distancia al predecesor
        return self.distancia
    
    def asignar_predecesor(self, predecesor):   
        self.predecesor = predecesor # Será un objeto Vertice

    def obtener_predecesor(self):  
        return self.predecesor


class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1 # Incrementa el numero de vertices
        nuevoVertice = Vertice(clave) # Crea un nuevo vertice
        self.listaVertices[clave] = nuevoVertice # Lo agrega al diccionario de vertices
        return nuevoVertice

    def obtenerVertice(self,n): 
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices: #creo el vertice si no existe
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def existe_vertice(self, vertice):
        return vertice.id in [v for v in self.listaVertices]
    
    def obtenerAristas(self): # Devuelve una lista de tuplas (de, a, costo) para todas las aristas del grafo
        aristas = []
        for v in self.listaVertices.values():
            for vecino, ponderacion in v.obtenerconectados().items():
                aristas.append((v.obtenerId(), vecino.obtenerId(), ponderacion))
        return aristas

# def prim(G, inicio):  # Algoritmo de Prim para encontrar el árbol de expansión mínima
#     cp = Monticulo(key="obtener_distancia")  # Usa el key directamente
#     for v in G:
#         v.asignar_distancia(float("inf"))
#         v.asignar_predecesor(None)
#     inicio.asignar_distancia(0)
#     cp.construirMonticulo([v for v in G]) 
#     while not cp.estavacio():
#         vertice_actual = cp.eliminarminimo()  
#         for siguiente in vertice_actual.obtenerConexiones(): 
#             nuevo_costo = vertice_actual.obtenerPonderacion(siguiente)
#             if siguiente in cp and nuevo_costo < siguiente.obtener_distancia():
#                 siguiente.asignar_distancia(nuevo_costo)
#                 siguiente.asignar_predecesor(vertice_actual)
#                 cp.decrementar_clave(siguiente, nuevo_costo)

def prim(G, inicio):  # Algoritmo de Prim para encontrar el árbol de expansión mínima
    cp = Monticulo(key="obtener_distancia")  # Usa el key directamente
    for v in G:
        v.asignar_distancia(float("inf"))
        v.asignar_predecesor(None)
    inicio.asignar_distancia(0)
    cp.construirMonticulo([v for v in G])
    while not cp.estavacio():
        try:
            vertice_actual = cp.eliminarminimo()
        except Exception as e:
            break

        if vertice_actual is None:
            break

        for siguiente in vertice_actual.obtenerConexiones():
            try:
                nuevo_costo = vertice_actual.obtenerPonderacion(siguiente)
            except Exception as e:
                try:
                    vid = vertice_actual.obtenerId()
                    sid = siguiente.obtenerId()
                except Exception:
                    vid = str(vertice_actual); sid = str(siguiente)
                print(f"Error obteniendo ponderación {vid}->{sid}: {e}")
                continue

            try:
                pertenencia = (siguiente in cp)
            except Exception as e:
                print(f"Error comprobando pertenencia en montículo para {getattr(siguiente,'obtenerId',lambda: str(siguiente))()}: {e}")
                pertenencia = False

            if pertenencia:
                try:
                    if nuevo_costo < siguiente.obtener_distancia():
                        siguiente.asignar_distancia(nuevo_costo)
                        siguiente.asignar_predecesor(vertice_actual)
                        try:
                            cp.decrementar_clave(siguiente, nuevo_costo)
                        except Exception as e:
                            print(f"Error en decrementar_clave para {getattr(siguiente,'obtenerId',lambda: str(siguiente))()}: {e}")
                except Exception as e:
                    print(f"Error actualizando vecino {getattr(siguiente,'obtenerId',lambda: str(siguiente))()}: {e}")

                
def distanciatotal(G): # Suma las distancias del árbol de expansión mínima
    total = 0
    for v in G:
        if v.obtener_predecesor() is not None:
            total += v.obtener_distancia()
    return total


def predecesores_sucesores_aldeas(G): # Imprime los predecesores y sucesores de cada aldea
    for v in G: # Itera sobre los vertices del grafo
        sucesores = []
        predecesor = v.obtener_predecesor()
        for posibles_sucesores in G: # Itera sobre todos los vertices
            if posibles_sucesores.obtener_predecesor() == v: # Confirma si es el sucesor
                sucesores.append(posibles_sucesores.obtenerId()) # Agrega la clave del sucesor a la lista

        # Casos según existencia de predecesor y cantidad de sucesores
        if predecesor is None:
            if len(sucesores) == 0:
                print(f"La aldea {v.obtenerId()} empieza el recorrido y no debe enviar réplicas.")
            elif len(sucesores) == 1:
                print(f"La aldea {v.obtenerId()} empieza el recorrido y debe enviar réplicas a {sucesores[0]}.")
            else:
                print(f"La aldea {v.obtenerId()} empieza el recorrido y debe enviar réplicas a {', '.join(sucesores[:-1])} y {sucesores[-1]}.")
        else:
            if len(sucesores) == 0:
                print(f"La aldea {v.obtenerId()} recibe el mensaje desde {predecesor.obtenerId()} y no debe enviar réplicas.")
            elif len(sucesores) == 1:
                print(f"La aldea {v.obtenerId()} recibe el mensaje desde {predecesor.obtenerId()} y debe enviar réplicas a {sucesores[0]}.")
            else:
                print(f"La aldea {v.obtenerId()} recibe el mensaje desde {predecesor.obtenerId()} y debe enviar réplicas a {', '.join(sucesores[:-1])} y {sucesores[-1]}.")

if __name__ == "__main__":
    g = Grafo()
    for i in range(0,8):
        g.agregarVertice(i)

    g.agregarArista(0,4,8)
    g.agregarArista(4,0,8)
    g.agregarArista(3,0,8)
    g.agregarArista(0,3,8)
    g.agregarArista(3,5,1)
    g.agregarArista(5,3,1)
    g.agregarArista(3,7,6)
    g.agregarArista(7,3,6)
    g.agregarArista(7,6,1)
    g.agregarArista(6,7,1)
    g.agregarArista(7,4,1)
    g.agregarArista(4,7,1)
    g.agregarArista(5,2,8)
    g.agregarArista(2,5,8)
    g.agregarArista(2,1,1)
    g.agregarArista(1,2,1)
    g.agregarArista(2,6,6)
    g.agregarArista(6,2,6)

    prim(g, g.obtenerVertice(3))
    print("Árbol de expansión mínima:")
    for v in g:
        if v.obtener_predecesor() is not None:
            print(f"{v.obtener_predecesor().obtenerId()} - {v.obtenerId()} con costo {v.obtener_distancia()}")

    print(f"La distancia total es: {distanciatotal(g)}")
    print(g.obtenerVertices())