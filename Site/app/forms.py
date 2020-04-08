from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('pseudo', validators=[DataRequired()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Connexion')

class RegistrationForm(FlaskForm):
    username = StringField("pseudo", validators=[DataRequired()])
    email = StringField('e-mail', validators=[DataRequired(), Email()])
    password = PasswordField('mot de passe', validators=[DataRequired()])
    password2 = PasswordField(
        'confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("S'enregistrer")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Veuillez choisir un autre pseudo')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Veuillez utiliser une autre adresse e-mail')
