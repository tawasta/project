from odoo import models, api


class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    @api.model
    def create(self, vals):
        if self._context.get('default_project_id'):
            self.check_locked(self._context.get('default_project_id'))

        return super(ProjectTaskType, self).create(vals)

    # Allow writing, because same stage may belong to multiple projects

    def unlink(self):
        self.check_locked()

        return super(ProjectTaskType, self).unlink()

    def check_locked(self, project_id=False):
        if project_id:
            project_ids = self.env['project.project'].browse([project_id])
        else:
            project_ids = self.project_ids

        for project_id in project_ids:
            project_id.check_locked()

        return
