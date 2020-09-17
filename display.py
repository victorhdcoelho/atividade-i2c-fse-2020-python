import smbus2
import bme280
import RPi_I2C_driver
import time

porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)
mylcd = RPi_I2C_driver.lcd()
calibracao_paramentros = bme280.load_calibration_params(bus, endereco)

while True:
    time.sleep(1)
    dado = bme280.sample(bus, endereco, calibracao_paramentros)
    string_t = "Victor: T. {:.2f}".format(dado.temperature)
    string_p = "U. {:.2f}P. {:.2f}".format(dado.humidity, dado.pressure)

    mylcd.lcd_display_string(string_t, 1)
    mylcd.lcd_display_string(string_p, 2)
