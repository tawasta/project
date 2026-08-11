import logging

from odoo import _, fields, models

_logger = logging.getLogger(__name__)


class ProjectTaskType(models.Model):
    _inherit = "project.task.type"

    task_auto_state = fields.Selection(
        selection=lambda self: self._get_task_states(),
        help="When a task reaches this stage,"
        "its state is updated to the selected value.",
    )

    def _get_task_states(self):
        """Returns selection list for task states."""
        task_states = self.env["project.task"]._fields["state"].selection
        return task_states

    def action_update_task_states(self):
        """Update states of all tasks in stages with auto state defined."""
        self.ensure_one()

        title = _("No Action Taken")
        message = _("No tasks needed state update.")

        if self.task_auto_state:
            tasks = self.env["project.task"].search(
                [("stage_id", "=", self.id), ("state", "!=", self.task_auto_state)]
            )
            if tasks:
                tasks.write({"state": self.task_auto_state})
                codes = tasks.mapped("code")
                title = _("Task States Updated")
                message = _("Task states updated successfully for tasks: %s.", codes)

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": title,
                "message": message,
                "type": "success",
                "sticky": False,
            },
        }
