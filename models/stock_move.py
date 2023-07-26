from odoo import models
from datetime import date


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_new_picking_values(self):
        res = super(StockMove, self)._get_new_picking_values()
        old_origin = res.get('origin')
        res.update({'origin': f'Delivery for {old_origin} from {date.today().strftime("%d %b %Y")}'})
        return res
