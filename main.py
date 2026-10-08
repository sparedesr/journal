archivo = open("diario.txt", "a")
# se abre el archivo del diario en modo "append"

archivo.write(input("¿Qué día es hoy?: ") + ":\t")		 # Solicita al usuario la fecha de hoy y la agrega
archivo.write(input("¿Cómo te sientes hoy?: "))	 # Solicita el contenido de la entrada al usuario y la agrega
archivo.write("\n" + "-"*50 + "\n")				 		 # Separador para la entrada del día siguiente
archivo.close()