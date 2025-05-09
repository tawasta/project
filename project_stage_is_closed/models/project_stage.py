from odoo import models, fields

import logging

_logger = logging.getLogger(__name__)


class ProjectStage(models.Model):
    _inherit = "project.project.stage"

    is_closed = fields.Boolean(
        string="Is Closed?",
        help="If checked, projects in this stage are considered closed",
    )
