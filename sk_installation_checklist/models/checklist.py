# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import datetime

class InstallationChecklistTemplate(models.Model):
    _name = "installation.checklist.template"
    _description = "Installation Checklist Template"
    _order = "module_id, sequence, id"

    name = fields.Char(required=True)
    description = fields.Text()
    module_id = fields.Many2one("software_knowledge_base.module", required=True, ondelete="cascade")
    is_mandatory = fields.Boolean(default=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)


class InstallationChecklistItem(models.Model):
    _name = "installation.checklist.item"
    _description = "Installation Checklist Item"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "sequence, id"

    name = fields.Char(required=True, tracking=True)
    description = fields.Text()
    sequence = fields.Integer(default=10)
    installation_id = fields.Many2one(
        "software_knowledge_base.installation", required=True, ondelete="cascade", index=True
    )
    template_id = fields.Many2one("installation.checklist.template", ondelete="set null", index=True)
    module_id = fields.Many2one(related="template_id.module_id", store=True, readonly=True)
    is_mandatory = fields.Boolean(related="template_id.is_mandatory", store=True, readonly=True)
    is_done = fields.Boolean(tracking=True)
    done_by = fields.Many2one("res.users", readonly=True)
    done_at = fields.Datetime(readonly=True)
    validation_status = fields.Selection([
        ("pending", "Pending"),
        ("passed", "Passed"),
    ], default="pending", tracking=True)

    _sql_constraints = [
        ("uniq_item_per_template_installation",
         "unique(installation_id, template_id)",
         "Checklist item for this template already exists on this installation.")
    ]

    @api.model
    def create(self, vals):
        rec = super().create(vals)
        # jos luodessa is_done = True, täytetään kentät
        if vals.get("is_done"):
            rec._set_done_metadata()
        return rec

    def write(self, vals):
        res = super().write(vals)
        # jos joku merkattiin valmiiksi
        if "is_done" in vals and vals["is_done"]:
            for rec in self:
                rec._set_done_metadata()
        return res

    def _set_done_metadata(self):
        """ Päivitä metatiedot kun is_done = True """
        self.write({
            "done_by": self.env.user.id,
            "done_at": fields.Datetime.now(),
            "validation_status": "passed",
        })


