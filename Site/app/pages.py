 from flask import render_template, redirect
from app import app
from . import config
import sqlite3
import os

@app.route('/')
@app.route('/index')
def index():
    #On va d'abord chercher les données relatives au site
    ##region requête SQL
    conn = sqlite3.connect("again.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM donnees_site")
    donnees_site = cur.fetchone()
    conn.close()
    ##endregion

    if donnees_site['maintenance'] == 1: #On remplacera cette ligne par une recherche dans la base de données du Site
        return redirect('/maintenance')
    return render_template('index.htm')

@app.route('/maintenance')
def maintenance():
    ##region requête SQL
    conn = sqlite3.connect("again.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM donnees_site")
    donnees_site = cur.fetchone()
    conn.close()
    ##endregion

    if donnees_site['maintenance'] != 1: #On remplacera cette ligne par une recherche dans la base de données du Site
        return redirect('/')
    return render_template('maintenance.htm')
