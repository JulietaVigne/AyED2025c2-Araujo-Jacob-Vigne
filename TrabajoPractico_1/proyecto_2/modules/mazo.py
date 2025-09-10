from modules.LDE import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass
class Mazo:
    def __init__(self):
        self.mazos = ListaDobleEnlazada()

#Poner arriba al momento de repartir las cartas, sacar arriba al momento de jugar el turno
#Poner abajo al momento de ganar el turno

    def poner_carta_arriba(self,carta): 
        self.mazos.agregar_al_inicio(carta)
    
    def sacar_carta_arriba(self,mostrar=None):
        if self.mazos.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        carta_juego= self.mazos.extraer(0)
        if mostrar:
            carta_juego.visible = True
            return carta_juego
        else:
          return carta_juego
    
    def poner_carta_abajo(self,carta):
        self.mazos.agregar_al_final(carta)
    
    def __len__(self):
        return self.mazos.tamanio

if __name__ == "__main__":
    #PRUEBAS DE USO
    mazo = Mazo()
    carta1 = Carta('3','♣')
    carta2 = Carta('5','♥')
    carta3 = Carta('7','♦')
    mazo.poner_carta_arriba(carta1)
    mazo.poner_carta_arriba(carta2) 
    mazo.poner_carta_abajo(carta3)
    print(mazo.mazos)
    print(mazo.sacar_carta_arriba())
    