# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    allow_task_notes_copy = fields.Boolean(
        string="Allow copying task notes values to the new project",
        config_parameter="project_task_note.allow_task_notes_copy",
    )
