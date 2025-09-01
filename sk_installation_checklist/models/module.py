from odoo import fields, models


class SkbModule(models.Model):
    _inherit = "software_knowledge_base.module"

    checklist_item_template_ids = fields.One2many(
        "installation.checklist.template", "module_id", string="Checklist Templates"
    )
