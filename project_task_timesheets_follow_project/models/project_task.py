from odoo import models


class ProjectTask(models.Model):
    _inherit = "project.task"

    def write(self, vals):
        """Synchronize timesheets when moving tasks between projects.

        Odoo does not automatically update existing timesheet entries when a task
        is moved to another project. As a result, historical timesheet lines remain
        linked to the previous project through ``account.analytic.line.project_id``,
        causing them to be excluded from the destination project's timesheet and
        project update views.

        This override updates the affected timesheet entries to reference the new
        project and its analytic account after the task has been moved.
        """

        old_project_by_task = {task.id: task.project_id.id for task in self}

        res = super().write(vals)

        updates = {}

        for task in self:
            old_project_id = old_project_by_task[task.id]
            new_project_id = task.project_id.id

            if old_project_id == new_project_id:
                continue

            analytic_account_id = task.project_id.analytic_account_id.id or False
            updates.setdefault(
                (old_project_id, new_project_id, analytic_account_id), []
            ).append(task.id)

        AnalyticLine = self.env["account.analytic.line"]

        for (old_project_id, new_project_id, analytic_account_id), task_ids in updates.items():
            values = {"project_id": new_project_id}

            if analytic_account_id:
                values["account_id"] = analytic_account_id

            AnalyticLine.search([
                ("task_id", "in", task_ids),
                ("project_id", "=", old_project_id),
            ]).write(values)

        return res