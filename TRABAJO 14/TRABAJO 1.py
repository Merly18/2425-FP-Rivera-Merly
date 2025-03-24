def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento a partir del monto total de la compra y un porcentaje de descuento.
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamadas a la función
monto1 = 100  # Ejemplo de monto total de la compra
monto2 = 200  # Otro ejemplo con un monto diferente

# Primera llamada con solo el monto total (se usa el descuento por defecto del 10%)
descuento1 = calcular_descuento(monto1)
print(f"Descuento para ${monto1}: ${descuento1}")

# Segunda llamada con el monto total y un porcentaje de descuento personalizado
descuento2 = calcular_descuento(monto2, 20)  # Aplicando un 20% de descuento
print(f"Descuento para ${monto2} con 20%: ${descuento2}")