from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    customer_latitude = fields.Float(
        string="Latitude", related="partner_id.partner_latitude"
    )
    customer_longitude = fields.Float(
        string="Longitude", related="partner_id.partner_longitude"
    )
