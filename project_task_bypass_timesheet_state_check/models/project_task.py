import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):

    _inherit = "project.task"

    def write(self, values):

        if self.env.user.has_group("project.group_project_manager"):

            # Bypass the standard state checks for timesheet lines
            res = super(ProjectTask, self.with_context(skip_check_state=True)).write(
                values
            )

            # Recalculate the parent timesheet sheets for each timesheet line.
            # Allow the parent timesheet to already be completed
            for task in self:
                for timesheet in task.timesheet_ids:
                    timesheet.with_context(
                        without_state_condition=True
                    )._compute_sheet()
        else:
            res = super().write(values)

        return res
