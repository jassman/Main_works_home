import json
import threading
import time
from datetime import datetime, timedelta
import locale

import notificationsIAfcm as fcm
import tasks
import apiTasks
import systemTasks
import iotComponents.dht11HumedadTemperatura as dht
import iotComponents.wifiMonitor

locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")

# RUTINAS
TEMPERATURA_HUMEDAD = True # Registro de la temperatura y humedad del sensor
CHECK_WIFI = False # Debe esta el servicio de detecciones encendido!!!! 
REGISTRO_RANGOS_WIFI = True # Registro de rangos wifi en el servidor

# TIEMPOS RUTINAS (segundos)
TEMPERATURA_HUMEDAD_TIME = 3600
CHECK_WIFI_TIME = 60

### TOKEN Y NOTIFICACIONES
token_fcm = fcm.getTokenFCM()

"""
############################### RUTINAS ############################################
"""
####################### MEMORIA SISTEMA ###########################
#tasks.rutinaMemoria()

#################### TEMPERATURA Y HUMEDAD ########################
# Comprueba la humedad y la temperatura actual y la guarda
def wrapperHumedadTemperatura():
    while True :
        tasks.rutinaHumedadTemperatura()
        time.sleep(3600)

####################### DETECCIONES WIFI ##########################
# Eventos de detecciones wifi
# Comprueba las detecciones en tiempo real y realiza un seguimiento de las macs conocidas
def wrapperAreUInHome():
    while True :
        mensaje = tasks.rutinaComprobarDispositivosWifi()
        if(mensaje != ""):
            print("RUTINAS " + token_fcm)
            fcm.push_notification('IA HOME', mensaje, token_fcm)
        time.sleep(60)

############### REGISTRO DIARIO DE DETECCIONES WIFI ################
# Comprueba la humedad y la temperatura actual y la guarda
def wrapperGuardaDatosWifi():
    while True :
        ahora = datetime.now().replace(microsecond=0) # Ahora
        tomorrow = datetime.today() + timedelta(days=1) # Mañana
        tomorrow_begin = datetime(year=tomorrow.year, month=tomorrow.month, day=tomorrow.day, hour=0, minute=5, second=0) # Mañana con hora
        t_hasta = (tomorrow_begin - ahora).seconds # Tiempo hasta el proximo registro
        time.sleep(t_hasta)
        tasks.rutinaGuardarDatosWifi(ahora.strftime('%Y-%m-%d'))

"""
################################# HILOS ############################################
"""
# TEMPERATURA Y HUMEDAD 
if (TEMPERATURA_HUMEDAD) :
    hilo_humedad_temperatura = threading.Thread(target=wrapperHumedadTemperatura)
    hilo_humedad_temperatura.start()

# EVENTOS DETECCIONES WIFI (NOTIFICACIONES)
if (CHECK_WIFI) :
    hilo_wifi_check = threading.Thread(target=wrapperAreUInHome)
    hilo_wifi_check.start()
   
# REGISTRO DETECCIONES WIFI
if (REGISTRO_RANGOS_WIFI) :
    hilo_wifi_rangos = threading.Thread(target=wrapperGuardaDatosWifi)
    hilo_wifi_rangos.start()



"""
############## RUTINAS UNICAS ################################
(Rutinas que solo son necesarias ejecutarlar una vez)
"""
#tasks.rutinaUnicaArquitectureInfo()
"""
############### PRUEBAS DE COSAS #############################
"""

### TOKEN Y NOTIFICACIONES
#token_fcm = fcm.getTokenFCM()
#statsCPU = tasks.getLastCPUTemperature()
#print (statsCPU)

##json_cpu = json.loads(statsCPU)
##ultima_temp_registrada = json_cpu["results"][-1]["temperatura"]

#fcm.push_notification('Hola Javier', ultima_temp_registrada, token_fcm)

#hilo1 = threading.Thread(target=dht.printTempAndHumidity())
#hilo1.start()

