# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Installation(models.Model):
    _inherit = "software_knowledge_base.installation"

    checklist_item_ids = fields.One2many(
        "installation.checklist.item", "installation_id", string="Checklist"
    )
    checklist_total = fields.Integer(compute="_compute_progress", store=True)
    checklist_done = fields.Integer(compute="_compute_progress", store=True)
    checklist_progress = fields.Float(
        string="Checklist %", compute="_compute_progress", store=True, group_operator="avg"
    )

    @api.depends("checklist_item_ids.is_done")
    def _compute_progress(self):
        for rec in self:
            total = len(rec.checklist_item_ids.filtered(lambda i: i.is_mandatory))
            done = len(rec.checklist_item_ids.filtered(lambda i: i.is_mandatory and i.is_done))
            rec.checklist_total = total
            rec.checklist_done = done
            rec.checklist_progress = (done * 100.0 / total) if total else 0.0

    def _templates_for_modules(self):
        self.ensure_one()
        Template = self.env["installation.checklist.template"]
        return Template.search([
            ("module_id", "in", self.module_ids.ids),
            ("active", "=", True),
        ])

    def action_sync_checklist(self):
        """Generoi puuttuvat checklist itemit valituista moduuleista ja poistaa vanhat moduulit."""
        for rec in self:
            templates = rec._templates_for_modules()
            existing_by_tmpl = {
                it.template_id.id: it for it in rec.checklist_item_ids if it.template_id
            }

            # Luo puuttuvat checklist itemit
            to_create = []
            for tmpl in templates:
                if tmpl.id in existing_by_tmpl:
                    continue
                to_create.append({
                    "installation_id": rec.id,
                    "template_id": tmpl.id,
                    "name": tmpl.name,
                    "description": tmpl.description,
                    "sequence": tmpl.sequence,
                })
            if to_create:
                self.env["installation.checklist.item"].create(to_create)

            # Poistaa checklist-itemit joiden template ei enää liity mihinkään moduuliin
            active_tmpl_ids = set(templates.ids)
            for item in rec.checklist_item_ids:
                if item.template_id and item.template_id.id not in active_tmpl_ids:
                    item.unlink()

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        rec.action_sync_checklist()
        return rec

    def write(self, vals):
        res = super().write(vals)

        # Synkronoi checklist, jos module_ids tai type muuttui
        if "module_ids" in vals or "type" in vals:
            for rec in self:
                rec.action_sync_checklist()

        # Jos tila -> ready, tarkista puuttuvat
        if "state" in vals:
            for rec in self:
                if vals.get("state") == "ready":
                    missing = rec.checklist_item_ids.filtered(
                        lambda i: i.is_mandatory and not i.is_done
                    )
                    if missing:
                        missing_names = "\n".join(missing.mapped("name"))
                        message = _(
                            "Installation '%s' status changed to *Ready*.\n\n"
                            "However, the following mandatory checklist items are still missing:\n%s\n\n"
                            "Please review these items to ensure full configuration."
                        ) % (rec.name or rec.id, missing_names)
                        rec.message_post(
                            body=message,
                            subtype_id=self.env.ref('mail.mt_comment').id
                        )

        return res



