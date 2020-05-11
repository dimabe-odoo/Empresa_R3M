# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    r3m_po = fields.Char('Purchase Order')
    r3m_order = fields.Char('Pedido')
    r3m_destination = fields.Many2one(comodel_name='r3m.port', string = 'Puerto destino')
    r3m_container = fields.Char('Contenedor')
    r3m_booking = fields.Char('Booking Number')
    r3m_bl = fields.Char('BL')
    r3m_vessel = fields.Char('Vessel')
    r3m_account = fields.Char('Cuenta')
    r3m_plant = fields.Char('Planta')
    r3m_eta = fields.Date('ETA')

    remarks = fields.Text('Observaciones')

    # Transporte 

    r3m_truck = fields.Many2one(comodel_name='r3m.truck', string = 'Camión')
    r3m_driver = fields.Many2one(comodel_name='res.partner', string = 'Conductor')
    r3m_date_dispatched = fields.Datetime('Fecha de salida')
    r3m_date_on_port = fields.Datetime('Fecha llegada a puerto')

