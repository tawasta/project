# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models, _

# 4. Imports from Odoo modules:
from openerp.exceptions import Warning

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectExtension(models.Model):
    # 1. Private attributes
    _inherit = 'project.project'
    _order = "priority DESC, sequence DESC, create_date DESC"

    # 2. Fields declaration

    accuracy = fields.Float(
        _("Time left / Overtime"),
        help="Difference between Planned Hours and Time Spent",
        compute='compute_accuracy', translate=True
    )
    real_planned = fields.Float(
        _("Planned Hours"),
        help="Sum of planned hours of all tasks related to this project and its child projects.",
        compute='compute_real_planned', translate=True
    )
    real_effective = fields.Float(
        _("Effective Hours"),
        help="Sum of spent hours of all tasks related to this project and its child projects.",
        compute='compute_real_effective', translate=True
    )
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')
    ],
        'Priority',
        select=True,
        default="1",
    )
    description = fields.Text(_('Description'))

    # 3. Default methods
    @api.model
    def default_get(self, fields):
        res = super(ProjectExtension, self).default_get(fields)
        res['parent_id'] = False
        return res

    # 4. Compute and search fields, in the same order that fields declaration
    @api.one
    def compute_accuracy(self):

        self.accuracy = self.real_planned - self.real_effective

    @api.depends('tasks.planned_hours')
    @api.one
    def compute_real_planned(self):

        planned = 0.0
        tasks = self.env['project.task'].search(
            [('id', 'in', self.tasks.ids)],
            order='write_date DESC')

        for task in tasks:
            planned += task.planned_hours
        self.real_planned = planned

    @api.depends('tasks.effective_hours')
    @api.one
    def compute_real_effective(self):

        effective = 0.0
        tasks = self.env['project.task'].search(
            [('id', 'in', self.tasks.ids)],
            order='write_date DESC'
        )
        for task in tasks:
            effective += task.effective_hours
        self.real_effective = effective

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def set_done(self):

        if not self.validate_project():
            return False

        else:
            return super(ProjectExtension, self).set_done()

    # 8. Business methods
    def validate_project(self):
        result = False
        msg = False

        unclosed_tasks = self.env['project.task'].search_count(
            [('id', 'in', self.tasks.ids), ('stage_id.fold', '=', False)]
        )

        if unclosed_tasks:
            msg = _("Project still has unclosed tasks!")

        else:
            result = True

        if msg:
            raise Warning(msg)

        return result


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # Default methods declared before fields, so using lambdas ins't needed.
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

    date_start = fields.Datetime(default=_get_default_date_start)
    date_end = fields.Datetime(default=_get_default_date_end)

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
