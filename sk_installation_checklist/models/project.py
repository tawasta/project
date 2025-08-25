# -*- coding: utf-8 -*-
from odoo import fields, models

class ProjectProject(models.Model):
    _inherit = "project.project"

    installation_id = fields.Many2one(
        "software_knowledge_base.installation",
        string="Installation",
        help="Linkitä projektin käyttöönotto suoraan asennukseen ja sen checklistiin."
    )
