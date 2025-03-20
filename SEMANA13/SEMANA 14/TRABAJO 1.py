def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Llamada 1: solo monto total, se usa el valor predeterminado de descuento (10%)
monto_total_1 = 200
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1
print(f"Monto total: {monto_total_1}, Descuento: {descuento_1}, Monto final a pagar: {monto_final_1}")

# Llamada 2: monto total y porcentaje de descuento proporcionados (15%)
monto_total_2 = 150
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2
print(f"Monto total: {monto_total_2}, Descuento: {descuento_2}, Monto final a pagar: {monto_final_2}")
