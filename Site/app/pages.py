from flask import render_template, redirect
from app import app
from . import config


@app.route('/')
@app.route('/index')
def index():
    if config.maintenance == True: #On remplacera cette ligne par une recherche dans la base de données du Site
        return redirect('/maintenance')
    return render_template('index.htm')
@app.route('/maintenance')
def maintenance():
    if config.maintenance == False: #On remplacera cette ligne par une recherche dans la base de données du Site
        return redirect('/')
    return render_template('maintenance.htm')
