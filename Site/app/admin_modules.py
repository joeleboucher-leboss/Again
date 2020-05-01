from flask_babel import _

# Classe de module administrateur
class Admin_module():
    def __init__(self, name, template_location):
        self.name = name
        self.template_location = template_location # Adresse de la page correspondant au module

# Classe de menu administrateur (contient plusieurs modules)
class Admin_menu():
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules

# modules Lots
prize_related_admin_modules = [
    Admin_module(_('Catégories'), 'admin/modules/categories.htm'), # Module de gestion des catégories
    Admin_module(_('Produits standarts'), 'admin/modules/standarts.htm') # Module de gestion des produits standarts
    ]

# modules sécurité
security_related_admin_modules = [

    Admin_module("CAPTCHA", 'admin/modules/CAPTCHA.htm') # Module de CAPTCHA Analytics
]

# Modules documentation
developer_reference = [
    Admin_module(_('Base de données'),'admin/doc/database_structure.htm'), # Documentation base de données
    Admin_module(_('Organisation du site'), 'admin/doc/organisation_site.htm'), # Documentation organisation du site
    Admin_module(_("Organisation des pages"), 'admin/doc/organisation_page.htm'), # Documentation organisation d'une page
    Admin_module(_("CSS"), 'admin/doc/css.htm'), # Documentation CSS
    Admin_module(_("Configuration"), 'admin/doc/configuration.htm'), # Documentation sur le fichier de configuration du site
    Admin_module(_("Authentification"), 'admin/doc/authentification.htm'), # Documentation sur le système d'authentification du site
    Admin_module(_("Traduction"), 'admin/doc/traduction.htm') # Documentation sur le système de traduction du site
    ]

# Liste des menus administrateur
admin_menus = [
    Admin_menu(_('Lots'), prize_related_admin_modules), # Menu Lots
    Admin_menu(_('Sécurité'), security_related_admin_modules), # Menu sécurité
    Admin_menu(_('Documentation'), developer_reference) # Menu Documentation
    ]
