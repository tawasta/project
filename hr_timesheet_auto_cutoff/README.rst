.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============================
Timesheet Auto Stop at Cutoff
=============================
This module automatically stops running timesheet entries at a configured
daily cutoff time. The cutoff is calculated per user based on their local
timezone, ensuring correct handling across multiple timezones.

The module also provides optional employee-level overrides for individual
cutoff settings.

Configuration
=============
Global configuration (default values applied at installation):

* ``ts_cutoff.enabled`` → Enable/disable automatic cutoff (default: False)
* ``ts_cutoff.hour`` → Hour of cutoff in local time (default: 18)
* ``ts_cutoff.minute`` → Minute of cutoff in local time (default: 0)
* ``ts_cutoff.block_start_after_cutoff`` → Prevent starting a timer after cutoff (default: False)

Employee-specific overrides:

* Enable override per employee
* Configure custom hour/minute for cutoff

A cron task runs every 5 minutes:

``Timesheet auto-stop at cutoff``  
 → Stops running timers at the cutoff moment by writing a final duration into the entry.


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
