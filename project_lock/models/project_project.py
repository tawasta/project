from odoo import _, fields, models
from odoo.exceptions import UserError


class ProjectProject(models.Model):

    _inherit = "project.project"

    locked = fields.Boolean(
        string="Locked",
        help="Project is locked."
        + "It can't be edited, and it's tasks cant be edited.",
        copy=False,
    )

    def write(self, vals):
        if "locked" not in vals:
            self.check_locked()

        return super(ProjectProject, self).write(vals)

    def unlink(self):
        self.check_locked()

        return super(ProjectProject, self).unlink()

    def check_locked(self):
        if self.locked:
            # Helper to prevent redundant code and errors
            msg = _("Project '%s' is locked." % self.name)
            msg += "\n"
            msg += _("Please unlock the project before editing.")
            raise UserError(msg)

        return
