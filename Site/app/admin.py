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
        return redirect(url_for('login', next=url_for('admin_dashboard'))) # si l'utilisateur n'est pas connecté, on le redirige vers la page de connexion

    if not(current_user.is_admin):
        return redirect(url_for('restricted')) # si l'utilisateur est connecté mais n'est pas administrateur, on lui affiche la page accès refusé

    categories = Category.query.filter_by(parent_id = None).all()
    newcategoryform = Admin_NewCategoryForm()
    newstandartproduct = Admin_NewStandartProduct()
    standartproducts = Prize.query.filter_by(is_standart = 1).all()

    ##region CATEGORIES

    if newcategoryform.newCategorySubmit.data and newcategoryform.validate_on_submit(): # si l'utilisateur tente de créer une catégorie
        name = Category.query.filter_by(name=newcategoryform.name.data).first()

        if name is not None or name == "": #si le nom existe deja ou est vide, on ne fait rien et on affiche la page (TEMPORAIRE)
            return render_template('admin/dashboard.htm', title=_('Panneau de bord'), admin_menus = modules.admin_menus, newcategoryform=newcategoryform, categories = categories, newstandartproductform=newstandartproduct, standartproducts = standartproducts)

        newCat = Category(name = newcategoryform.name.data) # on crée une nouvelle catégorie
        if (newcategoryform.parent_id.data != ""):
            newCat.parent_id = newcategoryform.parent_id.data # si le formulaire spécifie une catégorie parente, alors on la renseigne

        db.session.add(newCat) # on insère la nouvelle catégorie dans la base de données
        db.session.commit()
        return redirect(url_for('admin_dashboard')) # on recharge la page

    ##endregion

    ##region PRODUITS STANDARTS

    elif newstandartproduct.newStandartProductSubmit and newstandartproduct.validate_on_submit(): # si l'utilisateur tente de créer un produit standart
        name = Prize.query.filter_by(prize_name = newstandartproduct.name.data).first()

        if name is not None or name =="":
            return ("name error") # si le nom est vide ou qu'il existe déjà, on lance une erreur (PROVISOIRE)

        if (newstandartproduct.category.data == "0"): # si la catégorie renseignée est 0, alors on crée le produit sans spécifier de catégorie
            newPrize = Prize(prize_name = newstandartproduct.name.data, is_standart = True, prize_description = newstandartproduct.description.data)

        else: # sinon, on spécifie la catégorie
            newPrize = Prize(prize_name = newstandartproduct.name.data, is_standart = True, prize_description = newstandartproduct.description.data, prize_category = newstandartproduct.category.data)

        db.session.add(newPrize) # on insère le produit dans la base de données
        db.session.commit()
        return redirect(url_for('admin_dashboard')) # on recharge la page

    ##endregion

    # afficher la page
    return render_template('admin/dashboard.htm', title=_('Panneau de bord'), admin_menus = modules.admin_menus, newcategoryform=newcategoryform, categories = categories, newstandartproductform=newstandartproduct, standartproducts = standartproducts, site_version = app.config['VERSION'])
