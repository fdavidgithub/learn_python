# Slave
# Blink n times when receive command
import sys, uselect 
import machine
from machine import Pin
import utime

LEN_BYTE=1

sp=uselect.poll() 
sp.register(sys.stdin,uselect.POLLIN) 

led = Pin(25, Pin.OUT)

def blink(n):
    for i in range(0,n):
        led.toggle()
        utime.sleep(1)

def read():
    while True:
        if sp.poll(0):
            byte = sys.stdin.read(LEN_BYTE)
            blink(int(byte))


