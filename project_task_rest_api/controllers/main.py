from odoo.addons.base_rest.controllers import main


class ProjectTaskApiController(main.RestController):
    _root_path = "/project_task_rest_api/"
    _collection_name = "project.task.rest.services"
    _default_auth = "api_key"