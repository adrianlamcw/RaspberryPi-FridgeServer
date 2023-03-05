import RPi.GPIO as GPIO
import timers
import constants

def set_solenoid_on(pin):
	GPIO.output(pin, GPIO.HIGH)
	
	timers.set_timer(2)
	print('set high')
	GPIO.output(pin, GPIO.LOW)
	timers.set_timer(2)
	print('set low')


