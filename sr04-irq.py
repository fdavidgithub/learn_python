import machine
from machine import Pin, Timer
import utime as tm

'''
def distance():
    trig.low()
    tm.sleep_us(5)
    trig.high()
    tm.sleep_us(5)
    trig.low()

    while echo.value() == 0:
        signaloff = tm.ticks_us()

    while echo.value() == 1:
        signalon = tm.ticks_us()
'''

class Sr04:
    def __init__(self, pinTrig=0, pinEcho=1):
        # Variables
        self.FATORCM = 58
        self.FATORINCH = 148
        self.CYCLE = 60
        self.signalOn = 0
        self.signalOff = 0

        # Pin mode
        self.trig = Pin(pinTrig, Pin.OUT)
        self.echo = Pin(pinEcho, Pin.IN)

        # Interrupt
        self.echo.irq(handler = self.echoHigh, trigger=Pin.IRQ_RISING)
        self.echo.irq(handler = self.echoLow, trigger=Pin.IRQ_FALLING)
        self.trig.irq(handler = self.trigHigh, trigger=Pin.IRQ_RISING)
        self.trig.irq(handler = self.trigLow, trigger=Pin.IRQ_FALLING)

    def trigLow(self, pin):
        print("trig: low %s" % self.echo.value())
        self.signalOn = tm.ticks_us()

    def trigHigh(self, pin):
        print("trig: high")

    def echoLow(self, pin):
        print("echo: low %s" % self.echo.value())
        self.signalOff = tm.ticks_us()

    def echoHigh(self, pin):
        print("echo: high")

    def distance(self):
        self.trig.high()
        tm.sleep_us(10)
        self.trig.low()

        delta = tm.ticks_diff(self.signalOff, self.signalOn)
        distance = delta / self.FATORCM

        print("Fator %s | On %s | Off %s | %s" % (self.FATORCM, self.signalOn, self.signalOff, delta) ) 
        return distance

