from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
##region utilisateur
class User(UserMixin, db.Model):
    __tablename__ = 'user' # définit le nom de la table qui sera utilisée
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
##endregion

##region catégorie
class Category(db.Model):
    __tablename__ = 'category' # définit le nom de la table qui sera utilisée
    id = db.Column(db.Integer, primary_key=True) # clé primaire
    name = db.Column(db.String(64)) # Nom de la catégorie
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id')) # identifiant de la catégorie parent (clé étrangère)
    children = db.relationship('Category') # propriété qui permet de récupérer les catégories enfant
    def __repr__(self):
        return '<Category {}>'.format(self.name)
##endregion

##region Association Loterie - participants
#participants = Table('participants', Base.metadata,
#    Column('lotery_id', Integer, ForeignKey('loteries.id')),
#    Column('participant_id', Integer, ForeignKey('user.id'))
#)
##endregion

##region lot
class Prize(db.Model):
    __tablename__ = 'prizes' # définit le nom de la table qui sera utilisée
    id = db.Column(db.Integer, primary_key = True) # clé primaire
    prize_name = db.Column(db.String(128)) # Nom du lot
    is_standart = db.Column(db.Boolean) # Indique si ce lot est une vitrine pour plusieurs lots
    prize_description = db.Column(db.String(64000)) # Description du lot
    prize_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    # Pour l'instant pas d'image car alors il faudrait configurer FTP.
    standart_product_id = db.Column (db.Integer, db.ForeignKey('prizes.id'))
    def __repr__(self):
        return '<Prize {}>'.format(self.name)
##endregion

##region Loterie
#class Lotery(db.Model):
#    __tablename__ = 'loteries' # définit le nom de la table qui sera utilisée
#    id = db.Column(db.Integer, primary_key = True) # clé primaire
#    prize = db.Column(db.Integer, db.ForeignKey('prizes.id')) # Lot à gagner
#    vendor = db.Column(db.Integer, db.ForeinKey('user.id')) # Organisateur
#    participants = relationship(
#        'User',
#        secondary = participants,
#        backref = 'loteries'
#    )
##endregion
