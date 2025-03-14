import random  # Importamos la librería para generar datos aleatorios

# Definimos las ciudades y los días de la semana
ciudades = ["Macas", "Cuenca", "Quito"]  # Tres ciudades
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]  # Días de la semana
semanas = 2  # Número de semanas

# Creamos la matriz 3D con temperaturas aleatorias entre 10 y 40 grados
# La estructura es [ciudades][semanas][días de la semana]
matriz_temperaturas = [[[random.randint(10, 40) for _ in dias] for _ in range(semanas)] for _ in ciudades]

# Mostramos la matriz generada con las temperaturas de cada ciudad para cada semana
print("Temperaturas registradas:")
for i, ciudad in enumerate(ciudades):  # Iteramos sobre las ciudades
    print(f"\nCiudad: {ciudad}")
    for s in range(semanas):  # Iteramos sobre las semanas
        print(f"  Semana {s+1}: {matriz_temperaturas[i][s]}")

# Calculamos y mostramos el promedio de temperatura por ciudad y semana
print("\nPromedios de temperatura por ciudad y semana:")
for i, ciudad in enumerate(ciudades):  # Iteramos sobre cada ciudad
    for s in range(semanas):  # Iteramos sobre cada semana
        promedio = sum(matriz_temperaturas[i][s]) / len(dias)  # Calculamos el promedio de la semana
        print(f"Ciudad {ciudad}, Semana {s+1}: {promedio:.2f}°C")  # Mostramos el promedio con 2 decimales
