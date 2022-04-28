import RPi.GPIO as GPIO
import os
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
pins = [22,27,23,24]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

@app.route("/", methods=['GET', 'POST'])
def index():
	print('mt 1')
	if request.method == 'POST':
		print("up")
		print(request.form.get('up'))
		print("down")
		print(request.form.get('down'))
		print("left")
		print(request.form.get('left'))
		print("right")
		print(request.form.get('right'))

		if request.form.get('up') == 'up':
			os.system("bash /home/pi/up.sh")  # up
		if  request.form.get('down') == 'down':
			os.system("bash /home/pi/down.sh") # down
		if request.form.get('left') == 'left': 
			os.system("bash /home/pi/left.sh")  # left
		if  request.form.get('right') == 'right':
			os.system("bash /home/pi/right.sh")  # right
		if  request.form.get('stop') == 'stop':
			os.system("bash /home/pi/stop.sh")  # stop

		if request.form.get('Sup') == 'Sup':
                        os.system("python /home/pi/servo14.py")  # up
		if  request.form.get('Sdown') == 'Sdown':
                        os.system("python /home/pi/servo14RE.py") # down
		if request.form.get('Sleft') == 'Sleft':
                        os.system("python /home/pi/servo13.py")  # left
		if  request.form.get('Sright') == 'Sright':
                        os.system("python /home/pi/servo13RE.py")  # right
		if  request.form.get('home') == 'home':
			os.system("python /home/pi/home.py")  # home

		if  request.form.get('rVideo') == 'rVideo':
			os.system("bash /home/pi/restartcamer.sh")  # home

#	elif request.method == 'GET':
#		return render_template('index.html')
	return render_template('index.html') 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
