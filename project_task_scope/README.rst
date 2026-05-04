.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
Project Task Scope
===================

This module adds task scope classification support for project tasks in Odoo.  
It allows linking tasks to predefined scope definitions such as difficulty or size.

Each Scope record includes:
- Name
- Level (Easy, Medium, Hard, Undefined)
- Description

The selected scope helps categorize tasks based on their effort or complexity.
Tasks can also be filtered and grouped by scope in the search view.

Configuration
=============
No configuration needed.

Usage
=====
#. Go to Project → Configuration → Scope Definitions
#. Create scope levels with name, level, and description
#. Open or create a task and select a Scope
#. Use search filters:
   - Easy Tasks
   - Hard Tasks
#. Use "Group by Scope" in the search view to analyze workload

Known issues / Roadmap
======================
* No known issues.
* Integration with priority calculation is handled in a separate module.

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
