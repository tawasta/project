from odoo import http
from odoo.http import request
import logging

class TaskController(http.Controller):

    @http.route('/get_tasks', type='json', auth='user')
    def get_tasks(self):
        logging.info("===========================================");
        logging.info("===========================================");
        logging.info("===========================================");
        logging.info("===========================================");
        helpdesk_tasks = request.env['project.task'].sudo().search([])
        logging.info(helpdesk_tasks);
        project_tasks = request.env['project.task'].sudo().search([])
        logging.info(project_tasks);
        tasks_data = {
            'helpdesk_tasks': self._prepare_tasks_data(helpdesk_tasks),
            'project_tasks': self._prepare_tasks_data(project_tasks),
        }
        logging.info(tasks_data);
        return tasks_data

    def _prepare_tasks_data(self, tasks):
        tasks_data = []
        for task in tasks:
            logging.info(task.stage_id.name);
            tasks_data.append({
                'id': task.id,
                'name': task.name,
                'deadline': task.date_deadline or "",
                'status': task.stage_id.name,
            })
        return tasks_data
