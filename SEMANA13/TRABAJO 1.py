def calcular_temperatura_promedio(datos_temperatura):
    """
    Calcula la temperatura promedio de cada ciudad en el período de tiempo dado.
    :param datos_temperatura: Diccionario con los datos de temperatura por ciudad y semanas.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}

    for ciudad, semanas in datos_temperatura.items():
        total_temperaturas = sum(sum(semana) for semana in semanas)
        total_dias = sum(len(semana) for semana in semanas)
        promedios[ciudad] = total_temperaturas / total_dias if total_dias > 0 else 0

    return promedios


# Datos de temperatura para 3 ciudades (Macas, Cuenca y Quito) durante 4 semanas
# Cada sublista representa una semana con temperaturas diarias

datos_temperatura = {
    "Macas": [
        [22, 24, 23, 25, 26, 24, 23],
        [21, 23, 22, 24, 25, 23, 22],
        [20, 22, 21, 23, 24, 22, 21],
        [19, 21, 20, 22, 23, 21, 20]
    ],

    "Cuenca": [
        [15, 17, 16, 18, 19, 17, 16],
        [14, 16, 15, 17, 18, 16, 15],
        [13, 15, 14, 16, 17, 15, 14],
        [12, 14, 13, 15, 16, 14, 13]
    ],

    "Quito": [
        [18, 20, 19, 21, 22, 20, 19],
        [17, 19, 18, 20, 21, 19, 18],
        [16, 18, 17, 19, 20, 18, 17],
        [15, 17, 16, 18, 19, 17, 16]
    ]
}

# Calcular temperaturas promedio
promedios = calcular_temperatura_promedio(datos_temperatura)

# Mostrar resultados
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio:.2f}°C")
