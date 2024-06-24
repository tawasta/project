import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ProjectTask(models.Model):

    _inherit = "project.task"

    number_of_responses = fields.Integer(
        string="Number of Responses",
        compute="_compute_number_of_responses",
        store=True,
        help="The number of messages that have been sent to the customer",
    )

    @api.depends("message_ids")
    def _compute_number_of_responses(self):
        """
        Calculate the number of outbound mail.messages
        """

        mt_comment_subtype_id = self.env.ref("mail.mt_comment")

        for record in self:

            # Subtype is "Discussions" AND either
            # - Message type is Email and the task's partner is in the list of recipients, OR
            # - Message type is Comment
            record.number_of_responses = len(
                record.message_ids.filtered(
                    lambda msg: (
                        msg.subtype_id.id == mt_comment_subtype_id.id
                        and (
                            (
                                msg.message_type == "email"
                                and record.partner_id.id in msg.partner_ids.mapped("id")
                            )
                            or msg.message_type == "comment"
                        )
                    )
                )
            )
