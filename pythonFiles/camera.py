import time
from picamera2 import Picamera2, Preview

def take_picture():
	picam = Picamera2()

	config = picam.create_preview_configuration()
	picam.configure(config)

	picam.start_preview(Preview.QTGL)

	picam.start()
	time.sleep(2)
	picam.capture_file('images/test2.jpeg')

	picam.close()
