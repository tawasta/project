##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2022- Oy Tawasta OS Technologies Ltd. (https://tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class Task(models.Model):
    # 1. Private attributes
    _inherit = "project.task"

    # 2. Fields declaration
    task_note_ids = fields.One2many(
        "project.task.note", "project_task_id", string="Task Notes"
    )


class ProjectProject(models.Model):
    # 1. Private attributes
    _inherit = "project.project"

    def create_project_from_template(self):
        if " (TEMPLATE)" in self.name:
            new_name = self.name.replace(" (TEMPLATE)", " (COPY)")
        else:
            new_name = self.name + " (COPY)"
        new_project = self.copy(
            default={"name": new_name, "active": True, "alias_name": False}
        )
        if new_project.subtask_project_id != new_project:
            new_project.subtask_project_id = new_project.id

        # SINCE THE END DATE DOESN'T COPY OVER ON TASKS
        # (Even when changed to copy=true), POPULATE END DATES ON THE TASK
        for new_task_record in new_project.task_ids:
            for old_task_record in self.task_ids:
                if new_task_record.name == old_task_record.name:
                    new_task_record.date_end = old_task_record.date_end
                if (
                    self.env["ir.config_parameter"]
                    .sudo()
                    .get_param("project_task_note.allow_task_notes_copy")
                ):
                    for task_note in old_task_record.task_note_ids:
                        task_note.copy(default={"project_task_id": new_task_record.id})

        # OPEN THE NEWLY CREATED PROJECT FORM
        return {
            "view_type": "form",
            "view_mode": "form",
            "res_model": "project.project",
            "target": "current",
            "res_id": new_project.id,
            "type": "ir.actions.act_window",
        }


class ProjectTaskNote(models.Model):
    # 1. Private attributes
    _name = "project.task.note"
    _description = "Project Task Note"

    # 2. Fields declaration
    title = fields.Char(required=True)
    description = fields.Html()
    done = fields.Boolean()
    user_id = fields.Many2one(
        "res.users",
        string="Responsible",
        tracking=True,
        default=lambda self: self.env.user,
    )
    project_task_id = fields.Many2one(
        "project.task",
        string="Project Task",
        required=True,
        readonly=True,
        ondelete="cascade",
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
