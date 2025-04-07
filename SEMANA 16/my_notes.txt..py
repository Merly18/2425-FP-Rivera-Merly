# Escritura de archivo de texto

# Creamos o abrimos el archivo "my_notes.txt" en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos al menos tres líneas de notas personales en el archivo
archivo.write("Primera nota: Estudiar para los examamenes.\n")
archivo.write("Segunda nota: Realizar todas los deberes pendientes.\n")
archivo.write("Tercera nota: Leer el libro de Boulevard.\n")

# Cerramos el archivo luego de escribir
archivo.close()

# Lectura de archivo de texto

# Abrimos el archivo "my_notes.txt" en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea usando readline() y lo mostramos
print("Contenido del archivo my_notes.txt:")
linea = archivo.readline()
while linea:
    print(linea.strip())  # .strip() elimina el salto de línea para que no se vea doble en consola
    linea = archivo.readline()

# Cerramos el archivo después de leer
archivo.close()
