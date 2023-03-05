import RPi.GPIO as GPIO  
import constants
import solenoid
import linearActuator

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(constants.ACTUATOR_0_PIN_A, GPIO.OUT)
GPIO.setup(constants.ACTUATOR_0_PIN_B, GPIO.OUT)
GPIO.setup(constants.ACTUATOR_1_PIN_A, GPIO.OUT)
GPIO.setup(constants.ACTUATOR_1_PIN_B, GPIO.OUT)
GPIO.setup(constants.SOLENOID_0, GPIO.OUT)

try:
    # here you put your main loop or block of code 
    print('Hello World')
    # solenoid.set_solenoid_on(constants.SOLENOID_0)
    # linearActuator.open_drawer(constants.DRAWER_0)
    # linearActuator.open_drawer(constants.DRAWER_1)
    

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print('Keyboard Interrupt') # print value of counter  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print('Other Error Occurred')
  
finally:  
    GPIO.cleanup() # this ensures a clean exit
    print('Clean up')
