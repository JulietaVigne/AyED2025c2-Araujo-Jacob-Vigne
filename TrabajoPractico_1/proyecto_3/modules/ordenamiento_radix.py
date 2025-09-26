from random import randint
def obtener_digito(numero, posicion_digito, base = 10):
    """
    Obtiene el dígito en la posición especificada (de derecha a izquierda) de un número.
    Devuelve cero si la posición es mayor que el número de dígitos del número.
    """
    return (numero // (base ** posicion_digito)) % base

def ordenamiento_radix(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento Radix.
    """
    # Encuentra el número máximo para determinar el número de dígitos
    max_num = max(lista)
    exp = 1  # Exponente para la posición del dígito
    lista_aux = [[] for _ in range(10)]  
    pos = 0  # Inicializa la posición del dígito
    while max_num // exp > 0:
        # Coloca los números en la lista auxiliar según el dígito actual
        for num in lista:
            digit = obtener_digito(num, pos)  # Obtiene el dígito en la posición actual
            lista_aux[digit].append(num)

        # Reconstruye la lista original a partir de la lista auxiliar
        sig_pos = 0  # Inicializa la posición en la lista original
        for sublist in lista_aux:
            for num in sublist:
                lista[sig_pos] = num  # Añade el número a la lista original 
                sig_pos += 1    


        # Limpia la lista auxiliar para la siguiente posición de dígito
        lista_aux = [[] for _ in range(10)]

        # Aumenta el exponente para pasar al siguiente dígito
        exp *= 10
        pos += 1
 
 
    return lista

if __name__ == "__main__":
    def lista_500():
        lista = []
        for _ in range(500):
            lista.append(randint(10000, 99999))
        return lista

    lista_prueba = lista_500()
    lista_copia = lista_prueba.copy()
    ordenamiento_radix(lista_prueba)
    lista_sorted = sorted(lista_copia)

    if lista_prueba == lista_sorted:
        print("¡El ordenamiento Radix funciona correctamente!")
    else:
        print("El ordenamiento Radix NO funciona correctamente.")


