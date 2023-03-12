import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	print('test')
	while True:
		if GPIO.input(4) == 0:
			print('Hello')
		else:
			print('Bye')

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
