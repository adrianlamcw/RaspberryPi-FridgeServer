# This program allows a user to enter a
# Code. If the C-Button is pressed on the
# keypad, the input is reset. If the user
# hits the A-Button, the input is checked.

import RPi.GPIO as GPIO
import time
import constants
import solenoid

GPIO.setmode(GPIO.BCM)
# These are the GPIO pin numbers where the
# lines of the keypad matrix are connected
L1 = 5
L2 = 6
L3 = 13
L4 = 19

# These are the four columns
C1 = 12
C2 = 16
C3 = 20
C4 = 21

secretCode_1 = "1111"
secretCode_2 = "2222"
secretCode_1_lock = "1111B"
secretCode_2_lock = "2222B"

input = ""

# Setup GPIO
GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)
GPIO.setup(constants.LED_1_PIN, GPIO.OUT)
GPIO.setup(constants.LED_2_PIN, GPIO.OUT)
GPIO.setup(constants.SWITCH_1_PIN, GPIO.IN)
GPIO.setup(constants.SWITCH_2_PIN, GPIO.IN)
GPIO.setup(constants.SOLENOID_1, GPIO.OUT)
GPIO.setup(constants.SOLENOID_2, GPIO.OUT)

# Use the internal pull-down resistors
GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# The GPIO pin of the column of the key that is currently
# being held down or -1 if no key is pressed
keypadPressed = -1

# This callback registers the key that was pressed
# if no other key is currently pressed
def keypadCallback(channel):
    global keypadPressed
    if keypadPressed == -1:
        keypadPressed = channel

# Detect the rising edges on the column lines of the
# keypad. This way, we can detect if the user presses
# a button when we send a pulse.
GPIO.add_event_detect(C1, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C2, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C3, GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(C4, GPIO.RISING, callback=keypadCallback)

# Sets all lines to a specific state. This is a helper
# for detecting when the user releases a button
def setAllLines(state):
    GPIO.output(L1, state)
    GPIO.output(L2, state)
    GPIO.output(L3, state)
    GPIO.output(L4, state)

def checkSpecialKeys():
    global input
    pressed = False
    GPIO.output(L3, GPIO.HIGH)

    # C is pressed
    if (GPIO.input(C4) == 1):
        print("Input reset!");
        pressed = True

    GPIO.output(L3, GPIO.LOW)
    GPIO.output(L1, GPIO.HIGH)

    # A is pressed
    if (not pressed and GPIO.input(C4) == 1):
        if input == secretCode_1:
            print("Code correct! Unlock Drawer 1")
            # TODO: Unlock a door, turn a light on, etc.
            solenoid.solenoid_unlock(constants.SOLENOID_1, constants.LED_1_PIN)
        elif input == secretCode_2:
            print("Code correct! Unlock Drawer 2")
            # TODO: Unlock a door, turn a light on, etc.
            solenoid.solenoid_unlock(constants.SOLENOID_2, constants.LED_2_PIN)
        elif input == secretCode_1_lock:
            print("Code correct! Lock Drawer 1")
            solenoid.solenoid_lock(constants.SOLENOID_1, constants.LED_1_PIN, constants.SWITCH_1_PIN)
        elif input == secretCode_2_lock:
            print("Code correct! Lock Drawer 2")
            solenoid.solenoid_lock(constants.SOLENOID_2, constants.LED_2_PIN, constants.SWITCH_2_PIN)
        else:
            print("Incorrect code!")
            # TODO: Sound an alarm, send an email, etc.
        pressed = True

    GPIO.output(L3, GPIO.LOW)

    if pressed:
        input = ""

    return pressed

# reads the columns and appends the value, that corresponds
# to the button, to a variable
def readLine(line, characters):
    global input
    # We have to send a pulse on each line to
    # detect button presses
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        input = input + characters[0]
    if(GPIO.input(C2) == 1):
        input = input + characters[1]
    if(GPIO.input(C3) == 1):
        input = input + characters[2]
    if(GPIO.input(C4) == 1):
        input = input + characters[3]
    GPIO.output(line, GPIO.LOW)

def keypad_on():
    try:
        while True:
            # If a button was previously pressed,
            # check, whether the user has released it yet
            global keypadPressed
            if keypadPressed != -1:
                setAllLines(GPIO.HIGH)
                if GPIO.input(keypadPressed) == 0:
                    keypadPressed = -1
                else:
                    time.sleep(0.1)
            # Otherwise, just read the input
            else:
                if not checkSpecialKeys():
                    readLine(L1, ["1","2","3","A"])
                    readLine(L2, ["4","5","6","B"])
                    readLine(L3, ["7","8","9","C"])
                    readLine(L4, ["*","0","#","D"])
                    time.sleep(0.1)
                else:
                    time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nApplication stopped!")
        
    finally:  
        GPIO.cleanup() # this ensures a clean exit
        print('Clean up')
            
keypad_on()
