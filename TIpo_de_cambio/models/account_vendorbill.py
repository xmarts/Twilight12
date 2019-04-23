from odoo import api, fields, models, _

class InvoiceCambio(models.Model):
    _inherit = 'account.invoice'
    cambiobill = fields.Float(string='Tipo de Cambio',digits=(12,3),store=True,compute='calcularcambio3',readonly=0)



    @api.onchange('currency_id','partner_id')
    def calcularcambio3(self):
        for record in self:
            x=record.origin
            if x:
                domain=[('name','=',x)] 
                dicts=self.env['purchase.order'].sudo().search_read(domain,[('cambiobill')])
            #busqueda en purchase order en donde el nombre sea igual 'porder' y te regesa el '.'cambiobill de la purchase order
                for item in dicts:
                    resultado=item['cambiobill']
                    record[("cambiobill")]=float(resultado)  #iguala el tipo de cambio al resultado de la busqueda
            elif (record.tasadecambio!=0):
                record[('cambiobill')] = 1/record.tasadecambio
    
   

