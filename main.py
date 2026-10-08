from datetime import datetime

ahora = datetime.today()							  # guarda la fecha de hoy
dia, mes = ahora.strftime("%d"), ahora.strftime("%m") # se extrae el día y el mes desde la fecha de hoy
lock = False										  # Variable para permitir la escritura de nuevas entradas
                                                      # para que solo exista una por día

diasES = { "Mon":"Lunes","Tue":"Martes","Wed":"Miércoles","Thu":"Jueves","Fri":"Viernes","Sat":"Sábado", "Sun":"Domingo"}
# diccionario para transformar los días de la semana a su equivalente en español

with open("diario.txt", "r", encoding="utf-8") as lastVer:	# se abre el archivo en modo "read"
    lastEntry = lastVer.readlines()[-2]					  	# leer la última entrada en el archivo
    if lastEntry[1:3] == mes and lastEntry[4:6] == dia:	  	# si la fecha de la última entrada coincide con la fecha actual
        lock = True										  	# se marca la variable para no permitir que se escriba el diario

with open("diario.txt", "a", encoding="utf-8") as newVer: 	# se abre el archivo en modo "append"
    if lock == True:									  	# si el diario está marcado para no escribir nuevas entradas
        hRest = 23 -int(ahora.strftime("%H"))			  	# calcula cuánto tiempo falta para un nuevo día
        mRest = 60 -int(ahora.strftime("%M"))			  	# y lo informa en un mensaje por pantalla
        print(f"¡Ya escribiste una entrada para el día de hoy!\nPuedes escribir una nueva en {hRest} horas y {mRest} minutos.")
    else:
        diaSemana = diasES[ahora.strftime("%a")]			  	# si está permitido escribir nuevas entradas
        newVer.write(f"[{dia}/{mes}({diaSemana})]: ")	# escribe la fecha a partir de los datos obtenidos previamente
        newVer.write(input("¿Cómo te sientes hoy?: "))		# pide al usuario el contenido de la entrada y lo añade
        print("Tu entrada se guardó correctamente.")		# muestra un mensaje confirmando el éxito de la tarea
        newVer.write("\n" + "-"*50 + "\n")					# deja un separador para que se distinga una entrada de otra
        
# Como estamos usando open con with, no es necesario hacer .close(), ya que se cierra
# automáticamente una vez que ejecuta todas las líneas de codigo que están dentro de
# su estructura
        
        



