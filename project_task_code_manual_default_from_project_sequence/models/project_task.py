import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = "project.task"

    def _get_default_task_code(self, parent_project):
        # Return e.g. P01234-1
        return "{}-{}".format(
            parent_project.sequence_code or "n/a",
            parent_project.number_next_task or "n/a",
        )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if "project_id" in vals:
                parent_project = self.env["project.project"].search(
                    [("id", "=", vals["project_id"])]
                )

                vals["code"] = self._get_default_task_code(parent_project)

                parent_project.sudo().write(
                    {"number_next_task": parent_project.number_next_task + 1}
                )

        return super().create(vals_list)
