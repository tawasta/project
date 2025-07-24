from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    # Override priority field to use selection from project_task_add_very_high
    priority = fields.Selection(
        selection=[
            ("0", "Normal"),
            ("1", "High"),
            ("2", "Very High"),
            ("3", "Highest"),
        ],
        compute="_compute_priority",
        store=True,
        readonly=False,
        string="Priority",
        help="Task priority based on SLA and Scope levels. Can be manually overridden.",
    )

    @api.depends("project_task_sla_id.criticality", "project_task_scope_id.level")
    def _compute_priority(self):
        """
        Compute priority based on SLA and Scope matrix:

        Priority Matrix (SLA rows x Scope columns):
                    Scope 1     Scope 2     Scope 3     Scope 4
        SLA 1         3           3           3           3
        SLA 2         3           2           2           1
        SLA 3         2           1           1           0
        SLA 4         1           1           0           0

        Priority values (from project_task_add_very_high):
        0: Normal
        1: High
        2: Very High
        3: Highest
        """
        for task in self:
            # Default to normal priority
            priority = "0"

            if task.project_task_sla_id and task.project_task_scope_id:
                sla_level = int(task.project_task_sla_id.criticality)
                scope_level = int(task.project_task_scope_id.level)

                # Priority matrix implementation
                if sla_level == 1:
                    # SLA 1 (Critical) is always priority 3
                    priority = "3"
                elif sla_level == 2:
                    # SLA 2 varies based on scope
                    if scope_level <= 1:
                        priority = "3"
                    elif scope_level <= 3:
                        priority = "2"
                    else:
                        priority = "1"
                elif sla_level == 3:
                    # SLA 3 varies based on scope
                    if scope_level <= 1:
                        priority = "2"
                    elif scope_level <= 3:
                        priority = "1"
                    else:
                        priority = "0"
                elif sla_level == 4:
                    # SLA 4 varies based on scope
                    if scope_level <= 2:
                        priority = "1"
                    else:
                        priority = "0"

            task.priority = priority
