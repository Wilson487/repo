##########################匯入模組########################
from machine import Pin, PWM
from time import sleep

########################宣告與設定########################
frequency = 1000
duty_cycle = 0
led = PWM(Pin(2), freq=frequency, duty=duty_cycle)

#########################主程式###########################
while True:
    led.duty(0)  # LED 關閉
    sleep(2)  # 等 2 秒
    led.duty(512)  # LED 50% 亮度
    sleep(2)  # 等 2 秒
    led.duty(1023)  # LED 最亮
    sleep(2)  # 等 2 秒
