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

@app.route("/view-prize") # Page de visualisation d'un lot
def view_prize():
    return render_template("purchase/display_product.htm", title=_('Article'), site_version = app.config['VERSION'])

@app.route("/purchase-confirm") # Page de confirmation de participation
def confirm_purchase():
    return render_template("purchase/purchase_validated.htm", title=_('Confirmation'), site_version = app.config['VERSION'])
