import RPi.GPIO as GPIO
import time
import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)
p = GPIO.PWM(17,100)
dutyCycle = 0
p.start(dutyCycle)

i = 0
while i==0 :
	if keyboard.is_pressed('up') and dutyCycle <= 23:
		dutyCycle = dutyCycle + 0.1

	if keyboard.is_pressed('down') and dutyCycle >= 5 :
		dutyCycle = dutyCycle - 0.1
	
	if keyboard.is_pressed('space') :
		i = 1
	
	p.ChangeDutyCycle(dutyCycle)
	
p.stop()
GPIO.cleanup()

def angleToDutyCycle(a) :
	return float(a)/10 + 5
