# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import fields, models, tools

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:

class TaskReport(models.Model):
    
    # 1. Private attributes
    _inherit = 'report.project.task.user'

    # 2. Fields declaration
    task_type = fields.Many2one(
        "task.type",
        string="Task Type",
        help="Defines task's type."
    )
    hour_type = fields.Selection([
        ('fixed', 'Fixed'), 
        ('time_based', 'Time-Based'), 
        ('product_development', 'Product Development'),
        ('internal', 'Internal'),
        ('support', 'Support')], 
        string="Hour Type", 
        help="Defines hour type for task."
    ) 
    skills = fields.Many2one(
        "hr.skill",
        string="Required skills",
        help="Defines required skills for task."
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    def _select(self):

        select_str = "SELECT "
        select_str += "(select 1 ) AS nbr,"
        select_str += "t.id as id,"
        select_str += "t.date_start as date_start,"
        select_str += "t.date_end as date_end,"
        select_str += "t.date_last_stage_update as date_last_stage_update,"
        select_str += "t.date_deadline as date_deadline,"
        select_str += "abs((extract('epoch' from (t.write_date-t.date_start)))/(3600*24))  as no_of_days,"
        select_str += "t.user_id,"
        select_str += "t.reviewer_id,"
        select_str += "progress as progress,"
        select_str += "t.project_id,"
        select_str += "t.effective_hours as hours_effective,"
        select_str += "t.priority,"
        select_str += "t.name as name,"
        select_str += "t.company_id,"
        select_str += "t.partner_id,"
        select_str += "t.stage_id as stage_id,"
        select_str += "t.kanban_state as state,"
        select_str += "remaining_hours as remaining_hours,"
        select_str += "total_hours as total_hours,"
        select_str += "t.delay_hours as hours_delay,"
        select_str += "planned_hours as hours_planned,"
        select_str += "(extract('epoch' from (t.write_date-t.create_date)))/(3600*24)  as closing_days,"
        select_str += "(extract('epoch' from (t.date_start-t.create_date)))/(3600*24)  as opening_days,"
        select_str += "(extract('epoch' from (t.date_deadline-(now() at time zone 'UTC'))))/(3600*24)  as delay_endings_days,"
        select_str += "t.task_type as task_type,"
        select_str += "t.hour_type as hour_type,"
        select_str += "t.skills as skills"

        return select_str

    def _from(self):

        from_str = "project_task t "

        return from_str

    def _where(self):

        where_str = "t.active = 'true' "

        return where_str

    def _group_by(self):

        group_by_str = "t.id,"
        group_by_str += "remaining_hours,"
        group_by_str += "t.effective_hours,"
        group_by_str += "progress,"
        group_by_str += "total_hours,"
        group_by_str += "planned_hours,"
        group_by_str += "t.delay_hours,"
        group_by_str += "t.create_date,"
        group_by_str += "t.write_date,"
        group_by_str += "t.date_start,"
        group_by_str += "t.date_end,"
        group_by_str += "t.date_deadline,"
        group_by_str += "t.date_last_stage_update,"
        group_by_str += "t.user_id,"
        group_by_str += "t.reviewer_id,"
        group_by_str += "t.project_id,"
        group_by_str += "t.priority,"
        group_by_str += "t.name,"
        group_by_str += "t.company_id,"
        group_by_str += "t.partner_id,"
        group_by_str += "t.stage_id,"
        group_by_str += "t.task_type,"
        group_by_str += "t.hour_type,"
        group_by_str += "t.skills"

        return group_by_str

    def init(self, cr):
        self._table = 'report_project_task_user'
        tools.sql.drop_view_if_exists(cr, self._table)
        cr.execute(""" 
            CREATE or REPLACE VIEW %s as (
                %s
                FROM %s
                WHERE %s
                GROUP BY %s
                )""" % (self._table, self._select(),
                        self._from(), self._where(), self._group_by()))
    # 7. Action methods

    # 8. Business methods
    