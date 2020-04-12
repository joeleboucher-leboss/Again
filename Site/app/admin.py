from flask import render_template, redirect, url_for
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
import app.admin_modules as modules

@app.route('/restricted')
def restricted():
    return render_template('errors/no-access.htm')

@app.route('/admin')
def admin_dashboard():
    if not(current_user.is_authenticated):
        return redirect(url_for('login', next=url_for('admin_dashboard')))
    if not(current_user.is_admin):
        return redirect(url_for('restricted'))
    return render_template('admin/dashboard.htm', title=_('Panneau de bord'), admin_menus = modules.admin_menus)
