from odoo import models
from odoo import api
from datetime import date


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        vals['origin'] = f'Delivery for {vals["origin"]} from {date.today().strftime("%d %b %Y")}'
        rec = super(StockPicking, self).create(vals)
        return rec

