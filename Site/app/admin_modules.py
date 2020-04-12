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
admin_menus = [Admin_menu(_('Lots'), prize_related_admin_modules)]
