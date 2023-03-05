import RPi.GPIO as GPIO
import time

def set_solenoid_on(pin):
	GPIO.output(pin, GPIO.HIGH)
	print('set high')
	time.sleep(1)


def set_solenoid_off(pin):
	GPIO.output(pin, GPIO.LOW)
	print('set low')
	time.sleep(1)

def is_locked(pin):
	return GPIO.input(pin)
