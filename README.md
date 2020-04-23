# AGAIN
<!-- Pour visualiser ce fichier joliment sur Atome comme si c'était un pdf, clic droit dessus dans l'arborescence à gauche et choisir "Markdown preview"
Pour pouvoir alléger le code, ajouter le package "custom folds" à Atom.
Il suffira de faire Ctrl+Maj+[ pour cacher une région et Ctrl+Maj+] pour la développer.-->

<!--#region Arborescence -->
## Arborescence du site

**app**  
├── **static**  
│   ├── **css** *(feuilles de style)*  
│   ├── **fonts** *(polices)*  
│   ├── **img** *(images de contenu)*  
│   └── **js** *(fichiers javascript)*  
├── **templates**   
│   ├── **elements** *(templates réutilisables)*  
│   ├── index.htm *(page d'accueil)*  
│   ├── login.htm *(page de connexion)*  
│   ├── register.htm *(page d'inscription)*  
│   └── maintenance.htm *(page de maintenance)*  
├── **translations**   
│   ├── **de** *(allemand)*   
│   │   ├── .../messages.mo *(dictionnaire allemand)*  
│   │   └── .../messages.po *(catalogue allemand)*  
│   └── **en** *(anglais)*   
│   │   ├── .../messages.mo *(dictionnaire anglais)*  
│   │   └── .../messages.po *(catalogue anglais)*  
├── __ init __ .py *(initialisation de l'application)*  
├── forms.py *(contient les objets formulaires utilisés dans le site)*  
├── app.db *(base de données de l'application)*  
├── config.py *(données et variables nécessaires au fonctionnement du site)*  
├── babel.cfg *(informations pour babel, indique où scanner les fichiers à traduire)*  
├── messages.pot *(modèle de traduction)*  
├── models.py *(contient les classes des objets utilisés dans le site)*  
└── pages.py *(contient le script principal du serveur)*
<!--#endregion-->
<!--#region Pages HTML-->

## Organisation page HTML
- section *barre de navigation*
- section *contenu*
- section *pied de page*

### Pages principales
- **login.htm *(connexion)***  
  arguments: form  
  utilise: navBar.htm, footer.htm
- **register.htm *(inscription)***  
  arguments: form  
  utilise: navBar.htm, footer.htm
- **index.htm *(Liste des lots, page d'accueil)***  
  arguments: --  
  utilise: navBar.htm, footer.htm
- **maintenance.htm *(page utilisée pour bloquer le site)***  
  arguments: --  
  utilise:  navBarStatic.htm, footer.htm  

### Templates réutilisables
*Cette rubrique entière sera amenée à changer avec l'introduction de Bootstrap*
- **navBarStatic.htm *(barre de navigation sans fonctionnalités)***  
  arguments: --
- **navBar.htm *(barre de navigation)***   
  arguments: --
- **footer.htm *(pied de page)***  
  arguments: --

<!--#endregion-->
<!--#region CSS-->
## Bibliothèque css
On utilise une version personnalisée de bootstrap.css pour offrir une expérience fluide et agréable (et pour gagner en temps de développement)
<!--#endregion-->
<!--#region BDD-->
## Nomenclature base de données
### Gestionnaire de bases de Données
- On utilise la librairie *flask-sqlalchemy* qui permet de définir et utiliser les lignes d'une base de données comme des objets dont on définit soi-même une classe. Ceci permet d'être très efficace sans avoir à écrire de SQL, et on gagne beaucoup en clarté, concision et élégance.
- On utilise la librairie *flask-migrate* qui permet de mettre a jour la structure d'une base de données existante  
      $ flask db migrate -m 'message'

### Utilisateurs
Classe User dans app.models, *dérive de UserMixin et db.Model*

*UserMixin permet à l'objet User d'être utilisé par la librairie de flask-login pour l'authentification*  
*db.Model permet de définir des variables de format conforme à une base de données*
- **id** [INTEGER] *(clé primaire)*
- **username** [STRING] *(nom d'utilisateur)*
- **email** [STRING] *(adresse mail de l'utilisateur)*
- **password_hash** [STRING] *(mot généré à partir du mot de passe: on n'enregistre pas directement le mot de passe!)*

<!--#endregion-->
<!--#region configuration du site -->
## Configuration du site
Classe Config dans app.config
- **SQLALCHEMY_DATABASE_URI** *(adresse de la base de données)*
- **SQLALCHEMY_TRACK_MODIFICATIONS**
- **SECRET_KEY** [string] *(clé de sécurité contre les attaques CSRF, intégralement géré par les modules FLASK)*
- **VERSION** [string] *(La version actuelle du site en ligne)*
- **MAINTENANCE** [bool] *(True ou False, indique si le site est en maintenance ou non)*

<!--#endregion-->
<!--#region système d'authentification-->
## Système d'authentification

### Librairies utilisées
- On utilise la librairie *flask-login* pour gérer le système d'authentification. Cette librairie permet en outre de garder une session ouverte, et ce à travers une variable accessible également depuis les templates sans avoir à la passer en argument: *current_user*
- On utilise la librairie *flask-wtf* pour gérer les formulaires et s'en servir comme objets et utiliser des outils de vérification optimisés

<!--#endregion-->
<!--#region Babel (traduction)-->
## Système de traduction
### Librairie utilisée
On utilise la librairie *flask-babel* qui permet la gestion de plusieurs langues.
### Fonctionnement dans l'application
*flask-babel* propose les fonctions *_* et *lazy_gettext* qui prennent en argument une chaîne de caractères, recherchent dans un dictionnaire associé à la langue d'arrivée la chaîne de caractères et renvoie la traduction de cette chaîne.  

*nuance:* lazy_gettext *n'est appelée que lorsque l'objet est utilisé, et non en avance, donc pour les formulaires, il faut utiliser cette méthode puisqu'ils sont initialisés avant que l'on connaisse la langue utilisateur*  

C'est parce que la méthode qui permet d'appeler la traduction est nommée _ que l'on trouve dans le code la plupart des texts enveloppés dans des *_()*, comme suit.  

    from flask_babel import _
    #
    render_template("index.htm", title=\_('Menu principal'))

### Utilisation des dictionnaires
Les dictionnaires sont stockés dans les répertoires du type app/translations/en/LC_MESSAGES  
La génération d'un dictionnaire se fait en 3 parties:
- Génération d'un **modèle de traduction** qui contient toutes les chaînes à traduire (se placer dans /Site/app)  

      $ pybabel extract -F babel.cfg -k \_l -o messages.pot .

    *babel.cfg* est le fichier qui indique à babel quels sont les types de fichiers à scanner (ici les fichiers .py et .htm)
- Génération d'un catalogue de traduction (.po) pour chaque langue dans le répertoire translations/en/LC_MESSAGES  

  la première fois (se placer dans /Site/app):

       $ pybabel init -i messages.pot -d app/translations -l en

  Si ce fichier existe déjà et qu'on souhaite le mettre à jour avec les nouveaux messages, alors il suffit de faire la mise a jour depuis le logiciel Poedit.   
  En utilisant ce même logiciel, on procède à la **traduction** des messages et on enregistre bien le fichier .po que l'on est en train de modifier.  
  **TOUJOURS DÉCHOCHER L'OPTION A REVISER DANS LES TRADUCTIONS, SINON CE NE SERA PAS PRIS EN COMPTE**

- on compile le tout en une sorte de dictionnaire utilisable par babel (.mo) avec la commande (se placer dans /Site):

      $ pybabel compile -d app/translations


<!--#endregion-->
<!--#region Choses à améliorer-->
## Choses à améliorer


<!--#endregion-->
<!--#region références-->
## Références
[The flask mega tutorial](https://l.messenger.com/l.php?u=https%3A%2F%2Fblog.miguelgrinberg.com%2Fpost%2Fthe-flask-mega-tutorial-part-i-hello-world&h=AT0SJg8btXHBXAVtOC1ykmdBcyK92XKPvsI6ofYi1LFKN7TFkgr9N_FECaThZVsaruGnKIoSFfYjS_4x6_aT_QUEZChbn8R4B2NngwjbHl7TBJ1APa6R0bQreqgGM0dLo7g)  
[Documentation bootstrap](https://bootstrap.build/app)
<!--#endregion-->
