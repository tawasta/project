# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class InstallationChecklistWizard(models.TransientModel):
    _name = "installation.checklist.wizard"
    _description = "Installation Checklist Wizard"

    installation_id = fields.Many2one(
        "software_knowledge_base.installation",
        required=True, readonly=True
    )
    line_ids = fields.One2many(
        "installation.checklist.wizard.line",
        "wizard_id",
        string="Checklist"
    )

    @api.model
    def default_get(self, fields_list):
        vals = super().default_get(fields_list)
        installation = self.env["software_knowledge_base.installation"].browse(
            self.env.context.get("default_installation_id")
        )
        if not installation:
            raise UserError(_("Wizard needs an Installation in context."))
        vals["installation_id"] = installation.id

        # Täytetään rivit asennuksen checklististä
        lines = []
        for item in installation.checklist_item_ids.sorted(key=lambda i: (i.sequence, i.id)):
            lines.append((0, 0, {
                "item_id": item.id,
                "name": item.name,
                "module_id": item.module_id.id,
                "is_mandatory": item.is_mandatory,
                "description": item.description,
                "validation_status": item.validation_status,
                "is_done": item.is_done,
                "done_by": item.done_by.id,
                "done_at": item.done_at,
                "sequence": item.sequence,
            }))
        vals["line_ids"] = lines
        return vals

    def action_apply(self):
        """Kirjoita muutokset takaisin installation.checklist.item -riveille."""
        self.ensure_one()
        for line in self.line_ids:
            if line.item_id.exists() and line.item_id.is_done != line.is_done:
                # write laukaisee sinun item-mallin write-logiikan ja metadatan päivityksen
                line.item_id.write({"is_done": line.is_done})
        # Sulje modali
        return {"type": "ir.actions.act_window_close"}


class InstallationChecklistWizardLine(models.TransientModel):
    _name = "installation.checklist.wizard.line"
    _description = "Installation Checklist Wizard Line"
    _order = "sequence, id"

    wizard_id = fields.Many2one("installation.checklist.wizard", required=True, ondelete="cascade")
    item_id = fields.Many2one("installation.checklist.item", required=True)

    # Näytettävät kentät (kopioidaan/related vain näyttöä varten)
    sequence = fields.Integer(readonly=True)
    name = fields.Char(readonly=True)
    module_id = fields.Many2one("software_knowledge_base.module", readonly=True)
    is_mandatory = fields.Boolean(readonly=True)
    description = fields.Text(readonly=True)
    validation_status = fields.Selection([
        ("pending", "Pending"),
        ("passed", "Passed"),
    ], readonly=True)
    done_by = fields.Many2one("res.users", readonly=True)
    done_at = fields.Datetime(readonly=True)

    # Muokattava kenttä wizarissa
    is_done = fields.Boolean()
