def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Devuelve la posición si se encuentra
    return None  # Retorna None si no se encuentra

# Definimos una matriz 3x3
matriz = [
    [4, 2, 3],
    [2, 9, 7],
    [7, 3, 9]
]

# Valor a buscar
valor_buscar = int(input("Ingrese el valor a buscar: "))

# Realizamos la búsqueda
posicion = buscar_valor(matriz, valor_buscar)

# Mostramos el resultado
if posicion:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")

