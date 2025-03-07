##########################匯入模組########################
from machine import Pin, PWM
from time import sleep

########################宣告與設定########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################主程式###########################
while True:

    led.duty(0)
    sleep(1)
    led.duty(1023)
    sleep(1)
    led.duty(820)
    sleep(1)
    led.duty(512)
    sleep(1)
    led.duty(256)
    sleep(1)
    led.duty(100)
    sleep(1)
    led.duty(0)
    sleep(1)
    led.duty(100)
    sleep(1)
    led.duty(256)
    sleep(1)
    led.duty(512)
    sleep(1)
    led.duty(820)
    sleep(1)
    led.duty(1023)
    sleep(1)
