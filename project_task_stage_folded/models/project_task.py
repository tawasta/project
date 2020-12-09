from odoo import fields
from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    closed = fields.Boolean(string="Closed", related="stage_id.fold")
