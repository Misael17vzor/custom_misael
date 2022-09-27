    # -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.date_utils import get_month, get_fiscal_year
from odoo.tools.misc import format_date

import re
from collections import defaultdict
import json

class ChangePrice(models.TransientModel):
    _name = "change.price"
    _description = "Change Price"
    product_ids =  fields.Many2many('product.template')
    new_product_price = fields.Float('Nuevo Precio')

    @api.model
    def default_get(self, fields_list):
        values = super(ChangePrice, self).default_get(fields_list)
        active_product_ids = self.env['product.template']
        if self.env.context['active_model'] == 'product.template' and 'active_ids' in self.env.context:
            active_product_ids = self.env['product.template'].browse(self.env.context['active_ids'])
        values['product_ids'] = [(6, 0, active_product_ids.ids)]
        return values



    