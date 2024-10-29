from odoo import fields, models, api
from datetime import timedelta


class Visit_Insight(models.Model):
    _name = 'visit.insight'
    _description = 'Visits'
    _rec_name = 'visitor_name'

    visitor_name = fields.Char(string="Visitor Name", related='visitor_id.visitor_name', store=False)
    visitor_id = fields.Many2one('visitor.management', string="Visitor ID")
    phone_no = fields.Char(string="Contact Number", related='visitor_id.phone_no')
    mail_id = fields.Char(string="Email ID", related='visitor_id.mail_id')
    check_in_datetime = fields.Datetime(string="CheckIn Date")
    check_out_datetime = fields.Datetime(string="CheckOut Date")
    purpose_of_visit = fields.Char(string="Purpose")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancelled', 'Cancelled')], default='draft', string='Status')

    # New field to link with hr.employee
    employee_id = fields.Many2one('hr.employee', string="Meeting With")

    # Related fields to fetch employee details
    meeting_with = fields.Char(string="Employee Name", related='employee_id.name')
    employee_contact = fields.Char(string="Employee Contact", related='employee_id.mobile_phone')
    department = fields.Char(string="Department", related='employee_id.department_id.name')
    mail_id = fields.Char(string="Email ID", related='employee_id.work_email')

    duration = fields.Float(string="Duration (Hours)", compute='_compute_duration')
    property_sr_no = fields.Integer(string="SI")
    property = fields.Char(string="Property")
    property_count = fields.Integer(string="Property Count")
    permission = fields.Selection([
        ('allowed', 'Allowed'),
        ('not_allowed', 'Not Allowed')], default='not_allowed', string='Permission')

    def action_draft(self):
        for rec in self:
            self.check_in_datetime = False
            self.check_out_datetime = False
            self.employee_id = False
            self.meeting_with = False
            self.employee_contact = False
            self.mail_id = False
            self.department = False
            self.property_sr_no = False
            self.property = False
            self.property_count = False
            self.permission = False
            rec.state = 'draft'
            print("state1 :", self.state)

    def action_cancel(self):
        for rec in self:
            self.check_in_datetime = False
            self.check_out_datetime = False
            self.employee_id = False
            self.meeting_with = False
            self.employee_contact = False
            self.mail_id = False
            self.department = False
            self.property_sr_no = False
            self.property = False
            self.property_count = False
            self.permission = False
            rec.state = 'cancelled'
            print("state2 :", self.state)

    @api.depends('check_in_datetime', 'check_out_datetime')
    def _compute_duration(self):
        for record in self:
            print("state5 :", self.state)
            if record.check_in_datetime and record.check_out_datetime:
                duration = record.check_out_datetime - record.check_in_datetime
                record.duration = duration.total_seconds() / 3600  # Convert seconds to hours
            else:
                record.duration = 0.0

    # @api.onchange('check_in_datetime', 'check_out_datetime')
    # def _onchange_datetime(self):
    #     # If at least one of them is empty, the condition evaluates to True and sets the state field of the current record to 'draft'
    #     if not self.check_in_datetime or not self.check_out_datetime:
    #         self.state = 'draft'
    #     else:
    #         self.state = 'confirm'


    @api.onchange('check_in_datetime', 'check_out_datetime')
    def _onchange_datetime(self):
        if self.check_in_datetime and self.check_out_datetime:
            if self.check_out_datetime.date() != self.check_in_datetime.date():
                self.check_out_datetime = False
                self.state = 'draft'
                print("state3 :", self.state)
                return {
                    'warning': {
                        'title': "Invalid Check-Out Date",
                        'message': "Check-out must be on the same day as check-in.",
                    }
                }

            if self.check_out_datetime < self.check_in_datetime + timedelta(hours=1):
                self.check_out_datetime = False
                self.state = 'draft'
                return {
                    'warning': {
                        'title': "Check-Out Too Soon",
                        'message': "Check-out must be at least 1 hour after check-in.",
                    }
                }

        #     # If at least one of them is empty, the condition evaluates to True and sets the state field of the current record to 'draft'
        if not self.check_in_datetime or not self.check_out_datetime:
            self.state = 'draft'
        else:
            self.state = 'confirm'
            print("state4 :", self.state)

