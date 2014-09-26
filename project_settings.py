# -*- coding: utf-8 -*-
from openerp.osv import osv, fields

class project_settings(osv.osv):
    ''' A model for storing the project settings '''
    
    _name = "project.settings"
    _rec_name = 'next_number'
    
    _columns = {
        'next_number': fields.integer('The next project number'),
    }
    