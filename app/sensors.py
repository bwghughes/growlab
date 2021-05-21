import smbus2
import bme280

import time

class grownosensor:
    def __init__(self):
        pass

    def get_readings(self):
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
        }

class growbme280:
    def __init__(self):
        port = 1
        self.address = 0x77
        self.bus = smbus2.SMBus(port)
        self.calibration_params = bme280.load_calibration_params(self.bus, self.address)
        # the sample method will take a single reading and return a
        # compensated_reading object
        

    def get_readings(self):
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        temperature = data.temperature
        pressure = data.pressure
        humidity = data.humidity
        time_str = data.timestamp

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity
        }

class growbmp280:
    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BMP280(i2c_dev=self.bus)

    def get_readings(self):
        # Ignore first result since it seems stale
        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time.sleep(0.1)

        temperature = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time_str = time.strftime("%H:%M:%S")

        return {
            "time": time_str,
            "temperature": temperature,
            "pressure": pressure,
        }
