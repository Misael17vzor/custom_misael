#     # -*- coding: utf-8 -*-
# from odoo import api, fields, models, _
# from odoo.exceptions import UserError
# from odoo.tools.date_utils import get_month, get_fiscal_year
# from odoo.tools.misc import format_date

# import re
# from collections import defaultdict
# import json

# class AccountPaymentsPhaseWizard(models.TransientModel):
#     _name = "account.payments.phase.wizard"
#     _description = "Update the phase for multi payemnt"

#    # define the phase field which you will use to change the phase for the selected payments, for example if the phase field is a selection
#     phase = fields.Selection([('phase1', 'phase1'), ('phase2', 'phase2'), ('phase3', 'phase3')],string='phase')

#     # method update_payments_phase which will be called from wizard once click on Update phase button
#     @api.multi
#     def update_payments_phase(self):
#         # return all selected payments using active_ids and you can filter them and use any validation you want
#         payments = self.env['account.payments'].browse(self._context.get('active_ids'))
#         # loop the payments
#         for payment in payments:
#             # set the selected phase for each payment
#             payment.phase = self.phase