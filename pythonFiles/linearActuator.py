import RPi.GPIO as GPIO
import timers
import constants

def extend_actuator(pinA, pinB):
    # Turn the pin on and off
    GPIO.output(pinA, GPIO.HIGH)
    GPIO.output(pinB, GPIO.LOW)

    timers.set_timer(5)

    GPIO.output(pinA, GPIO.LOW)
    GPIO.output(pinB, GPIO.HIGH)
    
    timers.set_timer(6)

def open_drawer(drawer_id):
    if drawer_id == constants.DRAWER_0:
        extend_actuator(constants.ACTUATOR_0_PIN_A, constants.ACTUATOR_0_PIN_B)
    if drawer_id == constants.DRAWER_1:
        extend_actuator(constants.ACTUATOR_1_PIN_A, constants.ACTUATOR_1_PIN_B)
