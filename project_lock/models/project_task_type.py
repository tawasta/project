# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    locked = fields.Boolean(
        string='Locked',
        help="Stage is locked." +
             "It can't be edited.",
        default=True,
    )

    @api.model
    def create(self, vals):
        if self._context.get('default_project_id'):
            self.check_locked(self._context.get('default_project_id'))

        return super(ProjectTaskType, self).create(vals)

    @api.multi
    def unlink(self):
        self.check_locked()
        self.check_stage_locked()

        return super(ProjectTaskType, self).unlink()

    # Allow writing if stage is not locked, because same stage may belong to
    # multiple projects
    @api.multi
    def write(self, vals):
        if 'locked' not in vals:
            self.check_stage_locked()

        return super(ProjectTaskType, self).write(vals)

    @api.multi
    @api.onchange('project_ids')
    def lock_stage_if_one_project_is_added(self):
        project_ids_origin = self._origin.project_ids
        project_ids = self.project_ids
        number_of_projects = project_ids and len(project_ids) or 0
        number_of_projects_origin = project_ids_origin and len(project_ids_origin) or 0

        if (number_of_projects_origin + 1 == number_of_projects) and \
                (number_of_projects_origin == 1):
            self.locked = True

    def check_locked(self, project_id=False):
        if project_id:
            project_ids = self.env['project.project'].browse([project_id])
        else:
            project_ids = self.project_ids

        for project_id in project_ids:
            project_id.check_locked()
        return

    def check_stage_locked(self):
        if self.locked:
            msg = _("Stage '%s' is locked.") % self.name
            msg += _("\nEdited changes are not going to be saved without "
                     "unlocking selected stage.")
            msg += _("\nPlease unlock the stage before editing.")

            raise UserError(msg)
        return

    @api.onchange('locked')
    def stage_locked_onchange(self):
        locked = self._origin.locked
        number_of_projects = self.project_ids and len(self.project_ids) or 0
        title = _("Warning for stage: %s") % self.name

        if locked and number_of_projects > 1:
            message = _("Stage is linked to %s projects.") % number_of_projects
            message += _("\nModifying or deleting this stage will affect those "
                         "projects also.")
            warning = {
                'title': title,
                'message': message,
            }
            return {'warning': warning}
