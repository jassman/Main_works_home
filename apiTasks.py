import time
import json

### Formato esperado por el sistema
def formatMemoriaSistema(memoria):
    
    return {
        "fecha": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total": memoria["total"]["mem"],
        "swap_total": memoria["total"]["swap"],
        "usada": memoria["used"]["mem"],
        "usada_swap": memoria["used"]["swap"],
        "libre": memoria["free"]["mem"],
        "libre_swap": memoria["free"]["swap"],
        "compartida": memoria["shared"]["mem"],
        "compartida_swap": memoria["shared"]["swap"],
        "cache": memoria["buff/cache"]["mem"],
        "cache_swap": memoria["buff/cache"]["swap"],
        "disponible": memoria["available"]["mem"],
        "disponible_swap": memoria["available"]["swap"]
    }

### Formato esperado por el sistema
def formatArquitectureSistema(arqInfo):
    return {
        "arquitectura" : arqInfo["lscpu"][0]["data"],
        "byteorder" : arqInfo["lscpu"][1]["data"],
        "ncpu" : arqInfo["lscpu"][2]["data"],
        "nhilo" : arqInfo["lscpu"][4]["data"],
        "ncore" : arqInfo["lscpu"][5]["data"],
        "nsocket" : arqInfo["lscpu"][6]["data"],
        "fabricante" : arqInfo["lscpu"][7]["data"],
        "vmodel" : arqInfo["lscpu"][8]["data"],
        "model" : arqInfo["lscpu"][9]["data"],
        "maxcpu" : arqInfo["lscpu"][11]["data"],
        "mincpu" : arqInfo["lscpu"][12]["data"],
        "bogomips" : arqInfo["lscpu"][13]["data"]
    }
        


