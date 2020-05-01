import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-guess' #plus tard sera liée à une variable d'environnement pour plus de sécurité

    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = "6Leo2vAUAAAAAHWhJY5Z08lrhUdlq1OKgqh1_Gy_"
    RECAPTCHA_PRIVATE_KEY = "6Leo2vAUAAAAAOJFw5risJDpTVTBrpIyX9lvqWYy"
    RECAPTCHA_OPTIONS = {'theme':'white'}

    VERSION = "0.0.2"
    MAINTENANCE = False


    LANGUAGES = ['fr', 'en', 'de']
