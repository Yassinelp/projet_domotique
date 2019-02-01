from flask import Flask
app = Flask(__name__)

from flask import render_template

from temperature import TemperatureSensor 

michel = TemperatureSensor()

@app.route('/temperature/')
def hello():
    temps_c = michel.read_temp_c()
    message_froid = 'il fait froid'
    message_chaud = 'il fait chauuuuuuud'
    message_neutre = 'mouais '
    message = ''
    if temps_c < 20 :
        message = message_froid
    elif temps_c > 30 :
        message = message_chaud
    else:
        message = message_neutre
    return render_template('index.html', message=message, temps_c=temps_c)

