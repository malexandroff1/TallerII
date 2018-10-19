#!/usr/bin/env python

from pyA20.gpio import gpio
from pyA20.gpio import port
import time

gpio.init() #Initialize module. Always called first
led = port.PA20
gpio.setcfg(led, gpio.OUTPUT)  #Configure LED1 as output

while True:
    gpio.output(led,1)
    time.sleep(1)
    gpio.output(led, 0)
    time.sleep(1)