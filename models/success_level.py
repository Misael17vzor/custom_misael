from odoo import models, fields, api

class SuccessLevel(models.Model):
    #
    _name = 'success.level'
    _description = 'la descripcion'

    name = fields.Char(string='Nombre', required=True)
    lvl = fields.Selection(
        string='Nivel de satisfaccion',
        selection= [
            ('1' , '1'),('2', '2'),('3', '3')
        ],
        default=''
    )
    notes = fields.Text(string='Nota')
    # tags = fields.Many2many()

    # success_tag_ids = fields.Many2many(
    #     'success.tag.ids', 'success_tag_rel','success_id', 'success_tag_id', string='Tags')
    #     # help="Classify and analyze your lead/opportunity categories like: Training, Service")
