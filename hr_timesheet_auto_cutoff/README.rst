.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============================
Timesheet Auto Stop at Cutoff
=============================

This module automatically stops running timesheet entries based on a daily
cutoff time configured on the resource calendar.

Cutoff is calculated per user using their timezone. If the user has an
associated employee record, the employee’s resource calendar will be used.

Employee-specific overrides remain available when calendar configuration
needs to be refined per individual.


Features
========

* Automatically stops active timesheet timers after cutoff time
* Cutoff defined in *Resource Calendar*:
  * Enabled/disabled flag
  * Hour (0–23)
  * Minute (0–59)
  * Option to prevent starting timers after cutoff
* Optional employee-level override settings
* Handles users in different timezones correctly
* Cron job runs every 5 minutes to enforce cutoff


Configuration
=============

In **Settings → Technical → Resource Calendars**:

* ``Enable timesheet cutoff`` → Toggle automatic cutoff
* ``Cutoff hour`` → Time of day cutoff starts (local to calendar timezone)
* ``Cutoff minute`` → Minute of cutoff hour
* ``Block starting a timer after cutoff`` → Prevent new timers after cutoff

Per-employee override settings are available in **Employee form**:

* ``Override global cutoff`` → Enable override
* Custom cutoff hour/minute and blocking rules


Cron Job
========

A scheduled action enforces cutoff:

``Timesheet auto-stop at cutoff``  
→ Runs every 5 minutes, updating running timesheets that crossed cutoff time.


Known issues / Roadmap
======================

* —


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

This module is maintained by **Futural Oy**.
