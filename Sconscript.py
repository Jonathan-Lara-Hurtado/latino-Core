'''
/***********************************************************************************
 * Copyright (c) 2015-2021 Lenguaje-Latino, programación con sintaxis al Español.  *
 *                                                                                 *
 *                            Scons de Latino                                      *
 ***********************************************************************************/

'''

Import('entorno','debug','arquitectura')
import platform
import os

sistema = platform.system()
ruta_Absoluta = GetLaunchDir()
ruta_linenoise = os.path.join(ruta_Absoluta,"latino-Core/src/linenoise/")
ruta_include_latino = os.path.join(ruta_Absoluta,"latino-Core/include/")
ruta_regex = os.path.join(ruta_Absoluta,"latino-Core/latino-regex/src/")
ruta_librerias = os.path.join(ruta_Absoluta,"latino-Core/librerias/")


entorno['TARGET_ARCH'] = arquitectura
entorno.Append(LIBPATH=[ruta_librerias])

entorno.Append(CPPPATH=[ruta_linenoise,
                        ruta_include_latino,
                        ruta_regex])


Export('entorno','ruta_librerias')
SConscript('src/linenoise/Sconscript.py')

SConscript('latino-regex/Sconscript.py')

'''
entorno.Append(LIBS = ['linenoise'])

if sistema == "Windows":
    SConscript('latino-regex/Sconscript.py')
    entorno['LIBS'].append('regex')



SConscript(['src/Sconscript.py'])


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

entorno.Program(target='build/latino', source = codigoFuente)

'''

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