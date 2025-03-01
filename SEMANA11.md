# 2425-FP-Rivera-Merly
def ordenar_fila_quick_sort(fila):
    if len(fila) <= 1:
        return fila
    else:
        pivote = fila[len(fila) // 2]
        menores = [x for x in fila if x < pivote]
        iguales = [x for x in fila if x == pivote]
        mayores = [x for x in fila if x > pivote]
        return ordenar_fila_quick_sort(menores) + iguales + ordenar_fila_quick_sort(mayores)

# Definir una matriz 3x3
matriz = [
    [4, 2, 3],
    [2, 9, 7],
    [7, 3, 9]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Seleccionar la fila a ordenar
fila_a_
ordenar = int(input("Ingrese el número de la fila a ordenar (0-2): "))

# Ordenar la fila seleccionada
if 0 <= fila_a_ordenar < len(matriz):
    matriz[fila_a_ordenar] = ordenar_fila_quick_sort(matriz[fila_a_ordenar])
else:
    print("Fila no válida.")

# Mostrar matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
