from odoo import http, models
from odoo.http import request
from datetime import date, timedelta


class StockPickingController(http.Controller):

    @http.route('/api/receptions', type='json', method=['GET'], cors='*')
    def get_receptions(self):
        result = request.env['stock.picking'].search([('picking_type_code', '=', 'incoming')])
        recepctions = []
        if result:
            for res in result:
                recepctions.append({
                    'Id': res.id,
                    'Name': res.name,
                    'CreateAt': res.create_date,
                    'State': res.state,
                    'Parent_id': res.partner_id.name,
                    'Location_Dest': res.location_dest_id.name,
                    'Products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'Invoice ': res.r3m_account,
                    'Order': res.r3m_order,
                    'ETA': res.r3m_eta,
                    'DestinationPort': res.r3m_destination.name,
                    'Container_Number': res.r3m_container,
                    'Booking_Number': res.r3m_booking,
                    'BL': res.r3m_bl,
                    'Vessel': res.r3m_vessel,
                    'Plant_Ids': res.r3m_partner_plant_ids.mapped('name'),
                    'Plant_Id': res.r3m_plant_id.mapped('name')
                })
        return recepctions

    @http.route('/api/dispatchs', type='json', method=['GET'], cors='*')
    def get_dispatchs(self):
        result = request.env['stock.picking'].search([('picking_type_code', '=', 'outgoing')])
        dispatchs = []
        if result:
            for res in result:
                dispatchs.append({
                    'Id': res.id,
                    'Name': res.name,
                    'CreateAt': res.create_date,
                    'State': res.state,
                    'Parent_id': res.partner_id.name,
                    'Location_Dest': res.location_dest_id.name,
                    'Products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'Invoice ': res.r3m_account,
                    'Order': res.r3m_order,
                    'ETA': res.r3m_eta,
                    'DestinationPort': res.r3m_destination.name,
                    'Container_Number': res.r3m_container,
                    'Booking_Number': res.r3m_booking,
                    'BL': res.r3m_bl,
                    'Vessel': res.r3m_vessel,
                    'Plant_Ids': res.r3m_partner_plant_ids.mapped('name'),
                    'Plant_Id': res.r3m_plant_id.mapped('name')
                })
        return dispatchs

    @http.route('/api/picking', type='json', method=['GET'], cors='*')
    def get_picking_by_id(self,id):
        result = request.env['stock.picking'].search([('id','=',id)])
        recepctions = []
        if result:
            for res in result:
                recepctions.append({
                    'Id': res.id,
                    'Name': res.name,
                    'CreateAt': res.create_date,
                    'State': res.state,
                    'Parent_id': res.partner_id.name,
                    'Location_Dest': res.location_dest_id.name,
                    'Products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'Invoice ': res.r3m_account,
                    'Order': res.r3m_order,
                    'ETA': res.r3m_eta,
                    'DestinationPort': res.r3m_destination.name,
                    'Container_Number': res.r3m_container,
                    'Booking_Number': res.r3m_booking,
                    'BL': res.r3m_bl,
                    'Vessel': res.r3m_vessel,
                    'Plant_Ids': res.r3m_partner_plant_ids.mapped('name'),
                    'Plant_Id': res.r3m_plant_id.mapped('name')
                })
        return recepctions

    @http.route('/api/picking', type='json', method=['GET'], cors='*')
    def get_picking_by_name(self, name):
        result = request.env['stock.picking'].search([('name', '=', name)])
        recepctions = []
        if result:
            for res in result:
                recepctions.append({
                    'Id': res.id,
                    'Name': res.name,
                    'CreateAt': res.create_date,
                    'State': res.state,
                    'Parent_id': res.partner_id.name,
                    'Location_Dest': res.location_dest_id.name,
                    'Products': res.move_line_ids_without_package.mapped('product_id').mapped('display_name'),
                    'Invoice ': res.r3m_account,
                    'Order': res.r3m_order,
                    'ETA': res.r3m_eta,
                    'DestinationPort': res.r3m_destination.name,
                    'Container_Number': res.r3m_container,
                    'Booking_Number': res.r3m_booking,
                    'BL': res.r3m_bl,
                    'Vessel': res.r3m_vessel,
                    'Plant_Ids': res.r3m_partner_plant_ids.mapped('name'),
                    'Plant_Id': res.r3m_plant_id.mapped('name')
                })
        return recepctions