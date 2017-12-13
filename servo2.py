import RPi.GPIO as GPIO
import time
import keyboard
from pynput import keyboard

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

#Declaration des variables
p = GPIO.PWM(17,100)
dutyCycle = 0
i = 0

p.start(dutyCycle)

def on_press(key):
    if key == keyboard.Key.z and dutyCycle <= 23:
        dutyCycle = dutyCycle + 0.1
    if key == keyboard.Key.s and dutyCycle >= 5 :
		dutyCycle = dutyCycle - 0.1


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

	
while i==0 :
	p.ChangeDutyCycle(dutyCycle)
	
p.stop()
GPIO.cleanup()

		

def angleToDutyCycle(a) :
	return float(a)/10 + 5
