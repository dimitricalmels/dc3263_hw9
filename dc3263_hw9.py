from flask import Flask
from flask import render_template
from random import randint



app = Flask(__name__)
@app.route('/')
def quote() :

    with open('inspiration.txt', 'r') as fr:

        lineset = fr.read()
        N = len(lineset.split('\n'))
        i = randint(0, N)
        l = lineset.split('\n')[i]

    return render_template('dc3263_hw9.html', line = l)