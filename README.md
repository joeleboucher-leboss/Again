# AGAIN
<!-- Pour visualiser ce fichier joliment sur Atome comme si c'était un pdf, double-cliquer dessus dans l'arborescence à gauche et choisir "Markdown preview"-->
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
│   └── maintenance.htm *(page de maintenance)*  
├── __ init __ .py  
├── config.py *(configuration du serveur flask)*  
└── pages.py *(contient le script principal du serveur)*

## Organisation page HTML
- section *barre de navigation* (?)
- section *contenu*
- section *pied de page*

### Templates réutilisables
- **navBar.htm *(barre de navigation)***   
  arguments: --
- **footer.htm *(pied de page)***  
  arguments: --

## Nomenclature CSS
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

## Nomenclature base de données

### Données Site
- **version** [string] *(La version actuelle du site en ligne)*
- **maintenance** [bool] *(True ou False, indique si le site est en maintenance ou non)*
