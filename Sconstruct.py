'''
/***********************************************************************************
 * Copyright (c) 2015-2021 Lenguaje-Latino, programación con sintaxis al Español.  *
 *                                                                                 *
 *                            Scons de Latino                                      *
 ***********************************************************************************/

'''

import platform
import os

#Se crea el entorno scons
entorno = Environment()

#script Scons
SConscript(['src/linenoise/Sconscript'])
SConscript(['src/Sconscript'])


#Dependencias implícitas
#entorno.Append(CPPPATH=['src/linenoise/','include/'])


#entorno.Append(LIBS=['liblinenoise','latino','latino_static','-ldl','-lm','-lreadline','-lcurses'])


#codigoFuente = []
#for archivo in os.listdir("src/"):
#    if(archivo.endswith(".c")):
#        codigoFuente.append("src/"+archivo)


#se compila latino
#entorno.Program(target='build/latino', source = codigoFuente)