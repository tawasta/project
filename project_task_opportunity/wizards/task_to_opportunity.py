from odoo import _, api, fields, models
from odoo.tools import html2plaintext


class TaskToOpportunity(models.TransientModel):

    _name = "task.to.opportunity"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True,
        help="Related partner to this opportunity",
    )
    name = fields.Char(string="Name", required=True, help="Opportunity's name")
    description = fields.Text(
        string="Description", help="Opportunity's description in plain text"
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesperson",
    )

    @api.model
    def default_get(self, fields):
        """
        Get default values for fields when
        creating a new opportunity from a task
        """
        res = super().default_get(fields)

        active_id = self._context["active_id"]
        task = self.env["project.task"].browse([active_id])
        name = (
            "%s - %s" % (task.partner_id.name, task.name)
            if task.partner_id
            else task.name
        )

        description = html2plaintext(task.description)
        res.update(
            {
                "name": name,
                "description": description,
                "partner_id": task.partner_id.id,
                "user_id": self._uid,
            }
        )
        return res

    def create_opportunity(self):
        """
        Action method for creating an opportunity
        from a task
        """
        self.ensure_one()
        context = self._context

        values = {
            "partner_id": self.partner_id.id,
            "name": self.name,
            "description": self.description,
            "user_id": self.user_id.id,
            "type": "opportunity",
        }
        opportunity = self.env["crm.lead"].create(values)

        if "active_id" in context:
            active_id = context["active_id"]
            task = self.env["project.task"].browse([active_id])
            opportunity.task_id = task
        # Select opportunity form as the view
        view_id = self.env.ref("crm.crm_lead_view_form").id
        return {
            "name": _("Opportunity created"),
            "view_type": "form",
            "view_mode": "form",
            "view_id": view_id,
            "res_model": "crm.lead",
            "target": "current",
            "res_id": opportunity.id,
            "type": "ir.actions.act_window",
        }
