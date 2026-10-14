from odoo import _, api, models
from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _get_default_company(self):
        """The company of the user, as long as it is one of the active companies.

        Otherwise the project would be hidden from the user by the record rules
        right after it is created.
        """
        company = self.env.user.company_id
        return company if company in self.env.companies else self.env.company

    @api.depends(
        "analytic_account_id.company_id", "partner_id.company_id", "is_template"
    )
    def _compute_company_id(self):
        # The core sets the company of the account or the partner. Only a
        # project that would still be left without a company gets the default.
        # A template stays without a company, so it is visible to everyone.
        res = super()._compute_company_id()
        default_company = self._get_default_company()
        for project in self:
            if not project.company_id and not project.is_template:
                project.company_id = default_company
        return res

    @api.model_create_multi
    def create(self, vals_list):
        # A project copied from a template gets the empty company of the template
        # as a value, and a given value is not computed. Dropping the empty value
        # lets the company be computed.
        for vals in vals_list:
            is_template = vals.get(
                "is_template", self.env.context.get("default_is_template")
            )
            if "company_id" in vals and not vals["company_id"] and not is_template:
                del vals["company_id"]
        return super().create(vals_list)

    @api.constrains("company_id", "is_template")
    def _check_company_required(self):
        projects = self.filtered(
            lambda project: not project.company_id and not project.is_template
        )
        if projects:
            raise ValidationError(
                _(
                    "The company is required for a project that is not a "
                    "template: %s",
                    ", ".join(projects.mapped("name")),
                )
            )

    @api.onchange("is_template")
    def _onchange_is_template_company(self):
        if self.is_template:
            self.company_id = False
