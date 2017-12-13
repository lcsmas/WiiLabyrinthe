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

def up():
	print("u")
	if dutyCycle <= 23:
		dutyCycle = dutyCycle + 0.1
		print("u")
		return

keyboard.hook(up)
def down():
	if dutyCycle >= 5 :
		dutyCycle = dutyCycle - 0.1
		print("d")
		return

def space():
	print("space")
	i = 1
	return

keyboard.add_hotkey("z",up)
keyboard.add_hotkey("s",down)
keyboard.add_hotkey("space",space)

	
while i==0 :
	keyboard.read_key()
	print("ntm")
	p.ChangeDutyCycle(dutyCycle)
	
	
p.stop()
GPIO.cleanup()

		

def angleToDutyCycle(a) :
	return float(a)/10 + 5
