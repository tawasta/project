# -*- coding: utf-8 -*-
from odoo import models, api, fields


class ProjectProject(models.Model):

    _inherit = 'project.project'

    code_generated = fields.Boolean(
        string='Code generated',
        help='Helper for sequence generator',
        default=False,
        readonly=True,
    )

    @api.multi
    def action_sequence_to_name(self):
        self.ensure_one()

        IrSequence = self.env['ir.sequence']
        sequence = IrSequence.next_by_code('project.project')
        self.name = '%s %s' % (sequence, self.name)
        self.code_generated = True

        return {
            "type": "ir.actions.do_nothing",
        }
