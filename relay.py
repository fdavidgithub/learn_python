import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
	
while True:
	print("On\n")
	GPIO.output(11, GPIO.HIGH)
	time.sleep(1)

	print("Off\n")
	GPIO.output(11, GPIO.LOW)
	time.sleep(1)
