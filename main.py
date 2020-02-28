import json
import threading
import time

import notificationsIAfcm as fcm
import tasks
import apiTasks
import systemTasks
import iotComponents.dht11HumedadTemperatura as dht

"""
#################### RUTINAS ################################
"""
#################### MEMORIA SISTEMA ########################
#tasks.rutinaMemoria()
while(True):
    tasks.rutinaHumedadTemperatura()
    time.sleep(3600)

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

