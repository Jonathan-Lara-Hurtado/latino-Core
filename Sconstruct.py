'''
/***********************************************************************************
 * Copyright (c) 2015-2021 Lenguaje-Latino, programación con sintaxis al Español.  *
 *                                                                                 *
 *                            Scons de Latino                                      *
 ***********************************************************************************/

'''
Export('')
'''
import platform
import os

sistema = platform.system()
ruta_Absoluta = GetLaunchDir()
ruta_linenoise = os.path.join(ruta_Absoluta,"src/linenoise/")
ruta_include_latino = os.path.join(ruta_Absoluta,"include/")
ruta_regex = os.path.join(ruta_Absoluta,"src/latino-regex/src/")
ruta_librerias = os.path.join(ruta_Absoluta,"librerias/")
ruta_latino_regex = os.path.join(ruta_Absoluta,"src/latino-regex/src")


CambioArquitectura = True

if CambioArquitectura:
    arquitectura = 'x86_64'
else:
    arquitectura = 'x86'


entorno = Environment(TARGET_ARCH=arquitectura)

entorno['ruta_librerias'] = ruta_librerias

entorno.Append(CPPPATH=[ruta_linenoise,
                        ruta_include_latino,
                        ruta_regex])

entorno.Append(LIBPATH=[ruta_librerias])

Export('entorno')
SConscript(['src/linenoise/Sconscript'])
if sistema == "Windows":
    SConscript(['src/latino-regex/src/Sconscript'])
    entorno.Append(LIBS = ['linenoise','regex'])
SConscript(['src/Sconscript'])








if sistema == "Linux":
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
        if sistema == "Windows":
            if(archivo != "latcurseslib.c"):
                codigoFuente.append("src/"+archivo)
        else:
            codigoFuente.append("src/"+archivo)

#se compila latino
entorno.Program(target='build/latino', source = codigoFuente)
'''