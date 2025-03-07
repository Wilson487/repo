##########################匯入模組########################
from machine import Pin, PWM
from time import sleep

########################宣告與設定########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################主程式###########################
a = 1023
while True:
    for i in range(a=0):

        led.duty(a)
        sleep(0.001)
        a - 1
