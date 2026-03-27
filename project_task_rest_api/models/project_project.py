from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _inherit = "project.project"

    default_rest_api_project = fields.Boolean(
        string="Default REST API project",
        help=(
            "If enabled, this project is used as the default project "
            "in the Project Task REST API when no project_id is given."
        ),
    )

    @api.constrains("default_rest_api_project")
    def _check_unique_default_rest_api_project(self):
        for project in self.filtered("default_rest_api_project"):
            existing = self.search(
                [
                    ("id", "!=", project.id),
                    ("default_rest_api_project", "=", True),
                ],
                limit=1,
            )
            if existing:
                raise ValidationError(
                    _(
                        "Only one project can be marked as the default "
                        "REST API project."
                    )
                )
