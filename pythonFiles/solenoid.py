import RPi.GPIO as GPIO
import time

def solenoid_unlock(pin, LED_pin):
	GPIO.output(pin, GPIO.HIGH)
	print('set high, unlock')
	# Turn on LED
	GPIO.output(LED_pin, GPIO.HIGH)
	time.sleep(1)


def solenoid_lock(pin, LED_pin, switch_pin):
	if GPIO.input(switch_pin) == 1:
		GPIO.output(pin, GPIO.LOW)
		print('set low, lock')
		# Turn off LED
		GPIO.output(LED_pin, GPIO.LOW)
		time.sleep(1)
		return True
	else:
		for i in range(10):
			# Flash LED
			print('flash')
			GPIO.output(LED_pin, GPIO.LOW)
			time.sleep(0.25)
			GPIO.output(LED_pin, GPIO.HIGH)
			time.sleep(0.25)
		return False
			

def is_locked(pin):
	return GPIO.input(pin)
