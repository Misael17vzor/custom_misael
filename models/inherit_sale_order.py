from odoo import models, fields, api

class InheritSaleOrder(models.Model):
    _inherit = "sale.order"
    
    success_level = fields.Many2many(
        "success.level",
        string = "Nivel de satisfaccion"
    )
    

    def write(self, vals):
        res = super(InheritSaleOrder, self).write(vals)
        partner = self.env['res.partner'].search([('id','=', self.partner_id.id)])
        if 'state' in vals.keys() and vals['state']=="sale":
            partner.success_level = self.success_level[0]
        if 'state' in vals.keys() and vals['state']=="cancel":
            partner.success_level=False
        return res

