import platform
import os

Import('entorno')

ruta_librerias = entorno['ruta_librerias']
sistema = platform.system()


codigoFuenteC = []
codigoFuenteO = []



for archivo in os.listdir("."):
    if(archivo.endswith(".c")):
        if sistema == "Windows":
            if(archivo != "latcurseslib.c"):
                codigoFuenteC.append(archivo)
        else:
            codigoFuenteC.append(archivo)


entorno.SharedLibrary(target = ruta_librerias+"latino", source = codigoFuenteC)


for archivo in os.listdir("."):
    if(archivo.endswith(".obj") or archivo.endswith(".o")):
        codigoFuenteO.append(archivo)

entorno.StaticLibrary(target = ruta_librerias+"latino_static", source = codigoFuenteO)

#for archivo in os.listdir("."):
#    if(archivo.endswith(".c")):
#        if sistema == "Windows":
#            if archivo != "latcurseslib.c":
#                codigoFuenteC.append(archivo)
#        else:
#            codigoFuenteC.append(archivo)

#    if sistema == "Windows":
#        if(archivo.endswith(".obj")):    
#            codigoFuenteO.append(archivo)
#    elif sistema == "Linux":
#        if(archivo.endswith(".o")):    
#            codigoFuenteO.append(archivo)

#
#
