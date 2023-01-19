from flask import Flask, render_template, jsonify
import datetime
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
   
@app.route("/test_endpoint", methods=["GET"])
def test_endpoint():
   data = {"key1": "value1", "key2": "value2"}
   return jsonify(data)

if __name__ == "__main__":
   app.run(host='10.40.82.177', port=80, debug=True)
