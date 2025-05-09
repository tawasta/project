<<<<<<< HEAD
=======
from odoo import models, fields

>>>>>>> 66cf81174fc43d54f1bd640c3fd4dddb94715ec0
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ProjectStage(models.Model):
    _inherit = "project.project.stage"

    is_closed = fields.Boolean(
        string="Is Closed?",
        help="If checked, projects in this stage are considered closed",
    )
