from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import SUPERUSER_ID

class Project(osv.Model):
    
    _inherit = 'project.project'
    
    ''' When the module is installed, fetch all projects without a number and assign them one '''
    def _init_project_numbers(self, cr, uid, ids=None, context=None):

        search_filter = [('project_number','=',False)]
        
        matches = self.search(cr, SUPERUSER_ID, args=search_filter,order='id')
        
        settings_model = self.pool.get('project.settings')
        
        project_number = settings_model.browse(cr, SUPERUSER_ID, [1], context)[0].next_number
        for match in self.browse(cr, SUPERUSER_ID, matches, context):
            self.write(cr, SUPERUSER_ID, [match.id], {'project_number': project_number }, context)
            project_number += 1

        ''' Update the highest number in the settings '''
        settings_model.write(cr, SUPERUSER_ID, [1], {'next_number': project_number }, context)
        
        return True 

    ''' When a project is created, assign it a new project number '''
    def create(self, cr, uid, vals, context=None):
        
        if not context:
            context = {}
        
        res = super(Project, self).create(cr, uid, vals, context)
        if self.browse(cr, uid, [res], context)[0]:
            write_vals = {'project_number': self._get_project_number(cr,uid) }
            super(Project, self).write(cr, uid, [res], write_vals, context)
        return res
    
    def _get_project_number(self, cr, uid, context=None):
        settings_model  = self.pool.get('project.settings')   
        
        project_number = settings_model.browse(cr, SUPERUSER_ID, [1])[0].next_number
        
        ''' Bump number in settings by one '''
        settings_model.write(cr, SUPERUSER_ID, [1], {'next_number': project_number+1 })
        
        return project_number
    
    def copy(self, cr, uid, id, default=None, context=None):
        write_vals = {'project_number': self._get_project_number(cr,uid) }
        
        return super(Project, self).copy(cr, uid, id, write_vals, context=context)
    
    _columns = {
        'project_number': fields.char('Project number'),
    }
    
    _sql_constraints = [
        ('project_number', 'unique(project_number)', _('This project number is already in use.'))
    ]