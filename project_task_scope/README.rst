.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
Project Task Scope
===================

This module adds task scope classification support for project tasks in Odoo.  
It allows linking tasks to predefined scope definitions such as difficulty or size.

Each Scope record includes a complexity level (1–4), a name, and a description.  
The selected scope helps in categorizing tasks based on their effort or size.

Configuration
=============
No configuration needed.

Usage
=====
#. Go to Project → Task Scope
#. Create scope levels with name, level, and description
#. When creating tasks, select a Scope
#. Use the scope to organize or analyze task workload

Known issues / Roadmap
======================
* No known issues.
* Integration with priority calculation is handled in a separate module.

Credits
=======

Contributors
------------

* Patrik Torn <patrik.torn@outlook.com>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
