from odoo import fields, models


class View(models.Model):
    """
    Extends the base "ir.ui.view" model to include a new type of view
    called "Project Task Map".
    """

    _inherit = "ir.ui.view"
    type = fields.Selection(selection_add=[("ProjectTaskMapView", "Project Task Map")])


class IrActionsActWindowView(models.Model):
    """
    Extends the base "ir.actions.act_window.view" model to include
    a new view mode called "Project Task Map".
    """

    _inherit = "ir.actions.act_window.view"
    view_mode = fields.Selection(
        selection_add=[("ProjectTaskMapView", "Project Task Map")],
        ondelete={"ProjectTaskMapView": "cascade"},
    )
