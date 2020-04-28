import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'you-will-never-guess' #plus tard sera liée à une variable d'environnement pour plus de sécurité

    VERSION = "0.0.1"
    MAINTENANCE = False


    LANGUAGES = ['fr', 'en', 'de']
