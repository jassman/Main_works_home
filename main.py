import json
import threading
import time

import notificationsIAfcm as fcm
import tasks
import apiTasks
import systemTasks
import iotComponents.dht11HumedadTemperatura as dht
import iotComponents.wifiMonitor







### TOKEN Y NOTIFICACIONES
token_fcm = fcm.getTokenFCM()

"""
#################### RUTINAS ################################
"""
#################### MEMORIA SISTEMA ########################
#tasks.rutinaMemoria()
def wrapperHumedadTemperatura():
    while True :
        tasks.rutinaHumedadTemperatura()
        time.sleep(3600)

def wrapperAreUInHome():
    monitor = iotComponents.wifiMonitor.WifiMonitor()
    while True :
        mensaje = ""
        han_vuelto, primera_vez = monitor.get_in_home_now()
        se_han_ido = monitor.get_out_home_now()
        if(len(primera_vez) > 0):
            mensaje += "Primera deteccion: "
            for d in primera_vez :
                mensaje = mensaje + d["nombre"] + ": " +  d["last_format_date"] + " "
            mensaje += "\n"
        if(len(han_vuelto) > 0):
            mensaje += "Se ha detectado: "
            for d in han_vuelto :
                mensaje = mensaje + d["nombre"] + ": " +  d["last_format_date"] + " "
            mensaje += "\n"
        if(len(se_han_ido) > 0):
            mensaje += "Se ha dejado de detectar: "
            for d in se_han_ido :
                mensaje = mensaje + d["nombre"] + ": " +  d["last_format_date"] + " "
            mensaje += "\n"

        if(mensaje != ""):
            fcm.push_notification('Cambios en casa', mensaje, token_fcm)
        #print(monitor.dispositivos_conocidos)
        #print(monitor.ultimo_leido)
        time.sleep(60)

hilo_humedad_temperatura = threading.Thread(target=wrapperHumedadTemperatura)
hilo_wifi_check = threading.Thread(target=wrapperAreUInHome)
hilo_wifi_check.start()
hilo_humedad_temperatura.start()

"""
############## RUTINAS UNICAS ################################
"""
#tasks.rutinaUnicaArquitectureInfo()
"""
############### PRUEBAS DE COSAS #############################
"""


### TOKEN Y NOTIFICACIONES
#token_fcm = fcm.getTokenFCM()
statsCPU = tasks.getLastCPUTemperature()
print (statsCPU)



##json_cpu = json.loads(statsCPU)
##ultima_temp_registrada = json_cpu["results"][-1]["temperatura"]

#fcm.push_notification('Hola Javier', ultima_temp_registrada, token_fcm)

#hilo1 = threading.Thread(target=dht.printTempAndHumidity())
#hilo1.start()

