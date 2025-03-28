##########################匯入模組########################
from machine import Pin, PWM
from time import sleep

########################宣告與設定########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)
delay = 0.002

#########################主程式###########################
while True:
    for delay_cycle in range(1023, -1, -1):

        led.duty(delay_cycle)
        sleep(delay)

    for delay_cycle in range(1024):

        led.duty(delay_cycle)
        sleep(delay)
