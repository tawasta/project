# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:

class AccountAnalyticLine(models.Model):
    # 1. Private attributes
    _inherit = 'account.analytic.line'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods
    def _set_remaining_hours_create(self, cr, uid, vals, context=None):
        if not vals.get('task_id'):
            return
        hours = vals.get('unit_amount', 0.0)
        # We can not do a write else we will have a recursion error
        cr.execute(
            'UPDATE project_task '
            'SET remaining_hours=remaining_hours - %s '
            'WHERE id=%s', (hours, vals['task_id']))
        self.pool.get('project.task').invalidate_cache(cr, uid, ['remaining_hours'], [vals['task_id']], context=context)
        self._trigger_projects(cr, uid, [vals['task_id']], context=context)
        return vals

    def _set_remaining_hours_write(self, cr, uid, ids, vals, context=None):
        if isinstance(ids, (int, long)):
            ids = [ids]
        for line in self.browse(cr, uid, ids):
            # in OpenERP if we set a value to nil vals become False
            old_task_id = line.task_id and line.task_id.id or None
            # if no task_id in vals we assume it is equal to old
            new_task_id = vals.get('task_id', old_task_id)
            # we look if value has changed
            if (new_task_id != old_task_id) and old_task_id:
                self._set_remaining_hours_unlink(cr, uid, [line.id], context)
                if new_task_id:
                    data = {'task_id': new_task_id,
                            'to_invoice': vals.get('to_invoice',
                                                   line.to_invoice.id),
                            'unit_amount': vals.get('unit_amount',
                                                    line.unit_amount)}
                    self._set_remaining_hours_create(cr, uid, data, context)
                    self._trigger_projects(
                        cr, uid, list(set([old_task_id, new_task_id])),
                        context=context)
                return ids
            if new_task_id:
                hours = vals.get('unit_amount', line.unit_amount)
                old_hours = line.unit_amount if old_task_id else 0.0
                # We can not do a write else we will have a recursion error
                cr.execute(
                    'UPDATE project_task '
                    'SET remaining_hours=remaining_hours - %s + (%s) '
                    'WHERE id=%s', (hours, old_hours, new_task_id))
                self.pool.get('project.task').invalidate_cache(cr, uid, ['remaining_hours'], [line.task_id.id], context=context)
                self._trigger_projects(cr, uid, [new_task_id], context=context)
        return ids
    # 7. Action methods

    # 8. Business methods
