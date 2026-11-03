from datetime import datetime

usuario = input("¿Como te llamas?: ")
entrada = input("¿Que quieres agregar al diario el dia de hoy?: ")

ahora = datetime.today()
fecha = ahora.strftime(" Día %d, a las %H:%M:%S")

archivo = open("diario.txt", "a", encoding="utf-8")
archivo.write("Usuario: " + usuario + "\n")
archivo.write("Actualizado: "+ fecha + "\n")
archivo.write(entrada + "\n\n")
archivo.close()

print("Entrada guardada, " + usuario) 