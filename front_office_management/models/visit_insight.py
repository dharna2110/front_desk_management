from odoo import fields, models

class Visit_Insight(models.Model):
    _name = 'visit.insight'
    _description = 'Visits'
    _rec_name = 'visitor_name'

    visitor_name = fields.Char(string="Visitor Name", related='visitor_id.visitor_name')
    visitor_id = fields.Many2one('visitor.management',string="Visitor ID")
    phone_no = fields.Char(string="Contact Number", related='visitor_id.phone_no')
    mail_id = fields.Char(string="Email ID", related='visitor_id.mail_id')
    check_in_datetime = fields.Datetime(string="CheckIn Date")
    check_out_datetime = fields.Datetime(string="CheckOut Date")
    meeting_with = fields.Char(string="Employee Name")
    department = fields.Char(string="Department")
    purpose_of_visit = fields.Char(string="Purpose")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancelled', 'Cancelled')], default='draft', string='Status')


