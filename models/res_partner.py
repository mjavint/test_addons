from odoo import fields, models, api, _

MATURITY = [
    ('initial', _('Initial')),
    ('repetable', _('Repetable')),
    ('defined', _('Defined')),
    ('managed', _('Managed')),
    ('optimising', _('Optimising')),
]


class ResPartner(models.Model):
    _inherit = 'res.partner'

    cmm_maturity = fields.Selection(
        string=_('CMM Maturity'),
        selection=MATURITY,
    )
