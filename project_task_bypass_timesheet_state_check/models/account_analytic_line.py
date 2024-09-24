import logging

from odoo import models

_logger = logging.getLogger(__name__)


class AccountAnalyticLine(models.Model):

    _inherit = "account.analytic.line"

    def _get_sheet_domain(self):

        self.ensure_one()
        res = super()._get_sheet_domain()

        # Remove the state criteria if specifically requested
        if self._context.get("without_state_condition"):
            res.remove(("state", "in", ["new", "draft"]))

        return res
