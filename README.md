# 2425-FP-Rivera-Merly
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición (fila, columna)
    return None

# Definir una matriz 3x3
matriz = [
    [4, 2, 3],
    [2, 9, 7],
    [7, 3, 9]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")
