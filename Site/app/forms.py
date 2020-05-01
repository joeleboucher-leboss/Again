from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import lazy_gettext as _
from app.models import User

# Formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField(_('pseudo'), validators=[DataRequired()])
    password = PasswordField(_('mot de passe'), validators=[DataRequired()])
    remember_me = BooleanField(_('se souvenir de moi'))
    submit = SubmitField(_('connexion'))

# Formulaire d'inscription
class RegistrationForm(FlaskForm):
    username = StringField(_("pseudo"), validators=[DataRequired()])
    email = StringField(_('e-mail'), validators=[DataRequired(), Email()])
    password = PasswordField(_('mot de passe'), validators=[DataRequired()])
    password2 = PasswordField(
        _('confirmer le mot de passe'), validators=[DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()
    submit = SubmitField(_("S'enregistrer"))

    # Méthode de vérification du nom d'utilisateur
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() # On recherche un utilisateur du même nom
        if user is not None:
            raise ValidationError(_('Veuillez choisir un autre pseudo')) # Sil y en existe un, alors on renvoie une erreur à la page

    # Méthode de vérification de l'adresse e-mail
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() # On recherche une adresse e-mail identique
        if user is not None:
            raise ValidationError(_('Veuillez utiliser une autre adresse e-mail')) # S'il en existe une, on renvoie un erreur à la page
# Formulaire de création de nouvelle catégorie (administrateur)
class Admin_NewCategoryForm(FlaskForm):
    name = StringField(_('nom'), validators=[DataRequired()])
    parent_id = HiddenField()
    newCategorySubmit = SubmitField(_('ajouter'))

# Formulaire de création de nouveau produit standart (administrateur)
class Admin_NewStandartProduct(FlaskForm):
    category = HiddenField()
    name = StringField(_('nom'), validators=[DataRequired()])
    description = StringField(_('Description'))
    newStandartProductSubmit = SubmitField(_('ajouter'))
