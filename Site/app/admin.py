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

@app.route('/restricted')
def restricted():
    return render_template('errors/no-access.htm')

@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if not(current_user.is_authenticated):
        return redirect(url_for('login', next=url_for('admin_dashboard')))
    if not(current_user.is_admin):
        return redirect(url_for('restricted'))

    categories = Category.query.filter_by(parent_id = None).all()
    newcategoryform = Admin_NewCategoryForm()
    newstandartproduct = Admin_NewStandartProduct()
    standartproducts = Prize.query.filter_by(is_standart = 1).all()
    if newcategoryform.newCategorySubmit.data and newcategoryform.validate_on_submit():
        name = Category.query.filter_by(name=newcategoryform.name.data).first()
        if name is not None or name == "": #si le nom existe deja ou est vide
            return render_template('admin/dashboard.htm', title=_('Panneau de bord'), admin_menus = modules.admin_menus, newcategoryform=newcategoryform, categories = categories, newstandartproductform=newstandartproduct, standartproducts = standartproducts)
        newCat = Category(name = newcategoryform.name.data)
        if (newcategoryform.parent_id.data != ""):
            newCat.parent_id = newcategoryform.parent_id.data
        db.session.add(newCat)
        db.session.commit()
        return redirect(url_for('admin_dashboard'))

    elif newstandartproduct.newStandartProductSubmit and newstandartproduct.validate_on_submit():
        #insérer ici le code à exécuter lorsque l'administrateur tente de créer un produit standart
        name = Prize.query.filter_by(prize_name = newstandartproduct.name.data).first()
        if name is not None or name =="":
            return ("name error") # Provisoire
        newPrize = Prize(prize_name = newstandartproduct.name.data, is_standart = True, prize_description = newstandartproduct.description.data, prize_category = newstandartproduct.category.data)
        db.session.add(newPrize)
        db.session.commit()
    #return str([field.label for field in newstandartproduct])
    #return render_template('admin/modules/submodules/add_standart.htm', newstandartproductform = newstandartproduct)
    return render_template('admin/dashboard.htm', title=_('Panneau de bord'), admin_menus = modules.admin_menus, newcategoryform=newcategoryform, categories = categories, newstandartproductform=newstandartproduct, standartproducts = standartproducts)
