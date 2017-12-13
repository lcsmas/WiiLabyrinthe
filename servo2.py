import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

#Declaration des variables
p = GPIO.PWM(17,100)
dutyCycle = 0
i = 0

p.start(dutyCycle)	
	
while i==0 :
	x = input()
	if x == "z" and dutyCycle <= 23 :
		dutyCycle = dutyCycle + 0.1
	if x == "s" and dutyCycle >= 5 :
		dutyCycle = dutyCycle - 0.1
	if x == "p" :
		i = 1
	p.ChangeDutyCycle(dutyCycle)
	
p.stop()
GPIO.cleanup()

		

def angleToDutyCycle(a) :
	return float(a)/10 + 5
