from odoo import fields, models
from odoo.odoo.tools.populate import compute


class Visitor_Management(models.Model):
    _name = 'visitor.management'
    _description = 'Visitors Management'
    _rec_name = 'visitor_id'

    visitor_name = fields.Char(string="Visitor Name")
    visitor_id = fields.Char(string="Visitor Id")
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    zip_code = fields.Char(string="Area Code")
    state = fields.Char(string="state")
    company_name = fields.Char(string="Company Name")
    phone_no = fields.Char(string="Contact Info")
    mail_id = fields.Char(string="Email Id")
    id_proof = fields.Char(string="ID Proof of Visitors")
    visitor_count = fields.Integer(string="Visits", compute='compute_visitor_count')

    def compute_visitor_count(self):
        visitor_count = self.env['visitor.management'].search_count([('visitor_id', '=', self.visitor_id)])
        self.visitor_count = visitor_count

    # def visitor_view(self):
    #     return {
    #         'res_model' = 'visit.insight',
    #         'type' = 'ir.actions.act_window',
    #         'res_id': self.visitor_id,
    #         'view_mode': 'form',
    #         'target': 'current'
    #     }
