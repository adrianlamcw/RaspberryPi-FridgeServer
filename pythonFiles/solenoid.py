import RPi.GPIO as GPIO
import time

def solenoid_lock(pin):
	GPIO.output(pin, GPIO.HIGH)
	print('set high')
	time.sleep(1)


def solenoid_unlock(pin):
	GPIO.output(pin, GPIO.LOW)
	print('set low')
	time.sleep(1)

def is_locked(pin):
	return GPIO.input(pin)
