from odoo import fields, models


class Project(models.Model):

    _inherit = "project.project"

    def action_cron_compute_task_colors(self):
        projects = self.search([("task_autocolor", "=", True)])
        projects.action_compute_task_colors()

    def action_compute_task_colors(self):
        for record in self:
            if record.task_autocolor:
                record.task_ids._compute_task_color()

    task_autocolor = fields.Boolean(
        "Auto-color tasks",
        help="Set automatic colors for tasks, based on rules",
        default=False,
    )

    task_autocolor_color_fresh = fields.Integer(
        "Color for freshly updated tasks", default=10
    )
    task_autocolor_days_fresh = fields.Integer(
        "Max days to consider a task fresh", default=1
    )

    task_autocolor_color_recent = fields.Integer(
        "Color for recently updated tasks", default=3
    )
    task_autocolor_days_recent = fields.Integer(
        "Max days to consider a task recent", default=7
    )

    task_autocolor_color_aged = fields.Integer(string="Color for aged tasks", default=2)
    task_autocolor_days_aged = fields.Integer(
        "Max days to consider a task recent", default=14
    )

    task_autocolor_color_stale = fields.Integer(
        string="Color for stale tasks", default=1
    )
