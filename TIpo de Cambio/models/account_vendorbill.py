from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),store=True,compute='calcularcambio2',readonly=0)
    cambiobill2 = fields.Char(string='Tipo de Cambio',digits=(12,3),store=True,compute='calcularcambio2',readonly=0)


    @api.onchange('currency_id','partner_id')
    def calcularcambio2(self):
        x=self.origin
        resultado=self.env['purchase.order'].sudo().search([('name','=',x)])#busqueda en purchase order en donde el nombre sea igual 'porder' y te regesa el '.'cambiobill de la purchase order
        for record in self:
            record[("cambiobill2")]=resultado  #iguala el tipo de cambio al resultado de la busqueda
       
    @api.onchange('currency_id','partner_id')
    def calcularcambio2(self):
        x=self.origin
        resultado=self.env['purchase.order'].sudo().search([('name','=',x)]).cambiobill
         #busqueda en purchase order en donde el nombre sea igual 'porder' y te regesa el '.'cambiobill de la purchase order
        for record in self:
            if porder:
                record[("cambiobill")]=float(resultado)  #iguala el tipo de cambio al resultado de la busqueda
            elif (record.tasadecambio!=0):
                record[('cambiobill')] = 1/record.tasadecambio
    
   

