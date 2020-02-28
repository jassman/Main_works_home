import json

from restApiProvider import RestApiProviderClass
import systemTasks
import apiTasks
import iotComponents.dht11HumedadTemperatura as dht

apiRest = RestApiProviderClass()

#################### MEMORIA SISTEMA #############################
def rutinaMemoria():
    ## Obtiene los registros de memoria
    memoria = systemTasks.getMemoryInfo()
    #print (memoria)
    ## Formato de memoria
    api_memoria = apiTasks.formatMemoriaSistema(json.loads(memoria))
    ## Regitro de memoria
    respuesta = apiRest.postMemoriaSistema(api_memoria)
    print (respuesta)
##################################################################

########### Inserta los datos de la arquitectura del sistema #####
def rutinaUnicaArquitectureInfo():
    arqInfo = systemTasks.getArquitectureInfo()
    arqInfo = apiTasks.formatArquitectureSistema(arqInfo)
    respuesta = apiRest.postArquitectura(arqInfo)
    print(respuesta)
##################################################################

###### Inserta los datos de la humedad y temperatura externa #####
def rutinaHumedadTemperatura():
    infoHumedad = dht.readDHTHumedad()
    if (infoHumedad != False):
        respuesta = apiRest.postIotHumedadTemperatura(infoHumedad)
        print(respuesta)
##################################################################

### Obtiene la temperatura del procesador
def getLastCPUTemperature():
    statsCPU = apiRest.getLastTemperatureCPU()
    return json.dumps(statsCPU)
