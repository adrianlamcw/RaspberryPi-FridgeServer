import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(23, GPIO.OUT)

try:
	print('test')
	while True:
		# If limit switch is on
		if GPIO.input(24) == 1:
			print('Hello')
			# Turn on LED
			GPIO.output(23, GPIO.HIGH)
		else:
			print('Bye')
			GPIO.output(23, GPIO.LOW)

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print('Keyboard Interrupt') # print value of counter  
  
# except:  
    # # this catches ALL other exceptions including errors.  
    # # You won't get any error messages for debugging  
    # # so only use it once your code is working  
    # print('Other Error Occurred')
  
finally:  
    GPIO.cleanup() # this ensures a clean exit
    print('Clean up')
