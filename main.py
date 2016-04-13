import os
from flask import Flask, render_template, request
from ardour import main as shelly

app = Flask(__name__)

shellified=""""""

def preProcess(txt):
    txt = txt.replace("\n",".\n")
    txt = txt.replace("..",".")
    return txt

@app.route('/')
def index():
    return render_template('index.html', shellified = shellified)

@app.route('/stupid.css')
def stupid():
    return render_template('stupid.css')

@app.route('/upload', methods=['POST'])
def upload():
    preshellified = request.form['to']
    if 'adv' in request.form:
        advanced=True
    else:
        advanced=False
    return render_template('index.html', shellified=shelly(
                           preProcess(preshellified), not advanced))

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port)
