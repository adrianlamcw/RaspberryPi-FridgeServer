import RPi.GPIO as GPIO
import time
import constants

def extend_actuator(pinA, pinB):
    # Turn the pin on and off
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)

    time.sleep(2)

    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    
    time.sleep(3)

def open_drawer(drawer_id):
    if drawer_id == constants.DRAWER_1:
        extend_actuator(constants.ACTUATOR_1_PIN_A, constants.ACTUATOR_1_PIN_B)
    elif drawer_id == constants.DRAWER_2:
        extend_actuator(constants.ACTUATOR_2_PIN_A, constants.ACTUATOR_2_PIN_B)
