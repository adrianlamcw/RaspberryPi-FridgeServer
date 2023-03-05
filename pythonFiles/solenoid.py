import RPi.GPIO as GPIO
import timers
import constants

def set_solenoid_on(pin):
	GPIO.output(pin, GPIO.HIGH)
	print('set high')
	timers.set_timer(1)


def set_solenoid_off(pin):
	GPIO.output(pin, GPIO.LOW)
	print('set low')
	timers.set_timer(1)

