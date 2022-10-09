from odoo import fields, models


class ProjectTask(models.Model):

    _inherit = "project.task"

    difficulty = fields.Selection(
        [
            ("0", "No estimation"),
            ("1", "Difficult"),
            ("2", "Challenging"),
            ("3", "Moderate"),
            ("4", "Easy"),
        ],
        default="0",
        string="Difficulty",
        help="Task difficulty, i.e. how long it should take.\n"
        "Difficult: A very hard task, will take multiple days or even weeks.\n"
        "Challenging: A time consuming task, will take a few days.\n"
        "Moderate: A regular task, will take some hours.\n"
        "Easy: A quick task, will take less than hour.\n",
    )

    priority = fields.Selection(
        help="How critical this task is.\n"
        "Normal: No estimation.\n"
        "Important: Is essential, but not urgent.\n"
        "High: Needs an urgent solution\n"
        "Very High: Has to be dealt with immediately.\n",
    )

    work_threshold = fields.Integer(
        "Work threshold",
        compute="_compute_work_threshold",
    )

    def _compute_work_threshold(self):
        for record in self:
            record.work_threshold = int(record.priority) * int(record.difficulty)
            print(f"work_threshold: {record.work_threshold}")
