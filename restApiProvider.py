import requests as req
import json

class RestApiProviderClass:

    USUARIO = "clientpi3"
    PASS = ""

    SERVER_NAME = 'https://192.168.1.44'
    SERVER_PORT = '443'

    def __init__(self):
        self.tokenApiServer = self.__getToken()

    # Devuelve la lista de usuarios de la app
    def getUsuarios(self):
        r = req.get(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/usuarios/',
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return json.loads(r.text)

    # Devuelve la temperatura
    def getTemperatureCPU(self):
        r = req.get(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/temperaturaCPU/',
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return json.loads(r.text)
    
    # Devuelve la temperatura
    def getLastTemperatureCPU(self):
        r = req.get(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/temperaturaCPU/last/',
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return json.loads(r.text)
        
    # Devuelve los datos de memoria
    def getMemoriaSistema(self):
        r = req.get(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/memoriaSistema/',
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return json.loads(r.text)
    
    # Inserta datos de la memoria en la bbdd
    def postMemoriaSistema(self, memoria):
        r = req.post(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/memoriaSistema/',
                    data= json.dumps(memoria),
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return r

    # Inserta informacion de la arquitectura del sistema en la bbdd
    def postArquitectura(self, arqInfo):
        r = req.post(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/arquitecturaInfo/',
                    data= json.dumps(arqInfo),
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return r

    # Inserta informacion de la temperatura y humedad del entorno
    def postIotHumedadTemperatura(self, data):
        r = req.post(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/iotTempHum/',
                    data= json.dumps(data),
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return r

    # Inserta informacion de la temperatura y humedad del entorno
    def postIotWifiRangos(self, data):
        r = req.post(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/detectWifi/',
                    data= json.dumps(data),
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return r
        
    # Inserta informacion de las particulas en suspension
    def postParticularAire(self, data):
        r = req.post(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api/v1/particulasAire/',
                    data= json.dumps(data),
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer}, verify=False)
        return r

    # Devuelve el token generado por el servidor
    def __getToken(self):
        payload = {'username':self.USUARIO, 'password':self.PASS}

        r = req.post(url= self.SERVER_NAME + ':' + self.SERVER_PORT +'/apiapp/api-token-auth/',
            data= json.dumps(payload),
            headers= {'Content-type':'application/json'},
            verify=False)

        json_obj = json.loads(r.text)
        return json_obj['token']

    '''
    def get(self):
        r = req.get(url=self.SERVER_NAME + ':' + self.SERVER_PORT +'/api/v1/usuarios/',
                    headers= {'Content-type':'application/json', 'Authorization': 'Token ' + self.tokenApiServer})
        return json.loads(r.text)
    '''
