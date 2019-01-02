# -*- encoding: utf-8 -*-

import logging
from odoo import models, fields, api, tools
from odoo.fields import Datetime as fieldsDatetime
from odoo.exceptions import UserError
from datetime import datetime
import odoo.addons.decimal_precision as dp

_logger = logging.getLogger(__name__)

class AdquatAccountMoveLineGrouped(models.Model):
    
    _name = 'adquat.account.move.line.grouped'
    _auto = False

    _order = "date desc, id desc"

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(AdquatAccountMoveLineGrouped, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        self.init()
        return res


    move_id = fields.Many2one('account.move', string='Journal Entry')
    name = fields.Char(string="Label")
    partner_id = fields.Many2one('res.partner', string='Partner')
    account_id = fields.Many2one('account.account', string='Account')
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    full_reconcile_id = fields.Many2one('account.full.reconcile', string="Matching Number")
    debit = fields.Monetary(currency_field='company_currency_id')
    credit = fields.Monetary(currency_field='company_currency_id')
    date_maturity = fields.Date(string='Due date')

    currency_id = fields.Many2one('res.currency', string='Currency')
    payment_id = fields.Many2one('account.payment', string="Originator Payment")
    statement_line_id = fields.Many2one('account.bank.statement.line', string='Bank statement line reconciled with this entry')
    tax_line_id = fields.Many2one('account.tax', string='Originator tax')
    invoice_id = fields.Many2one('account.invoice')


    date = fields.Date(related='move_id.date', string='Date')
    journal_id = fields.Many2one('account.journal', related='move_id.journal_id', string='Journal')
    ref = fields.Char(related='move_id.ref', string='Reference')
    company_currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string="Company Currency")
    company_id = fields.Many2one('res.company', related='account_id.company_id', string='Company')
    statement_id = fields.Many2one('account.bank.statement', related='statement_line_id.statement_id', string='Statement')
    user_type_id = fields.Many2one('account.account.type', related='account_id.user_type_id')

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'adquat_account_move_line_grouped')
        self._cr.execute(
            "CREATE VIEW adquat_account_move_line_grouped AS (\
                SELECT\
                    l.move_id as move_id,\
                    ROW_NUMBER() OVER (ORDER BY move_id) as id,\
                    l.name as name,\
                    l.partner_id as partner_id,\
                    l.account_id as account_id,\
                    l.analytic_account_id as analytic_account_id,\
                    l.full_reconcile_id as full_reconcile_id,\
                    l.debit as debit,\
                    l.credit as credit,\
                    l.date_maturity as date_maturity,\
                    l.currency_id as currency_id,\
                    l.payment_id as payment_id,\
                    l.statement_line_id as statement_line_id,\
                    l.tax_line_id as tax_line_id,\
                    l.invoice_id as invoice_id\
                FROM (\
                    SELECT\
                        l1.move_id as move_id,\
                        MAX(l1.name) as name,\
                        l1.partner_id as partner_id,\
                        l1.account_id as account_id,\
                        l1.analytic_account_id as analytic_account_id,\
                        l1.full_reconcile_id as full_reconcile_id,\
                        SUM(l1.debit) as debit,\
                        SUM(l1.credit) as credit,\
                        l1.date_maturity as date_maturity,\
                        l1.currency_id as currency_id,\
                        l1.payment_id as payment_id,\
                        l1.statement_line_id as statement_line_id,\
                        l1.tax_line_id as tax_line_id,\
                        l1.invoice_id as invoice_id\
                    FROM account_move_line as l1\
                    WHERE l1.debit = 0 AND l1.credit <> 0\
                    GROUP BY l1.move_id, l1.account_id, l1.partner_id, l1.analytic_account_id, l1.full_reconcile_id, l1.date_maturity, l1.currency_id, l1.payment_id, l1.statement_line_id, l1.tax_line_id, l1.invoice_id\
                    UNION ALL\
                    SELECT\
                        l2.move_id as move_id,\
                        MAX(l2.name) as name,\
                        l2.partner_id as partner_id,\
                        l2.account_id as account_id,\
                        l2.analytic_account_id as analytic_account_id,\
                        l2.full_reconcile_id as full_reconcile_id,\
                        SUM(l2.debit) as debit,\
                        SUM(l2.credit) as credit,\
                        l2.date_maturity as date_maturity,\
                        l2.currency_id as currency_id,\
                        l2.payment_id as payment_id,\
                        l2.statement_line_id as statement_line_id,\
                        l2.tax_line_id as tax_line_id,\
                        l2.invoice_id as invoice_id\
                    FROM account_move_line as l2\
                    WHERE l2.debit <> 0 AND l2.credit = 0\
                    GROUP BY l2.move_id, l2.account_id, l2.partner_id, l2.analytic_account_id, l2.full_reconcile_id, l2.date_maturity, l2.currency_id, l2.payment_id, l2.statement_line_id, l2.tax_line_id, l2.invoice_id\
                    UNION ALL\
                    SELECT\
                        l3.move_id as move_id,\
                        MAX(l3.name) as name,\
                        l3.partner_id as partner_id,\
                        l3.account_id as account_id,\
                        l3.analytic_account_id as analytic_account_id,\
                        l3.full_reconcile_id as full_reconcile_id,\
                        SUM(l3.debit) as debit,\
                        SUM(l3.credit) as credit,\
                        l3.date_maturity as date_maturity,\
                        l3.currency_id as currency_id,\
                        l3.payment_id as payment_id,\
                        l3.statement_line_id as statement_line_id,\
                        l3.tax_line_id as tax_line_id,\
                        l3.invoice_id as invoice_id\
                    FROM account_move_line as l3\
                    WHERE l3.debit <> 0 AND l3.credit <> 0\
                    GROUP BY l3.move_id, l3.account_id, l3.partner_id, l3.analytic_account_id, l3.full_reconcile_id, l3.date_maturity, l3.currency_id, l3.payment_id, l3.statement_line_id, l3.tax_line_id, l3.invoice_id\
                    ) as l\
                )")
              
