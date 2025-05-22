import logging

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class Task(models.Model):
    _inherit = "project.task"

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Assignee",
        store=True,
        compute="_compute_user_id",
        copy=False,
        help="Single assignee of the task, computed from the 'Assignees' field.",
    )

    @api.depends("user_ids")
    def _compute_user_id(self):
        """
        Helper field for populating a m2o field with the only one
        assignee, to be used with e.g. Ninja reports
        """
        for record in self:
            if record.user_ids:
                record.user_id = record.user_ids[0]
            else:
                record.user_id = False

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
