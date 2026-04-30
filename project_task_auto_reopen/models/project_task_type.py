from odoo import fields, models


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    reopen = fields.Boolean(
        string="Re-open Stage",
        help=(
            "When a new incoming email is posted on a closed task, "
            "move the task to this stage."
        ),
    )
