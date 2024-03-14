from subprocess import PIPE, Popen
from gpiozero import CPUTemperature
from pyfcm import FCMNotification

from restApiProvider import RestApiProviderClass


apiRest = RestApiProviderClass()
API_KEY = ''

"""
Envia una notificacion a la aplicacion movil (Android)
"""
def push_notification(titulo, mensaje, id_registro):
    push_service = FCMNotification(api_key=API_KEY)
    registration_id = id_registro
    message_title = str(titulo) 
    message_body = str(mensaje)
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
     
    print (result)
    
"""
Devuelve el token de firebase registrado (Android)
"""
def getTokenFCM():
    usuarios = apiRest.getUsuarios()
    print (usuarios)
    token_firebase = ''
    # Futuro añadir topics y enviar a todos los usuarios
    for user in usuarios['results']:
        if(user['name'] == 'javi'):
            token_firebase = user["token_firebase"] # 0 para usuario javi (En este momento)
    
    print("ESTE: " + token_firebase)
    return token_firebase