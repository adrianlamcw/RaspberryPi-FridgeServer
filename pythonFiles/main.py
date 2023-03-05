from flask import Flask, render_template, jsonify, send_file, abort
import datetime
import timers
import camera
import RPi.GPIO as GPIO  
import constants
import solenoid
import linearActuator

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(constants.ACTUATOR_1_PIN_A, GPIO.OUT)
GPIO.setup(constants.ACTUATOR_1_PIN_B, GPIO.OUT)
GPIO.setup(constants.ACTUATOR_2_PIN_A, GPIO.OUT)
GPIO.setup(constants.ACTUATOR_2_PIN_B, GPIO.OUT)
GPIO.setup(constants.SOLENOID_1, GPIO.OUT)

try:
    # here you put your main loop or block of code 
    print('Hello World')
    # solenoid.set_solenoid_on(constants.SOLENOID_1)
    # linearActuator.open_drawer(constants.DRAWER_1)
    # linearActuator.open_drawer(constants.DRAWER_2)
    
    app = Flask(__name__)
    @app.route("/")
    def hello():
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        templateData = {
          'title' : 'HELLO!',
          'time': timeString
          }
        return render_template('index.html', **templateData)
       
    @app.route("/ping", methods=["GET"])
    def get_ping():
        data = {"key1": "value1", "key2": "value2"}
        return jsonify(data)
        
    @app.route("/status", methods=["GET"])
    def get_status():
        data = {
            "temperature": "4",
            "drawerData": [
                {
                "id": 1,
                "name": "Test User 1",
                "camera": True
                },
                {
                "id": 2,
                "name": "Test User 2",
                "camera": False
                }]}
        return jsonify(data)
        
    @app.route("/unlock/<username>", methods=["GET"])
    def unlock(username):
        if(username == "1"):
            solenoid.set_solenoid_off(constants.SOLENOID_1)
            print('unlock')
        elif(username == "2"):
            solenoid.set_solenoid_off(constants.SOLENOID_2)
        else:
            abort(400, "Incorrect ID!") 
        return f"Unlock, {username}"
        
    @app.route("/lock/<username>", methods=["GET"])
    def lock(username):
        if(username == "1"):
            solenoid.set_solenoid_on(constants.SOLENOID_1)
            print('lock')
        elif(username == "2"):
            solenoid.set_solenoid_on(constants.SOLENOID_2)
        else:
            abort(400, "Incorrect ID!") 
        return f"Lock, {username}"
        
    @app.route("/camera", methods=["GET"])
    def get_image():
        camera.take_picture()
        image_path = "images/test2.jpeg"
        return send_file(image_path)

    if __name__ == "__main__":
        app.run(host='192.168.121.17', port=80, debug=True)
    

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
