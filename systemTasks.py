#! /usr/bin/env python
import os
import json
import threading

"""
from restApiProvider import RestApiProviderClass

apiRest = RestApiProviderClass()
"""
### Obtiene informacion sobre la arquitectura del sistema
def getArquitectureInfo():
    fr = os.popen("lscpu -J", "r")

    dump = fr.read()
    arqInfo = json.loads(dump)
    """
    for i in range(len(arqInfo["lscpu"])):
        print(arqInfo["lscpu"][i]["field"], arqInfo["lscpu"][i]["data"])
    """
    return arqInfo




### Obtiene la memoria del sistema (swap y ram)
def getMemoryInfo():
    mInfo = {} # Informacion de la memoria
    vLin = [] # Lineas de stdout
    fr = os.popen("free -m", "r")
    # Recorre la salida del comando
    for lin in fr:
        # Quita espacios y separamos por objetos independientes
        vPal = lin.rstrip().split()
        # Añade el objeto a la lista
        vLin.append( vPal )
    fr.close()

    # Recorre la cabecera
    for n in range(len(vLin[0])):
        mem = int(vLin[1][n+1]) # Añade el valor de la columna
        swap = 0 # Valor por defecto
        # Intenta ver si hay valor y lo añade en caso satisfactorio
        try:
            swap = int(vLin[2][n+1])
        except:
            pass
        # Añadimos el objeto a la lista
        mInfo[ vLin[0][n] ] = { "mem": mem, "swap": swap }

    # Volcamos la lista como json
    #print( json.dumps(mInfo) )
    return json.dumps(mInfo)
    

#print(yeah)




### Obtiene informacion de los discos montados
def getDiskInfoLinux():
    mInfo = []
    vLin = []
    datos = []
    lista = []
    dispositivos = []
    # Comando a ejecutar
    fr = os.popen("fdisk -l", "r")
    # Por cada linea en el output
    for lin in fr:
        # Quitamos espacios y separamos por objetos independientes
        vPal = lin.rstrip().split()
        # Añade el objeto a la lista
        vLin.append( vPal )
    fr.close()

    for n in range(len(vLin)):
        #print(vLin[n])
        for m in range(len(vLin[n])):
            datos.append(vLin[n][m])
        try:
            mInfo = datos.copy()
            lista.append(mInfo.copy())
        except:
            print("no")
            pass
        datos.clear()

    for x in range(len(lista)-9):
        #print(x, lista[x+8])
        num_discos = {
            "dispositivo": lista[x+9][0],
            "tam": lista[x+9][4],
            "tipo": lista[x+9][5]
        }
        dispositivos.append(num_discos)

    data_general = {
        lista[0][0].lower():lista[0][1][:-1],
        "tam_disco": lista[0][2] + " " + lista[0][3][:-1],
        lista[1][0].lower(): lista[1][3],
        "tam_sector_logico":lista[3][4] + " " + lista[3][5],
        "tam_sector_fisico":lista[3][7] + " " + lista[3][8],
        "etiqueta":lista[5][5],
        "id_disco":lista[6][3],
    }

    return data_general, dispositivos


def contar():
    '''Contar hasta cien'''
    contador = 0
    while contador<100:
        contador+=1
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'Contador:', contador)

