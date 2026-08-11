import logging

from odoo import models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = "project.task"

    def create(self, vals):
        task = super().create(vals)
        task._update_state_based_on_stage()
        return task

    def write(self, vals):
        res = super().write(vals)
        if "stage_id" in vals:
            self._update_state_based_on_stage()
        return res

    def _update_state_based_on_stage(self):
        for task in self:
            stage = task.stage_id
            if stage.task_auto_state and task.state != stage.task_auto_state:
                task.state = stage.task_auto_state
