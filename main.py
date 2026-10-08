archivo = open("diario.txt", "a")
# se abre el archivo del diario en modo "append"

archivo.write(input("¿Cómo te sientes hoy?: "))	# Solicita el contenido de la entrada al usuario y la agrega
archivo.close()