from flask import Flask, render_template, request
from app.config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel

app = Flask(__name__) # Création de l'application flask
app.config.from_object(Config) # Initialisation des paramètres de configuration à partir du fichier config.py
db = SQLAlchemy(app) # Création d'un gestionnaire de base de données
migrate = Migrate(app, db) # Création d'un gestionnaire de migrations
login = LoginManager(app) # Création d'un gestionnaire d'authentification
babel = Babel(app) # Création d'un gestionnaire de langues

@babel.localeselector
def get_locale(): # Permet d'obtenir la langue la plus appropriée par rapport au navigateur de l'utilisateur. Fonction directement utilisée par Babel
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import pages, models
