from flask import Flask, render_template, jsonify, send_file, abort
import datetime
import camera
import RPi.GPIO as GPIO  
import constants
import solenoid

# Set the GPIO numbering mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(constants.LED_1_PIN, GPIO.OUT)
GPIO.setup(constants.LED_2_PIN, GPIO.OUT)
GPIO.setup(constants.SWITCH_1_PIN, GPIO.IN)
GPIO.setup(constants.SWITCH_2_PIN, GPIO.IN)
GPIO.setup(constants.SOLENOID_1, GPIO.OUT)
GPIO.setup(constants.SOLENOID_2, GPIO.OUT)

try:
    # here you put your main loop or block of code 
    print('Hello World')
    
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
        if GPIO.input(constants.SOLENOID_1):
            lock_1 = False
        else:
            lock_1 = True
        if GPIO.input(constants.SOLENOID_2):
            lock_2 = False
        else:
            lock_2 = True
        data = {
            "temperature": 22,
            "drawerData": [
                {
                "id": 1,
                "name": "Test User 1",
                "camera": True,
                "lock": lock_1
                },
                {
                "id": 2,
                "name": "Test User 2",
                "camera": False,
                "lock": lock_2
                }]}
        return jsonify(data)
        
    @app.route("/unlock/<username>", methods=["GET"])
    def unlock(username):
        if(username == "1"):
            solenoid.solenoid_unlock(constants.SOLENOID_1, constants.LED_1_PIN)
        elif(username == "2"):
            solenoid.solenoid_unlock(constants.SOLENOID_2, constants.LED_2_PIN)
        else:
            abort(400, "Incorrect ID!") 
        return f"Unlock, {username}"
        
    @app.route("/lock/<username>", methods=["GET"])
    def lock(username):
        if(username == "1"):
            if not solenoid.solenoid_lock(constants.SOLENOID_1, constants.LED_1_PIN, constants.SWITCH_1_PIN):
                abort(400, "Drawer not closed properly")
        elif(username == "2"):
            if not solenoid.solenoid_lock(constants.SOLENOID_2, constants.LED_2_PIN, constants.SWITCH_2_PIN):
                abort(400, "Drawer not closed properly")
        else:
            abort(400, "Incorrect ID!") 
        return f"Lock, {username}"
        
    @app.route("/camera", methods=["GET"])
    def get_image():
        camera.take_picture()
        image_path = "images/test2.jpeg"
        return send_file(image_path)

    if __name__ == "__main__":
        # Start the Flask server
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
