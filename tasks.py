import json

from restApiProvider import RestApiProviderClass
import systemTasks
import apiTasks
import iotComponents.dht11HumedadTemperatura as dht

import iotComponents.wifiMonitor

apiRest = RestApiProviderClass()
monitor = iotComponents.wifiMonitor.WifiMonitor()

### REGISTRO MEMORIA SISTEMA #################################################################
def rutinaMemoria():
    ## Obtiene los registros de memoria
    memoria = systemTasks.getMemoryInfo()
    #print (memoria)
    ## Formato de memoria
    api_memoria = apiTasks.formatMemoriaSistema(json.loads(memoria))
    ## Regitro de memoria
    respuesta = apiRest.postMemoriaSistema(api_memoria)
    print (respuesta)
##############################################################################################

### REGISTRO ARQUITECTURA SISTEMA ############################################################
def rutinaUnicaArquitectureInfo():
    arqInfo = systemTasks.getArquitectureInfo()
    arqInfo = apiTasks.formatArquitectureSistema(arqInfo)
    respuesta = apiRest.postArquitectura(arqInfo)
    print(respuesta)
##############################################################################################

### REGISTRO TEMPERATURA Y HUMEDAD ###########################################################
def rutinaHumedadTemperatura():
    infoHumedad = dht.readDHTHumedad()
    if (infoHumedad != False):
        respuesta = apiRest.postIotHumedadTemperatura(infoHumedad)
        print(respuesta)
##############################################################################################

### COMPROBAR PERSONAS EN CASA WIFI ##########################################################
def rutinaComprobarDispositivosWifi():
    mensaje = ""
    han_vuelto, primera_vez = monitor.get_in_home_now()
    se_han_ido = monitor.get_out_home_now()
    if(len(primera_vez) > 0): # Si se han detectado nuevos dispositivos
        mensaje += "Primera deteccion: "
        for d in primera_vez :
            mensaje = mensaje + d["nombre"] + ": " +  d["last_format_date"] + " "
        mensaje += "\n"
    if(len(han_vuelto) > 0): # Si se ha vuelto a detectar un dispositivo
        mensaje += "Se ha detectado: "
        for d in han_vuelto :
            mensaje = mensaje + d["nombre"] + ": " +  d["last_format_date"] + " "
        mensaje += "\n"
    if(len(se_han_ido) > 0): # Si se ha dejado de detectar algun dispositivo
        mensaje += "Se ha dejado de detectar: "
        for d in se_han_ido :
            mensaje = mensaje + d["nombre"] + ": " +  d["last_format_date"] + " "
        mensaje += "\n"

    return mensaje
##############################################################################################

### REGISTRO DETECCIONES POR RANGOS WIFI #####################################################
def rutinaGuardarDatosWifi(fecha):
    detecciones = monitor.loadData(fecha)
    conocidos = []
    for d in detecciones:
        if(d["conocido"] == 0 or d["conocido"] == 1):
            conocidos.append(d)
    #print(conocidos)
    respuesta = apiRest.postIotWifiRangos(conocidos)
    print(respuesta.text)
##############################################################################################







### OBTIENE LA TEMPERATURA DE LA CPU DE SERVIDOR #############################################
def getLastCPUTemperature():
    statsCPU = apiRest.getLastTemperatureCPU()
    return json.dumps(statsCPU)
##############################################################################################