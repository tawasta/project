# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models


# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):
    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration
    project_count = fields.Integer(string="Projects", compute='compute_project_count')
    task_count = fields.Integer(string="Tasks", compute='compute_task_count')

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration
    @api.multi
    def compute_project_count(self):

        project_count = 0

        for partner in self:
            child_ids = partner._get_recursive_child_ids(partner)

            for child in child_ids:
                project_count += partner.env['project.project'].search_count([('partner_id', '=', child)])

            project_count += partner.env['project.project'].search_count([('partner_id', '=', partner.id)])
            partner.project_count = project_count

    @api.multi
    def compute_task_count(self):

        task_count = 0

        for partner in self:
            child_ids = partner._get_recursive_child_ids(partner)

            for child in child_ids:
                task_count += partner.env['project.task'].search_count([('partner_id', '=', child)])

            task_count += partner.env['project.task'].search_count([('partner_id', '=', partner.id)])
            partner.task_count = task_count

    @api.multi
    def _get_recursive_child_ids(self, record):
        child_ids = []

        for child in self.search([('parent_id', '=', record.id)]):
            child_ids.append(child.id)

            if self.search([('parent_id', '=', child.id)]):
                child_ids += self._get_recursive_child_ids(child)

        return child_ids

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
