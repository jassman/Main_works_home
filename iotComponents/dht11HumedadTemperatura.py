import time

import Adafruit_DHT


def printTempAndHumidity():
    #while (True):
    # Set sensor type : Options are DHT11,DHT22 or AM2302
    sensor=Adafruit_DHT.DHT11
    # Set GPIO sensor is connected to
    gpio=3
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    
        #time.sleep(3600)
        
def readDHTHumedad():
    # Set sensor type : Options are DHT11,DHT22 or AM2302
    sensor=Adafruit_DHT.DHT11
    # Set GPIO sensor is connected to
    gpio=3
    json_response = {}
    # Use read_retry method. This will retry up to 15 times to
    # get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    # Reading the DHT11 is very sensitive to timings and occasionally
    # the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
        json_response = {"temperatura": temperature, "humedad": humidity, "habitacion": 1}
        return json_response
    else:
        print('Failed to get reading. Try again!')
        return False

"""
respuesta = readDHTHumedad()
if(respuesta != False):
    print(respuesta)
    print(respuesta["temperatura"])
"""
    