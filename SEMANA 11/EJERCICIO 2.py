# Definimos la función de ordenamiento usando Bubble Sort
def bubble_sort(lista):  # La función recibe una lista como parámetro
    n = len(lista)  # Obtenemos la cantidad de elementos en la lista
    for i in range(n - 1):  # Recorremos la lista (excepto el último elemento)
        for j in range(n - 1 - i):  # Comparamos elementos adyacentes
            if lista[j] > lista[j + 1]:  # Si el actual es mayor que el siguiente, los intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambiamos los valores

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [7, 8, 2],  # Fila 0
    [3, 7, 8],  # Fila 1
    [9, 2, 4]   # Fila 2
]

# Mostramos la matriz original antes de ordenar
print("Matriz original:")  # Mensaje para el usuario
for fila in matriz:  # Recorremos cada fila de la matriz
    print(fila)  # Imprimimos la fila actual

# Pedimos al usuario qué fila quiere ordenar
fila_a_ordenar = int(input("Ingrese el número de la fila a ordenar (0, 1 o 2): "))  # Convertimos la entrada a entero

# Verificamos que la fila ingresada sea válida
if 0 <= fila_a_ordenar < len(matriz):  # Si el número está entre 0 y 2 (incluidos)
    bubble_sort(matriz[fila_a_ordenar])  # Llamamos a la función para ordenar la fila seleccionada
else:  # Si el número es inválido
    print("Número de fila inválido.")  # Mostramos un mensaje de error

# Mostramos la matriz después de ordenar la fila seleccionada
print("\nMatriz con la fila ordenada:")  # Mensaje de salida
for fila in matriz:  # Recorremos nuevamente cada fila
    print(fila)  # Imprimimos la matriz actualizada
