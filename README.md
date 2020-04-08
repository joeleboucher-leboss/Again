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
├── **templates** *(CETTE PARTIE SERA AMENÉE A CHANGER AVEC L'INTRODUCTION DE BOOTSTRAP)*  
│   ├── **elements** *(templates réutilisables)*  
│   ├── index.htm *(page d'accueil)*  
│   ├── login.htm *(page de connexion)*  
│   ├── register.htm *(page d'inscription)*  
│   └── maintenance.htm *(page de maintenance)*  
├── __ init __ .py *(initialisation de l'application)*  
├── forms.py *(contient les objets formulaires utilisés dans le site)*  
├── app.db *(base de données de l'application)*  
├── config.py *(données et variables nécessaires au fonctionnement du site)*  
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
  arguments: --  
  utilise: navBar.htm, footer.htm
- **register.htm *(inscription)***  
  arguments: form  
  utilise: navBar.htm, footer.htm
- **index.htm *(Liste des lots, page d'accueil)***  
  arguments: --  
  utilise: navBar.htm, footer.htm
- **maintenance.htm *(page utilisée pour bloquer le site)***  
  arguments:  
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
## Nomenclature CSS
*Cette rubrique entière sera amenée à changer avec l'introduction de Bootstrap*
### Elements réutilisables

**body** [again-base.css]  
├── **navBar** *(barre de navigation)* [again-navBar.css]  
│   ├── **logo** *(logo de la barre de navigation)* [again-navBar.css]  
│   ├── **-** *()*  
│   ├── **-** *()*  
│   └── **-** *()*   
├── **footer** *(pied de page)* [again-footer.css]  
│   ├── **-** *()*   
│   ├── **-** *()*   
│   └── **-** *()*   
├── **a** *(hyperlien)* [again-base.css]  
├── **h1** *(Titre 1)* [again-base.css]  
└── **-** *()*
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
- **version** [string] *(La version actuelle du site en ligne)*
- **maintenance** [bool] *(True ou False, indique si le site est en maintenance ou non)*
<!--#endregion-->
<!--#region système d'authentification-->
## Système d'authentification

### Librairies utilisées
- On utilise la librairie *flask-login* pour gérer le système d'authentification. Cette librairie permet en outre de garder une session ouverte, et ce à travers une variable accessible également depuis les templates sans avoir à la passer en argument: *current_user*
- On utilise la librairie *flask-wtf* pour gérer les formulaires et s'en servir comme objets et utiliser des outils de vérification optimisés
<!--#endregion-->
