from machine import Pin
from time import sleep

p2=Pin(2,Pin.OUT)

while True:
    p2.value(0)  #設為低電位（通常 LED 會熄滅）
    sleep(1)  #等待 1 秒
    p2.value(1)  #設為高電位（通常 LED 會閃爍）
    sleep(1)  #等待 1 秒