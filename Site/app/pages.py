from flask import render_template, redirect
from app import app
from . import config

maintenance = True

@app.route('/')
@app.route('/index')
def index():
    #if maintenance == True:
    return redirect('/maintenance')
    #return render_template('index.htm')
@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.htm')
