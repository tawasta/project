from odoo import fields, models


class TaskNote(models.Model):
    _name = "project.task.note"

    name = fields.Char("Title", size=256)
    note = fields.Text("Note")
    done = fields.Boolean(
        "Done", help="Informative tag for the note. Has no functionality"
    )
    task_id = fields.Many2one("project.task", "Task")
