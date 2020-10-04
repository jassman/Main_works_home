from sds011 import SDS011

port = "/dev/ttyUSB0"

sds = SDS011(port=port)
sds.set_working_period(rate=1)#one measurment every 5 minutes offers decent granularity and at least a few years of lifetime to the sensor
print(sds)
import csv
try:
    logcols = ["timestamp","pm2.5","pm10","devid"]
    while True:
        meas = sds.read_measurement()
        vals = [str(meas.get(k)) for k in logcols]
        print(vals)
        print(sds)
            
            
except KeyboardInterrupt:
    #sds.sleep()
    sds.__del__()