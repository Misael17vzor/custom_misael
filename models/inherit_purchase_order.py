from odoo import models, fields, api

class InheritPurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    success_level = fields.Many2many(
        "success.level",
        string = "Nivel de satisfaccion"
       
    )

