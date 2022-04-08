print('[Mensaje] Generando libreria compartida linenoise')

import platform
sistema = platform.system()

Import('entorno','ruta_librerias')


if sistema == "Linux":
    entorno.Append(CCFLAGS = '-fPIC')

entorno.SharedLibrary(target=ruta_librerias+"linenoise",source="linenoise.c")