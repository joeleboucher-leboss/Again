from flask_babel import _

class Admin_module():
    def __init__(self, name, template_location):
        self.name = name
        self.template_location = template_location
class Admin_menu():
    def __init__(self, name, modules):
        self.name = name
        self.modules = modules


prize_related_admin_modules = [Admin_module(_('Catégories'), 'admin/modules/categories.htm'), Admin_module(_('Produits standarts'), 'admin/modules/standarts.htm')]
developer_reference = [Admin_module(_('Base de données'),'admin/doc/database_structure.htm'),
    Admin_module(_('Organisation du site'), 'admin/doc/organisation_site.htm'),
    Admin_module(_("Organisation des pages"), 'admin/doc/organisation_page.htm'),
    Admin_module(_("CSS"), 'admin/doc/css.htm'),
    Admin_module(_("Configuration"), 'admin/doc/configuration.htm'),
    Admin_module(_("Authentification"), 'admin/doc/authentification.htm'),
    Admin_module(_("Traduction"), 'admin/doc/traduction.htm')]
admin_menus = [Admin_menu(_('Lots'), prize_related_admin_modules), Admin_menu(_('Documentation'), developer_reference)]
