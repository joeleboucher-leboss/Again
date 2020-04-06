from flask import render_template
from app import app
from . import config

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.htm')
