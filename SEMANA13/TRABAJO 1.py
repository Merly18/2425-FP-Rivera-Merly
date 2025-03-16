def calcular_temperatura_promedio(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad.
    :param datos_temperaturas: Diccionario con ciudades como claves y listas de temperaturas semanales como valores.
    :return: Diccionario con la temperatura promedio de cada ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos_temperaturas.items():
        total_temperaturas = sum(temperaturas)
        cantidad_datos = len(temperaturas)
        promedio = total_temperaturas / cantidad_datos if cantidad_datos > 0 else 0
        promedios[ciudad] = round(promedio, 2)
    return promedios

# Datos de temperaturas (simulados para 4 semanas)
datos_temperaturas = {
    "Macas": [22.5, 23.1, 21.8, 22.9, 23.5, 22.7, 21.9,
               22.8, 23.0, 21.7, 22.5, 23.3, 22.6, 22.0,
               23.2, 22.9, 21.5, 22.6, 23.4, 22.3, 22.1,
               22.7, 23.1, 21.8, 22.9, 23.2, 22.5, 21.9],
    "Cuenca": [18.5, 19.1, 17.8, 18.9, 19.5, 18.7, 17.9,
                18.8, 19.0, 17.7, 18.5, 19.3, 18.6, 18.0,
                19.2, 18.9, 17.5, 18.6, 19.4, 18.3, 18.1,
                18.7, 19.1, 17.8, 18.9, 19.2, 18.5, 17.9],
    "Quito": [15.5, 16.1, 14.8, 15.9, 16.5, 15.7, 14.9,
               15.8, 16.0, 14.7, 15.5, 16.3, 15.6, 15.0,
               16.2, 15.9, 14.5, 15.6, 16.4, 15.3, 15.1,
               15.7, 16.1, 14.8, 15.9, 16.2, 15.5, 14.9]
}

# Calcular temperatura promedio por ciudad
promedios = calcular_temperatura_promedio(datos_temperaturas)

# Mostrar resultados
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio en {ciudad}: {promedio}°C")

