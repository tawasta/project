# -*- coding: utf-8 -*-

from openerp import api, fields, models

class HrEmployee(models.Model):

	_inherit = 'hr.employee'

	hourly_wage = fields.Float("Hourly wage", default=10.0)

	