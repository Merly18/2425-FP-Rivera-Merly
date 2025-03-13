# Definimos una función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    # Recorremos la matriz fila por fila
    for i in range(len(matriz)):
        # Recorremos cada columna de la fila actual
        for j in range(len(matriz[i])):
            # Si encontramos el valor en la matriz
            if matriz[i][j] == valor:
                return i, j  # Devolvemos la posición (fila, columna)
    return None  # Si no se encuentra, retornamos None

# Definimos una matriz 3x3 con números
matriz = [
    [5, 8, 2],  # Primera fila
    [3, 7, 6],  # Segunda fila
    [9, 1, 4]   # Tercera fila
]

# Pedimos al usuario que ingrese un número a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Llamamos a la función para buscar el valor en la matriz
resultado = buscar_valor(matriz, valor_buscado)

# Verificamos si el valor fue encontrado
if resultado:
    print(f"El valor {valor_buscado} se encontró en la posición {resultado}")
else:
    print(f"El valor {valor_buscado} no está en la matriz.")
