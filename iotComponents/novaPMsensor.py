import serial
import struct
import aqi
import time
from datetime import datetime

# Change this to the right port - /dev/tty* on Linux and Mac and COM* on Windows
PORT = '/dev/ttyUSB0'

UNPACK_PAT = '<ccHHHcc'

def getParticulasAire():
    with serial.Serial(PORT, 9600, bytesize=8, parity='N', stopbits=1) as ser:
        data = ser.read(10)
        unpacked = struct.unpack(UNPACK_PAT, data)
        ts = datetime.now()
        pm25 = unpacked[2] / 10.0
        pm10 = unpacked[3] / 10.0
        myaqi = aqi.to_aqi([
                                (aqi.POLLUTANT_PM25, pm25),
                                (aqi.POLLUTANT_PM10, pm10)
                            ])
        print("{}: AQI = {}, PM 2.5 = {}, PM 10 = {}".format(ts, myaqi, pm25, pm10))

        json_response = {}
        if pm25 is not None and pm10 is not None and myaqi is not None:
            json_response = {"fecha": datetime.time(), "aqi": myaqi, "PM25": pm25, "PM10": pm10}
            return json_response
        else:
            print('Failed to get reading getParticulasAire. Try again!')
            return False