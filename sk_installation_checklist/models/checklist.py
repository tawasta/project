from markupsafe import Markup, escape

from odoo import _, api, fields, models


class InstallationChecklistTemplate(models.Model):
    _name = "installation.checklist.template"
    _description = "Installation Checklist Template"
    _order = "module_id, sequence, id"

    name = fields.Char(required=True)
    description = fields.Text()
    module_id = fields.Many2one(
        "software_knowledge_base.module", required=True, ondelete="cascade"
    )
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
        "software_knowledge_base.installation",
        required=True,
        ondelete="cascade",
        index=True,
    )
    template_id = fields.Many2one(
        "installation.checklist.template", ondelete="set null", index=True
    )
    module_id = fields.Many2one(
        related="template_id.module_id", store=True, readonly=True
    )
    is_mandatory = fields.Boolean(
        related="template_id.is_mandatory", store=True, readonly=True
    )
    is_done = fields.Boolean(tracking=True)
    done_by = fields.Many2one("res.users", readonly=True)
    done_at = fields.Datetime(readonly=True)
    validation_status = fields.Selection(
        [
            ("pending", "Pending"),
            ("passed", "Passed"),
        ],
        default="pending",
        tracking=True,
    )

    task_id = fields.Many2one(
        "project.task", string="Project Task", readonly=True, copy=False, index=True
    )

    _sql_constraints = [
        (
            "uniq_item_per_template_installation",
            "unique(installation_id, template_id)",
            "Checklist item for this template already exists on this installation.",
        )
    ]

    @api.model
    def create(self, vals):
        rec = super().create(vals)

        if rec.installation_id:
            project = self.env["project.project"].search(
                [("installation_id", "=", rec.installation_id.id)],
                order="id desc",
                limit=1,
            )

            if project:
                module_name = rec.module_id.name if rec.module_id else _("(No module)")

                description_parts = []

                if rec.description:
                    description_parts.append(escape(rec.description))

                description_parts.append(
                    "Installation: %s" % escape(rec.installation_id.display_name)
                )
                if rec.module_id:
                    description_parts.append(
                        "Module: %s" % escape(rec.module_id.display_name)
                    )

                # Muodostetaan kappaleet HTML:llä
                description = "<br/><br/>".join(description_parts)

                task = self.env["project.task"].create(
                    {
                        "name": "[Checklist] %s" % rec.name,
                        "project_id": project.id,
                        "description": description,
                        "installation_id": rec.installation_id.id,
                        "module_ids": [(4, rec.module_id.id)] if rec.module_id else [],
                        "user_ids": [
                            (4, rec.installation_id.technical_responsible_person_id.id)
                        ]
                        if rec.installation_id.technical_responsible_person_id
                        else [],
                    }
                )

                rec.task_id = task.id

                # Chatter-viestiin myös moduulitieto
                item_display = rec.name or ("#%s" % rec.id)
                item_link = Markup(
                    "<a href='#' data-oe-model='installation.checklist.item' "
                    "data-oe-id='%d'>%s</a>"
                ) % (rec.id, escape(item_display))

                task.message_post(
                    body=Markup(
                        _("Linked checklist item: %(item)s<br/>Module: %(module)s")
                        % {
                            "item": item_link,
                            "module": escape(module_name),
                        }
                    ),
                    subtype_xmlid="mail.mt_comment",
                )

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
        """Päivitä metatiedot kun is_done = True"""
        self.write(
            {
                "done_by": self.env.user.id,
                "done_at": fields.Datetime.now(),
                "validation_status": "passed",
            }
        )
