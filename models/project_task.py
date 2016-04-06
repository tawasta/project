# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, _

# 4. Imports from Odoo modules:
from openerp.exceptions import Warning

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectTask(models.Model):
    # 1. Private attributes
    _inherit = 'project.task'

    # 2. Fields declaration

    # 3. Default methods
    @api.model
    def default_get(self, fields):
        res = super(ProjectTask, self).default_get(fields)
        res['planned_hours'] = 0
        return res

    # Default methods declared before fields, so using lambdas isn't needed.
    # Default value to date_start from project
    @api.model
    def _get_default_date_start(self):

        project_id = self._get_default_project_id()
        project = self.env['project.project'].search([('id', '=', project_id)])
        return project.date_start or False

    # Default value to date_end from project
    @api.model
    def _get_default_date_end(self):
        project_id = self._get_default_project_id()
        project = self.env['project.project'].search([('id', '=', project_id)])
        return project.date or False

    # 3.1. Fields declaration
    date_start = fields.Datetime(default=_get_default_date_start)
    date_end = fields.Datetime(default=_get_default_date_end)

    # 5. Constraints and onchanges

    # 6. CRUD methods
    @api.one
    def write(self, vals):

        msgbody = ""
        msgsubject = ""

        if 'description' in vals:
            msgbody = _("Task's description changed.")
            msgsubject = _("Description changed")
        elif self.date_deadline and 'date_deadline' in vals:
            msgbody = _("Task's deadline changed from %s to %s.") % (self.date_deadline, vals['date_deadline'])
            msgsubject = _("Deadline changed")

        # TODO: Fix this, messy solution
        if 'description' in vals or self.date_deadline and 'date_deadline' in vals:
            msg_id = self.message_post(subject=msgsubject, body=msgbody, type="notification")
            self.env['mail.message'].browse(msg_id).write({'subtype_id': 1})

        return super(ProjectTask, self).write(vals)

    # 7. Action methods

    # 8. Business methods
