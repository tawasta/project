.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

======================================================
Project Task Billing / Sale Order Item Change Filter
======================================================
* Adds one-click "Billing/SO Item Changed" filters (Today, Last 2/3/4/5
  Days) to the "All Tasks" search view, to find tasks where the "Billing"
  (``project_task_billing_enabled``) or "Sale Order Item" (``sale_line_id``)
  field was changed recently, based on their chatter tracking history

Configuration
=============
* The filters are only visible to users in the "Billing / Sale Order Item
  Change Filter" group. Add users to this group in Settings > Users &
  Companies > Users.

Usage
=====
* In Project > Tasks > All Tasks, open the Filters dropdown and pick one of
  the "Billing/SO Item Changed: ..." options (Today, Last 2 Days, ... Last
  5 Days) to find tasks where either field was changed within that period,
  by any user. Can be saved as a personal filter via "Save current search"
  without sharing it.

Known issues / Roadmap
======================
* The "Last N Days" filters use a single lower-bound comparison
  (changed-on-or-after), not a strict "was this the only change" check, so
  a task with older unrelated changes to the same fields still matches as
  long as at least one change happened within the period.

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
