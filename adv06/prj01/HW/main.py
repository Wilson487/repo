# 當光感數值超過700的時候燈開啟，低於700的時候燈關閉

##########################匯入模組########################
from machine import Pin, PWM
from machine import Pin, ADC
from time import sleep
import mcu

########################宣告與設定########################
gpio = mcu.gpio()
light_sensor = ADC(0)  # 建立ADC物件
RED = PWM(Pin(gpio.D5), freq=frequency, duty=duty_cycle)
########################主程式########################
while True:
    light_sensor_reading = light_sensor.read()
    if light_sensor_reading > 700:
        print("燈開啟")
        RED.value(1)
    else:
        print("燈關閉")
        RED.value(0)
    sleep(1)  # 等1秒
