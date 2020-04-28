from flask import render_template, redirect, url_for
from flask import request
from werkzeug.urls import url_parse
#from jinja2 import Template #pour déboguer
from app import app, db, login
from flask_babel import _, refresh
from flask_login import current_user, login_user, logout_user
from app.models import User, Category, Prize
from app.config import Config
from app.forms import LoginForm, RegistrationForm, Admin_NewCategoryForm, Admin_NewStandartProduct
import os
import app.admin_modules as modules

@app.route("/sell")
def sell():
    return render_template("sell/sell_article.htm", title=_('Créer une loterie'))

@app.route("/sell-preview")
def sell_preview():
    return render_template("sell/sell_article_preview.htm", title=_('Vérifier votre loterie'))
