# -*- coding: utf-8 -*-

from openerp import models, fields, tools

class project_report(models.Model):
	_name = "project.report"
	_inherit = "report.project.task.user"


	avg_price = fields.Float("Average price",default=10.5)

	_order = 'name desc, project_id'

	def init(self, cr):
		tools.sql.drop_view_if_exists(cr, 'report_project_task_user')
		cr.execute("""
			CREATE view report_project_task_user as
			SELECT
			(select 1 ) AS nbr,
			t.id as id,
			t.date_start as date_start,
			t.date_end as date_end,
			t.date_last_stage_update as date_last_stage_update,
			t.date_deadline as date_deadline,
			abs((extract('epoch' from (t.write_date-t.date_start)))/(3600*24))  as no_of_days,
			t.user_id,
			t.reviewer_id,
			t.progress as progress,
			t.project_id,
			t.effective_hours as hours_effective,
			t.priority,
			t.name as name,
			t.company_id,
			t.partner_id,
			t.stage_id as stage_id,
			t.kanban_state as state,
			t.remaining_hours as remaining_hours,
			t.total_hours as total_hours,
			delay_hours as hours_delay,
			t.planned_hours as hours_planned,
			(extract('epoch' from (t.write_date-t.create_date)))/(3600*24)  as closing_days,
			(extract('epoch' from (t.date_start-t.create_date)))/(3600*24)  as opening_days,
			(extract('epoch' from (t.date_deadline-(now() at time zone 'UTC'))))/(3600*24)  as delay_endings_days,
			p.avg_price as avg_price
			FROM project_task t 
			JOIN project_project p
			ON p.id = t.project_id
			WHERE t.active = 'true'
			GROUP BY
			t.id,
			remaining_hours,
			t.effective_hours,
			progress,
			t.total_hours,
			t.planned_hours,
			hours_delay,
			t.create_date,
			t.write_date,
			t.date_start,
			t.date_end,
			t.date_deadline,
			t.date_last_stage_update,
			t.user_id,
			t.reviewer_id,
			t.project_id,
			t.priority,
			name,
			t.company_id,
			t.partner_id,
			stage_id,
			avg_price
			""")
