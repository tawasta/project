.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================
Project Task Timesheets Follow Project
======================================

This module keeps task timesheet entries synchronized with the task's project.

By default, Odoo does not update existing timesheet entries when a task is
moved to another project. The task is moved successfully, but historical
timesheet entries remain linked to the original project.

As a consequence, the timesheet entries are still visible on the task itself,
but they are excluded from the destination project's timesheet and project
update views.

This module automatically updates the affected timesheet entries so they
follow the task to the new project. The corresponding analytic account is
updated as well to maintain reporting consistency.


Configuration
=============
No configuration is required.

Usage
=====

#. Open a task.
#. Change the project.
#. Save the task.

The module automatically updates all existing timesheet entries belonging to
the task from the previous project to the new project.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
