from machine import Pin
import utime

green_button = Pin(0, Pin.IN)
red_button = Pin(1, Pin.IN)
yellow_button =  Pin(2, Pin.IN)
blue_button = Pin(3, Pin.IN)

green_LED = Pin(4, Pin.OUT)
red_LED = Pin(5, Pin.OUT)
yellow_LED =  Pin(6, Pin.OUT)
blue_LED = Pin(7, Pin.OUT)

while true:
  if red_button.value() == 1:
    red_LED.value(1)
  utime.sleep(1)