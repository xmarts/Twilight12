from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    tasadecambiobill = fields.Float(related='currency_id.rate_ids.rate')
    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),store=True)


    @api.onchange('purchase_id')
    def calcularcambio2(self):
        for record in self:
            porder=record.origin #purchase order name 
            if porder:
                res=self.env['purchase.order'].sudo().search([('name','=',porder)]).cambiobill #busqueda en purchase order en donde el nombre sea igual 'porder' y te regesa el '.'cambiobill de la purchase order
                record[("cambiobill")]=res  #iguala el tipo de cambio al resultado de la busqueda
            elif (record.tasadecambio!=0):
                record['cambiobill'] = 1/record.tasadecambio
    
   

