#!/usr/bin/env python3
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/zero')
def zero():
    return render_template('0-main.html')

@app.route('/one')
def one():
    return render_template('1-main.html')

@app.route('/two')
def two():
    return render_template('2-main.html')

@app.route('/three')
def three():
    return render_template('3-main.html')

@app.route('/four')
def four():
    return render_template('4-main.html')

@app.route('/five')
def five():
    return render_template('5-main.html')

@app.route('/six')
def six():
    return render_template('6-main.html')

@app.route('/seven')
def seven():
    return render_template('7-main.html')

@app.route('/eight')
def eight():
    return render_template('8-main.html')

@app.route('/nine')
def nine():
    return render_template('9-main.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
