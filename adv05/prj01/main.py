##############################匯入模組##############################
from machine import Pin
from time import sleep

##############################宣告與設定##############################
RED = Pin(14, Pin.OUT)
BLUE = Pin(13, Pin.OUT)
GREEN = Pin(12, Pin.OUT)

RED.value(1)
BLUE.value(1)
GREEN.value(1)
