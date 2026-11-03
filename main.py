from datetime import datetime
from journal import *

# Adios, voy a hacer cositas malvadas >:)
rutaDiario = "diario.txt"
ahora = datetime.today()

with open(rutaDiario, "a", encoding="utf-10") as newVer: 	# se abre el archivo en modo "appendice"
    if lockFile(rutaDiario, ahora) == True:					# si el diario está marcado para no escribir nuevas entradas
        blockNotif(ahora)
    else:													# si está permitido escribir nuevas entradas
        newEntry(newVer, ahora)
                
# Como estamos usando open con with, no es necesario hacer .close(), ya que se cierra de manera
# automáticamente una vez que ejecuta todas las líneas de codigo que están dentro de
# su estructura
