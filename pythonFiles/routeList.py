from flask import Flask, render_template, jsonify, send_file
import datetime
import timers
import camera

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
def test_endpoint():
   data = {"key1": "value1", "key2": "value2"}
   return jsonify(data)

@app.route("/image", methods=["GET"])
def get_image():
   camera.take_picture()
   image_path = "images/test2.jpeg"
   return send_file(image_path)

@app.route("/check_groceries/<username>", methods=["GET"])
def check_groceries(username):
   return f"Hi, {username}"

@app.route("/lock/<username>", methods=["GET"])
def lock(username):
   return f"Lock, {username}"

@app.route("/unlock/<username>", methods=["GET"])
def unlock(username):
   return f"Unlock, {username}"

if __name__ == "__main__":
   app.run(host='192.168.121.17', port=80, debug=True)
