from odoo import models, fields, api, _


class Project(models.Model):
    _inherit = 'project.project'

    project_template_id = fields.Many2one(comodel_name='project.project', domain="[('is_template', '=', True)]")

    def create_task(self, task):
        vals = {'project_id': self.id,
                'name': task.name,
                'stage_id': task.stage_id.id,
                'user_id': task.user_id.id,
                'description': task.description
                }
        task_id = self.env['project.task'].create(vals).id


    def action_create_project_from_template(self):
        template_id = self.project_template_id
        for task in template_id.task_ids:
            self.create_task(task)
        return {
            'view_mode': 'form',
            'res_model': 'project.project',
            'res_id': self.id,
            'type': 'ir.actions.act_window',
            'context': self._context
        }
