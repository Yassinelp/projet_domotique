
from flask import Flask
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


@app.route('/on')
def on():
	GPIO.output(14, GPIO.HIGH)
	GPIO.output(15, GPIO.HIGH)
	return 'ALLUMÉ!'
@app.route('/off')
def off():
        GPIO.output(14, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        return 'ÉTEINT!'

from flask import render_template
@app.route('/projetbreakingbad/hello/<name>')
def hello(name=None):
    return render_template('base.html', name=name)
