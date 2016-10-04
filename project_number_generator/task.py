from openerp.osv import osv, fields
from openerp.tools.translate import _
from openerp import SUPERUSER_ID

class Task(osv.Model):
    
    _inherit = 'project.task'
    
    ''' When the module is installed, fetch all tasks without a number and assign them one '''
    def _init_task_numbers(self, cr, uid, ids=None, context=None):

        search_filter = [('task_number','=',False)]
        
        matches = self.search(cr, SUPERUSER_ID, args=search_filter,order='id')
        
        settings_model = self.pool.get('project.settings')
        
        task_number = settings_model.browse(cr, SUPERUSER_ID, [1], context)[0].next_task_number
        for match in self.browse(cr, SUPERUSER_ID, matches, context):
            self.write(cr, SUPERUSER_ID, [match.id], {'task_number': task_number }, context)
            task_number += 1

        ''' Update the highest number in the settings '''
        settings_model.write(cr, SUPERUSER_ID, [1], {'next_task_number': task_number }, context)
        
        return True 

    ''' When a task is created, assign it a new task number '''
    def create(self, cr, uid, vals, context=None):
        
        if not context:
            context = {}
        
        res = super(Task, self).create(cr, uid, vals, context)
        if self.browse(cr, uid, [res], context)[0]:
            write_vals = {'task_number': self._get_task_number(cr,uid) }
            super(Task, self).write(cr, uid, [res], write_vals, context)
        return res
    
    def _get_task_number(self, cr, uid, context=None):
        settings_model  = self.pool.get('project.settings')   
        
        task_number = settings_model.browse(cr, SUPERUSER_ID, [1])[0].next_task_number
        
        ''' Bump number in settings by one '''
        settings_model.write(cr, SUPERUSER_ID, [1], {'next_task_number': task_number+1 })
        
        return task_number
    
    def copy(self, cr, uid, id, default=None, context=None):
        write_vals = {'task_number': self._get_task_number(cr,uid) }
        
        return super(Task, self).copy(cr, uid, id, write_vals, context=context)
    
    _columns = {
        'task_number': fields.char('Task number'),
    }
    
    _sql_constraints = [
        ('task_number', 'unique(task_number)', _('This task number is already in use.'))
    ]