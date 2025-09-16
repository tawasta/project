.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

==============================
Timesheet: Task Billing flag
==============================
* Adds a stored related field **billing_enabled** to ``account.analytic.line`` (related to ``task_id.billing_enabled``)
* Shows the flag on timesheet list and form views
* Adds search filters for Billable / Non-billable

Configuration
=============
-

Usage
=====
- Open *Timesheets* and review lines: the **Billing** column mirrors the related task's setting.
- Filter timesheet lines using the provided Billable/Non-billable filters.

Known issues / Roadmap
======================
- If custom timesheet views are used, adjust ``inherit_id`` and XPaths accordingly.

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
