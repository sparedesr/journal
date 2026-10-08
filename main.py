from datetime import datetime

archivo = open("diario.txt", "a")
# se abre el archivo del diario en modo "append"

ahora = datetime.today()	# guarda la fecha de hoy
dia = ahora.strftime("%d")	# se extrae el día y el 
mes = ahora.strftime("%m")	# mes desde la fecha de hoy

archivo.write(f"[{dia}/{mes}]: ")						# Escribir la fecha de la entrada
archivo.write(input("¿Cómo te sientes hoy?: "))			# Solicita el contenido de la entrada al usuario
archivo.write("\n" + "-"*50 + "\n")						# Separador para la entrada del día siguiente
archivo.close()											# Cerrar el archivo