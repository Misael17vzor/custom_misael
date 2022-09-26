from odoo import models, fields, api

class InheritPartnerOrder(models.Model):
    _inherit = "res.partner"
    
    success_level = fields.Many2many(
        "success.level",
        string = "Nivel de satisfaccion"
    )

