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
    def __init__(self):
        self.SOUNDSPEED = 343.0              # meters per seconds
        self.M2CM = 100.0
        self.S2US = 1000000.0
        self.fator = (lambda: self.SOUNDSPEED * self.M2CM / self.S2US)

        self.trig = Pin(0, Pin.OUT)
        self.echo = Pin(1, Pin.IN)
        self.led = Pin(25, Pin.OUT)

        self.signalOn = 0
        self.signalOff = 0

    def echoHigh(self, pin):
        self.signalOn = tm.ticks_us()
        self.led.low()
        self.trig.low()

    def trigHigh(self, pin):
        self.led.high()
 
        while self.trig.value() == 1:
            self.signalOff = tm.ticks_us()
            
    def distance(self):
        self.trig.high()

        while self.trig.value() == 1:
            delta = tm.ticks_diff(self.signalOn, self.signalOff)
    
        distance = delta#(delta * self.fator() ) / 2

        return distance

    def init(self):
        self.led.low()
        self.trig.low()
        tm.sleep_us(5)

        self.trig.irq(handler = self.trigHigh, trigger=Pin.IRQ_RISING)
        self.echo.irq(handler = self.echoHigh, trigger=Pin.IRQ_RISING)

