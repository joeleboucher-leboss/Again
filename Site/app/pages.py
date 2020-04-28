from flask import render_template, redirect, send_from_directory, url_for
from flask import request
from werkzeug.urls import url_parse
#from jinja2 import Template #pour déboguer
from app import app, db, login
from flask_babel import _, refresh
from flask_login import current_user, login_user, logout_user
from app.models import User
from app.config import Config
from app.forms import LoginForm, RegistrationForm
import os
from app.admin import *
from app.sell import *
from app.purchase import *

# routage pour l'icône du site
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():

    if app.config['MAINTENANCE'] == True: #Si l'application est en maintenance
        return redirect('/maintenance') #afficher la page MAINTENANCE
    return render_template('index.htm', title="Again - "+_("Loterie entre particuliers"), site_version = app.config['VERSION']) #page d'accueil

@app.route('/maintenance')
def maintenance():

    if app.config['MAINTENANCE'] == False: #si le site n'est pas en maintenance
        return redirect('/') #renvoyer à l'accueil du site
    return render_template('errors/maintenance.htm', title=_("Cette page est en maintenance."), site_version = app.config['VERSION']) #page de maintenance

@app.route('/login', methods=['GET','POST'])
def login():
    if app.config['MAINTENANCE'] == True: #si le site est en maintenance
        return redirect('/maintenance') #afficher la page de maintenance
    if current_user.is_authenticated: #si l'utilisateur est deja connecté
        return redirect('/') #le renvoyer a l'accueil
    form = LoginForm() #récupérer le type de formulaire dont on a besoin

    if form.validate_on_submit(): # Si le formulaire est reçu et correct
        user = User.query.filter_by(username=form.username.data).first() #on recherche l'utilisateur dans la base de données
        if user is None or not user.check_password(form.password.data): #si la combinaison utilisateur-mdp ne fonctionne pas
            return redirect('/login') #on recharge la page.

        # si c'est bon, on connecte l'utilisateur
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next') # on récupère la page suivante si jamais on se connecte pour accéder a une page spécifique
        if not next_page or url_parse(next_page).netloc != '': #s'il n'y a pas de page suivante ou que l'adresse est erronnée
            next_page = '/' #on renvoie à l'accueil
        return redirect(next_page) #sinon, on renvoie bien a la page suivante

    return render_template('login.htm', form=form, title="Again - "+_("Connexion"), site_version = app.config['VERSION']) #page de connexion

@app.route('/logout')
def logout():
    logout_user() #déconnecter l'utilisateur
    return redirect('/')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if app.config['MAINTENANCE'] == True: #si le site est en maintenance
        return redirect('/maintenance') #page de maintenance
    if current_user.is_authenticated: #si l'utilisateur est deja connecté
        return redirect('/') #on renvoie a la page d'accueil
    form = RegistrationForm() #on récupère le formulaire nécessaire
    if form.validate_on_submit(): #si le formulaire est reçu et bon
        user = User(username=form.username.data, email=form.email.data) #on crée un objet utilisateur
        user.set_password(form.password.data) #on lui renseigne le mot de passe par la méthode set_password
        db.session.add(user) #on ajoute l'utilisateur a la base de données
        db.session.commit() #on enregistre en ligne les modifications

        # ICI INSÉRER CODE ENVOI EMAIL CONFIRMATION OU PAGE DE CONFIRMATION D'INSCRIPTION

        return redirect('/login') #on renvoie a la page de connexion
    #on affiche le formulaire d'inscription
    return render_template('register.htm', title=_("S'enregistrer"), site_version = app.config['VERSION'], form=form)
