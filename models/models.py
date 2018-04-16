# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import re


class model_num(models.Model):
    _inherit = 'product.template'

    model_number = fields.Char(string="Model Number",
                               help='According to the format\n')

    @api.constrains('model_number')
    def onchange_number(self):
        model_num = self.model_number
        pattern = re.compile(r'\[[a-zA-Z0-9]*\]-*')
        if model_num == False:
            return None
        if len(pattern.findall(model_num)) == 0:
            raise UserError(' the format to fill in, please:[]-[]-[]-[]...')


