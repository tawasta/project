import logging

from odoo import _, models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):
    _inherit = "project.task"

    def message_post(self, *args, **kwargs):
        if kwargs.get("message_type") == "email":
            self._reopen()

        return super().message_post(*args, **kwargs)

    def message_post_with_template(self, template_id, **kwargs):
        if kwargs.get("message_type") == "email":
            self._reopen()

        return super().message_post_with_template(template_id, **kwargs)

    def _reopen(self):
        for task in self.filtered(lambda task: task.stage_id.fold):
            reopen_stage = task._get_reopen_stage()
            if not reopen_stage:
                continue

            task.sudo().write({"stage_id": reopen_stage.id})

            task.sudo().message_post(
                body=_("Re-opening task due to a new message."),
                message_type="comment",
                subtype_xmlid="mail.mt_note",
            )

    def _get_reopen_stage(self):
        self.ensure_one()

        stages = self.project_id.type_ids.filtered("reopen")
        if not stages:
            _logger.warning("No reopen stage set for %s", self.project_id.display_name)
            return self.env["project.task.type"]

        if len(stages) > 1:
            _logger.warning(
                "Multiple reopen stages for %s. Using %s.",
                self.project_id.display_name,
                stages[0].display_name,
            )

        return stages[0]