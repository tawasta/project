.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================
Project Task SLA
==================

This module adds SLA (Service Level Agreement) support for project tasks in Odoo.  
It allows linking tasks to predefined SLA levels and calculating whether the SLA was met.

Each SLA record includes a criticality level (1-4), a response time in hours, and a description.  
Tasks display whether SLA was met and by how many hours over/under the expected time.

Configuration
=============
No configuration needed.

Usage
=====
#. Go to Project → Task SLA
#. Create SLA levels with criticality and response time
#. When creating tasks, select SLA level
#. The task will show whether the SLA was met and the difference in hours

Known issues / Roadmap
======================
* Reporting based on SLA is planned for a future version

Credits
=======

Contributors
------------

* Patrik Torn <patrik.torn@outlook.com>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
