import os
from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('hello.html')

