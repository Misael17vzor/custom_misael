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
    new_product_price = fields.Float()

    @api.model
    def default_get(self, fields_list):
        values = super(ReSequenceWizard, self).default_get(fields_list)
        active_product_ids = self.env['product.template']
        if self.env.context['active_model'] == 'product.template' and 'active_ids' in self.env.context:
            active_product_ids = self.env['product.template'].browse(self.env.context['active_ids'])
        if len(active_product_ids.journal_id) > 1:
            raise UserError(_('You can only resequence items from the same journal'))
        move_types = set(active_product_ids.mapped('move_type'))
        if (
            active_product_ids.journal_id.refund_sequence
            and ('in_refund' in move_types or 'out_refund' in move_types)
            and len(move_types) > 1
        ):
            raise UserError(_('The sequences of this journal are different for Invoices and Refunds but you selected some of both types.'))
        values['move_ids'] = [(6, 0, active_product_ids.ids)]
        return values