# -*- coding: utf-8 -*-

from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_id = fields.Many2one('res.company', string='Company', index=True,
                                 default=lambda self: self.env.company.id)
    api_token = fields.Char(_("API Token"),
                            config_parameter='test_addons.api_token',
                            related="company_id.api_token",
                            readonly=False)

    @api.model
    def get_values(self):
        res = super().get_values()
        res.update(
            api_token=self.env["ir.config_parameter"].sudo().get_param(
                "api_token"),
        )
        return res

    def set_values(self):
        super().set_values()
        for record in self:
            self.env['ir.config_parameter'].sudo().set_param(
                "api_token", record.api_token)


class ResCompany(models.Model):
    _inherit = "res.company"

    api_token = fields.Char("Token for API services",
                            config_parameter='test_addons.api_token')

