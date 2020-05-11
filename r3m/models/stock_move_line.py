from odoo import models, fields

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    kilos = fields.Integer('Kilos')
    linear_m = fields.Integer('Linear M')
    area_sqm = fields.Integer('AREA SQM')