'''
/***********************************************************************************
 * Copyright (c) 2015-2021 Lenguaje-Latino, programación con sintaxis al Español.  *
 *                                                                                 *
 *                            Scons de Latino                                      *
 ***********************************************************************************/

'''

import platform
import os

sistema = platform.system()
ruta_Absoluta = GetLaunchDir()
ruta_linenoise = os.path.join(ruta_Absoluta,"src/linenoise/")
ruta_include_latino = os.path.join(ruta_Absoluta,"include/")
ruta_librerias = os.path.join(ruta_Absoluta,"librerias/")
ruta_latino_regex = os.path.join(ruta_Absoluta,"src/latino-regex/src")


#Se crea el entorno scons
entorno = Environment()

entorno['ruta_librerias'] = ruta_librerias

entorno.Append(CPPPATH=[ruta_linenoise,
                        ruta_include_latino])

Export('entorno')
SConscript(['src/Sconscript'])
SConscript(['src/linenoise/Sconscript'])


entorno.Append(LIBPATH=[ruta_librerias])

if sistema == "Windows":
    entorno.Append(LIBS = ['linenoise','regex'])
else:
    entorno.Append(LIBS = ['linenoise',
                            'latino',
                            'latino_static',
                            '-ldl',
                            '-lm',
                            '-lreadline',
                            '-lcurses',
                            ])



codigoFuente = []
for archivo in os.listdir("src/"):
    if(archivo.endswith(".c")):
        codigoFuente.append("src/"+archivo)


#se compila latino
entorno.Program(target='build/latino', source = codigoFuente)