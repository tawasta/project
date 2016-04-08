# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import fields, models, tools
from openerp import _
# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ProjectReport(models.Model):

	# 1. Private attributes
	_name = "project.report" 
	_description = "Reports about projects"
	_auto = False
 	
 	# 2. Fields declaration
	name = fields.Char(_('Name of project'), readonly=True)
	planned_hours = fields.Float(_('Planned hours'), readonly=True)
	effective_hours = fields.Float(_('Effective hours'), readonly=True)
	avg_price = fields.Float(_('Average price per hour'), default=0.0)
	estimated_cost = fields.Float(_('Estimated cost of project'), readonly=True)
	current_cost = fields.Float(_('Current cost of project'), readonly=True)
	project_state = fields.Selection([('open', 'In Progress'),('cancelled', 'Cancelled'),('close', 'Closed')],_('Status'), readonly=True)
	expenses = fields.Float(_('Expenses'), default=0.0,readonly=True)
	tasks = fields.Integer(_('Tasks'), readonly=True)
	current_cost_overall = fields.Float(_('Overall current cost'), readonly=True)
	estimated_cost_overall = fields.Float(_('Overall estimated cost'), readonly=True)
	# hourly_wage = fields.Float('Hourly wage')
	# user_cost = fields.Float('Costs from employy hourly wage', readonly=True)

	# 3. Default methods
	def _select(self):
		select_str = "SELECT "
		select_str += "min(p.id) as id,"
		select_str += "a.name as name,"
		select_str += "p.planned_hours as planned_hours,"
		select_str += "p.effective_hours as effective_hours,"
		select_str += "avg_price,"
		select_str += "(avg_price*p.planned_hours) as estimated_cost,"
		select_str += "(avg_price*p.effective_hours) as current_cost,"
		select_str += "p.state as project_state,"
		select_str += "COALESCE(h.unit_amount*h.unit_quantity,0) as expenses,"		
		select_str += "(avg_price*p.effective_hours + COALESCE (h.unit_amount*h.unit_quantity,0)) as current_cost_overall,"
		select_str += "(avg_price*p.planned_hours + COALESCE (h.unit_amount*h.unit_quantity,0)) as estimated_cost_overall,"
		select_str += "count(t.project_id) as tasks"
		# select_str += "COALESCE(hourly_wage,avg_price) as hourly_wage"
		# select_str += "sum(w.hours*hourly_wage) as user_cost"

		return select_str

	def _from(self):

		from_str = "project_project p "
		from_str += "LEFT JOIN account_analytic_account a "
		from_str += "ON p.analytic_account_id = a.id "
		from_str += "LEFT JOIN hr_expense_line h "
		from_str += "ON a.id = h.analytic_account "
		from_str += "LEFT JOIN project_task t "
		from_str += "ON p.id = t.project_id "
		from_str += "LEFT JOIN hr_employee e "
		from_str += "ON t.write_uid = e.id " 
		from_str += "LEFT JOIN project_task_work w "
		from_str += "ON t.id = w.task_id"

		return from_str


	def _group_by(self):

		group_by_str = "p.id,"
		group_by_str += "a.name,"
		group_by_str += "p.planned_hours,"
		group_by_str += "p.effective_hours,"
		group_by_str += "avg_price,"
		group_by_str += "estimated_cost,"
		group_by_str += "current_cost,"
		group_by_str += "project_state,"
		group_by_str += "h.unit_amount,"
		group_by_str += "h.unit_quantity"
		# group_by_str += "hourly_wage"

		return group_by_str

				
	def init(self, cr):
		self._table = 'project_report'
		tools.sql.drop_view_if_exists(cr, self._table)
		cr.execute(""" 
			CREATE or REPLACE VIEW %s as (
				%s
				FROM %s
				GROUP BY %s
				)""" % (self._table, self._select(),
                    	self._from(), self._group_by()))


	# 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    