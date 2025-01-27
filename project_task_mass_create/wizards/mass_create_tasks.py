from odoo import api, fields, models


class MassCreateTasks(models.TransientModel):
    _name = "mass.create.tasks"
    _description = "Mass create tasks"

    project_id = fields.Many2one(
        comodel_name="project.project",
        required=1,
    )

    task_prefix = fields.Char(
        string="Task prefix",
    )

    task_suffix = fields.Char(
        string="Task suffix",
    )

    task_user_id = fields.Many2one(
        comodel_name="res.users",
        string="Task assignee",
    )

    task_description = fields.Html(
        string="Task description",
    )

    task_tag_ids = fields.Many2many(
        comodel_name="project.tags",
        string="Task tags",
    )

    task_date_deadline = fields.Date(
        string="Deadline",
    )

    tasks_string = fields.Text(
        string="Tasks",
        help="Paste a list of tasks here. One per line",
        required=1,
    )
    tasks_todo = fields.Text(
        string="Tasks to be created",
        help="These tasks will be created",
        compute="_compute_tasks_todo",
    )

    @api.onchange("task_prefix", "task_suffix", "tasks_string")
    def _compute_tasks_todo(self):
        self.ensure_one()
        if self.tasks_string:
            tasks = self.tasks_string.splitlines()
            tasks_preview = ""
            for task in tasks:
                task_name = self._get_task_name(task)
                tasks_preview += task_name + "\n"

            self.tasks_todo = tasks_preview

    def default_get(self, fields):
        """
        Get default values for fields when
        mass creating tasks
        """
        res = super().default_get(fields)

        active_id = self._context["active_id"]
        project = self.env["project.project"].browse([active_id])
        res.update(
            {
                "project_id": project.id,
            }
        )
        return res

    def _get_task_name(self, name):
        task_name = "{} {} {}".format(
            self.task_prefix or "", name, self.task_suffix or ""
        )
        task_name.rstrip(" ").lstrip(" ")

        return task_name

    def create_tasks(self):
        self.ensure_one()

        values = {
            "project_id": self.project_id.id,
            "partner_id": self.project_id.partner_id.id,
            "date_deadline": self.task_date_deadline,
            "user_ids": [(4, self.task_user_id.id)] if self.task_user_id else [],
            "description": self.task_description,
            "tag_ids": self.task_tag_ids,
        }

        tasks = self.tasks_string.splitlines()
        for task in tasks:
            values["name"] = self._get_task_name(task)
            self.env["project.task"].create(values)
