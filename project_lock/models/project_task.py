from odoo import models, api


class ProjectTask(models.Model):

    _inherit = 'project.task'

    @api.model
    def create(self, vals):
        if self._context.get('default_project_id'):
            self.check_locked(self._context.get('default_project_id'))

        return super(ProjectTask, self).create(vals)

    def write(self, vals):
        # Allow modifying followers and project_id
        if not (len(vals) == 1
                and ('message_follower_ids' in vals or 'project_id' in vals)):
            self.check_locked()

        return super(ProjectTask, self).write(vals)

    def unlink(self):
        self.check_locked()

        return super(ProjectTask, self).unlink()

    def check_locked(self, project_id=False):
        for record in self:
            if project_id:
                project = record.env['project.project'].browse([project_id])
            else:
                project = record.project_id

            project.check_locked()

        return
