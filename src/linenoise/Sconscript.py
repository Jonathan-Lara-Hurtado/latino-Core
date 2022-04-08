print('[Mensaje] Generando libreria estatica linenoise')

import platform
sistema = platform.system()

Import('entorno','ruta_librerias')


if sistema == "Linux":
    entorno.Append(CCFLAGS = '-fPIC')

entorno.StaticLibrary(target=ruta_librerias+"linenoise",source="linenoise.c")