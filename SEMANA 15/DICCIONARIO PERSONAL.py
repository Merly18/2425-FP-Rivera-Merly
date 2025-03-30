# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Merly Rivera",
    "edad": 18,
    "ciudad": "Macas",
    "profesion": "Arquitecta"
}

# Acceder y modificar la ciudad
informacion_personal["ciudad"] = "Cuenca"

# Agregar una nueva clave-valor para la profesión (ya existe, pero podríamos actualizarla)
informacion_personal["Igennieria en sistemas"] = ""

# Verificar si "telefono" existe en el diccionario y agregarlo si no está presente
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0989191430"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
