from odoo import models, fields, api

class ConstructionJob(models.Model):
    _name = 'construction.job'
    _description = 'Construction Job Record'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Adds communication logs to the bottom of the form

    name = fields.Char(string='Project Name', required=True, tracking=True)
    project_code = fields.Char(string='Project Code', required=True)
    manager_id = fields.Many2one('res.users', string='Project Manager', default=lambda self: self.env.user)
    
    # Custom pipeline stages
    stage = fields.Selection([
        ('survey', 'Site Survey'),
        ('boq', 'BOQ Generation'),
        ('fabrication', 'Structural Fabrication'),
        ('installation', 'On-Site Installation'),
        ('billing', 'Progress Billing'),
        ('done', 'Completed')
    ], string='Project Stage', default='survey', tracking=True)
    
    notes = fields.Text(string='Internal Notes')
