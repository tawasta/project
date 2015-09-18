from openerp import models, fields

class ProjectReport(models.Model):
	_name = 'project.report'
	_inherit = 'project.project'
	_description = 'Project reports'
	_order = "sequence"
	name = fields.Char('Description', required=True)

	