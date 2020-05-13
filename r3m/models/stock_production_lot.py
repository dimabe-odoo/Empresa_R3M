from odoo import models, fields

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    kilos = fields.Integer('Kilos')
    linear_m = fields.Integer('Linear M')
    area_sqm = fields.Integer('AREA SQM')