import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

#Declaration des variables
p = GPIO.PWM(17,100)
dutyCycle = 0
i = 0

p.start(dutyCycle)


def keydown(e):
	if keyboard.is_pressed('up') and dutyCycle <= 23:
		dutyCycle = dutyCycle + 0.1

	if keyboard.is_pressed('down') and dutyCycle >= 5 :
		dutyCycle = dutyCycle - 0.1
	
	if keyboard.is_pressed('space') :
		i = 1

keyboard.hook(keydown)

	
	
while i==0 :
	p.ChangeDutyCycle(dutyCycle)
	
	
p.stop()
GPIO.cleanup()

		

def angleToDutyCycle(a) :
	return float(a)/10 + 5
