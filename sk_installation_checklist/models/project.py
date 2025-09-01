# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ProjectProject(models.Model):
    _inherit = "project.project"

    installation_id = fields.Many2one(
        "software_knowledge_base.installation",
        string="Installation",
        help="Linkitä projektin käyttöönotto suoraan asennukseen ja sen checklistiin."
    )

    def action_open_installation_checklist(self):
        self.ensure_one()
        if not self.installation_id:
            raise UserError(_("No Installation linked to this project."))
        return {
            "type": "ir.actions.act_window",
            "res_model": "installation.checklist.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_installation_id": self.installation_id.id},
        }
