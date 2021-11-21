from __future__ import division

import os
import sys

from gpiozero import LED
from time import sleep
from pygame import mixer

pins = ["GPIO04", "GPIO17", "GPIO27", "GPIO22", "GPIO10", 
"GPIO09", "GPIO11", "GPIO08"]
pinValues = [False for i in range(8)]
led = [None] * 8

counterC = 120.0
diffC = .5


def zero():
    counter = counterC
    while counter > 0:
        diff = diffC
        for x in range(0,4):
            led[x].on()
            led[x+4].on()
            sleep(diff)
            counter-=diff
        for x in range(0,4):
            led[x].off()
            led[x+4].off()
            sleep(diff)
            counter-=diff
def one():
    counter = counterC
    while counter > 0:
        diff = diffC
        for x in range(0,4):
            if x != 0:
                led[x-1].off()
                led[x+3].off()
            led[x].on()
            led[x+4].on()
            sleep(diff)
            counter -= diff
        
        led[3].off()
        led[7].off()
    
def two():
    counter = counterC
    while counter > 0:
        diff = diffC
        for x in range(0,4):
            led[x].toggle()
            sleep(diff)
            counter -= diff
        for x in range (7, 3, -1):
            led[x].toggle()
            sleep(diff)
            counter -= diff

def three():
    
    counter = counterC
    while counter > 0:
        diff = diffC
        for x in range(0,4):
            led[x].toggle()
        sleep(diff)
        counter -= diff
        for x in range (4, 8):
            led[x].toggle()
        sleep(diff)
        counter -= diff
def main():
    options = {
        0 :zero,
        1:one,
        2:two,
        3:three,
    }
    for x in range(0,8):
        led[x] = LED(pins[x])
        led[x].on()
        sleep(.05)
    sleep(.5)

    for x in range(0,8):
        led[x].off()
        sleep(.05)
   
    print("Finished init")
    val = True
    count = 0
    while val:
        for x in range (0,8):
            led[x].on()
        #sleep(120)
        sleep(counterC)
        print("Finished waiting")
        print(count)
        options[count%len(options)]()
        count+=1
        print("finished show")


if __name__ == "__main__":
    main()
