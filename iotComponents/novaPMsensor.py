import serial
import struct
import aqi
from sds011 import SDS011
import calendar
import time
from datetime import datetime


# Change this to the right port - /dev/tty* on Linux and Mac and COM* on Windows
PORT = '/dev/ttyUSB0'

UNPACK_PAT = '<ccHHHcc'

def getParticulasAire(apiRest):
    # with serial.Serial(PORT, 9600, bytesize=8, parity='N', stopbits=1) as ser:
    #     data = ser.read(10)
    #     unpacked = struct.unpack(UNPACK_PAT, data)
    #     ts = datetime.now()
    #     pm25 = unpacked[2] / 10.0
    #     pm10 = unpacked[3] / 10.0
    #     myaqi = aqi.to_aqi([
    #                             (aqi.POLLUTANT_PM25, pm25),
    #                             (aqi.POLLUTANT_PM10, pm10)
    #                         ])
    #     print("{}: AQI = {}, PM 2.5 = {}, PM 10 = {}".format(ts, myaqi, pm25, pm10))

    #     json_response = {}
    #     if pm25 is not None and pm10 is not None and myaqi is not None:
    #         json_response = {"fecha": int(datetime.now().timestamp()), "aqi": int(myaqi), "pm25": pm25, "pm10": pm10}
    #         return json_response
    #     else:
    #         print('Failed to get reading getParticulasAire. Try again!')
    #         return False
    sds = SDS011(port=PORT)
    sds.set_working_period(rate=30)

    try:
        logcols = ["timestamp","pm2.5","pm10","devid"]
        while True:
            meas = sds.read_measurement()
            vals = [str(meas.get(k)) for k in logcols]
            ts = datetime.now()
            myaqi = aqi.to_aqi([
                                (aqi.POLLUTANT_PM25, vals[1]),
                                (aqi.POLLUTANT_PM10, vals[2])
                            ])
            print("{}: AQI = {}, PM 2.5 = {}, PM 10 = {}".format(ts, myaqi, vals[1], vals[2]))
            print(sds)

            json_response = {}
            if vals[1] is not None and vals[2] is not None and myaqi is not None:
                json_request = {"fecha": int(datetime.now().timestamp()), "aqi": int(myaqi), "pm25": pm25, "pm10": pm10}
                respuesta = apiRest.postParticularAire(json_request)
                print('novaPMSensor::getParticulasAire:: Llamada a apiRest.postParticularAire', respuesta)
            else:
                print('Failed to get reading getParticulasAire. Try again!')

    except:
        #sds.sleep()
        sds.__del__()