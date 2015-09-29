# -*- coding: utf-8 -*-

from openerp import models, fields, tools

class project_report(models.Model):
	_name = "project.report" 
	_description = "Reports about projects"
	_auto = False
 
	name = fields.Char('Name of project', readonly=True)
	planned_hours = fields.Float('Planned hours', readonly=True)
	effective_hours = fields.Float('Effective hours', readonly=True)
	avg_price = fields.Float('Average price per hour',default=10.5)
	estimated_cost = fields.Float('Estimated cost of project', readonly=True)
	current_cost = fields.Float('Current cost of project', readonly=True)
	#project_state = fields.Char('Projects state', readonly=True)
	project_state = fields.Selection([('open', 'In Progress'),('cancelled', 'Cancelled'),('close', 'Closed')],'Status', readonly=True)

	def _select(self):
		select_str = "SELECT "
		select_str += "min(p.id) as id,"
		select_str += "a.name as name,"
		select_str += "p.planned_hours as planned_hours,"
		select_str += "p.effective_hours as effective_hours,"
		select_str += "avg_price,"
		select_str += "(avg_price*planned_hours) as estimated_cost,"
		select_str += "(avg_price*effective_hours) as current_cost,"
		select_str += "p.state as project_state"	
		
		return select_str

	def _from(self):

		from_str = "project_project p "
		from_str += "JOIN account_analytic_account a "
		from_str += "ON p.analytic_account_id = a.id"
		
		return from_str


	def _group_by(self):

		group_by_str = " GROUP BY "
		group_by_str += "p.id,"
		group_by_str += "a.name,"
		group_by_str += "planned_hours,"
		group_by_str += "effective_hours,"
		group_by_str += "avg_price,"
		group_by_str += "estimated_cost,"
		group_by_str += "current_cost,"
		group_by_str += "project_state"
		return group_by_str

				
	def init(self, cr):
		self._table = 'project_report'
		tools.sql.drop_view_if_exists(cr, self._table)
		cr.execute(""" 
			CREATE or REPLACE VIEW %s as (
				%s
				FROM %s
				%s
				)""" % (self._table, self._select(),
                    	self._from(), self._group_by()))

