from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import lazy_gettext as _
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_('pseudo'), validators=[DataRequired()])
    password = PasswordField(_('mot de passe'), validators=[DataRequired()])
    remember_me = BooleanField(_('se souvenir de moi'))
    submit = SubmitField(_('connexion'))

class RegistrationForm(FlaskForm):
    username = StringField(_("pseudo"), validators=[DataRequired()])
    email = StringField(_('e-mail'), validators=[DataRequired(), Email()])
    password = PasswordField(_('mot de passe'), validators=[DataRequired()])
    password2 = PasswordField(
        _('confirmer le mot de passe'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_("S'enregistrer"))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Veuillez choisir un autre pseudo'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Veuillez utiliser une autre adresse e-mail'))
