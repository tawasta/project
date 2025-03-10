from odoo import models, _
from odoo.exceptions import ValidationError


class Task(models.Model):
    _inherit = "project.task"

    def create(self, vals):
        res = super().create(vals)

        for record in self:
            if len(record.user_ids) > 1:
                raise ValidationError(
                    _("Setting more than one assignee is not allowed.")
                )

        return res

    def write(self, vals):
        res = super().write(vals)

        for record in self:
            if len(record.user_ids) > 1:
                raise ValidationError(
                    _("Setting more than one assignee is not allowed.")
                )

        return res
