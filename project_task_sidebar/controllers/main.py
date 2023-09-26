from odoo import http
from odoo.http import request

class ProjectTaskSidebar(http.Controller):

    @http.route('/project_task_sidebar/tasks', type='json', auth='user')
    def get_tasks(self):
        # Fetch project tasks
        projects = request.env['project.project'].search([('id', '=', '1')])
        project_data = []
        for project in projects:
            tasks = request.env['project.task'].search([('project_id', '=', project.id), ('user_id', '=', request.uid)])
            task_data = [{'name': task.name, 'id': task.id} for task in tasks]
            project_data.append({
                'name': project.name,
                'id': project.id,
                'tasks': task_data
            })

        helpdesk_projects = request.env['project.project'].search([('id', '=', '2')])
        helpdesk_data = []
        for hp in helpdesk_projects:
            helpdesk_tasks = request.env['project.task'].search([('project_id', '=', hp.id), ('user_id', '=', request.uid)])
            help_task_data = [{'name': ht.name, 'id': ht.id} for ht in helpdesk_tasks]
            helpdesk_data.append({
                'name': project.name,
                'id': project.id,
                'tasks': help_task_data
            })

        return {
            'project_tasks': project_data,
            'helpdesk_tasks': helpdesk_data,
        }
