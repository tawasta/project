.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

==============================================
Sale/Project: Create sale order line from task
==============================================

* Adds the possibility to create a new Sale Order Line
  from task view, to supplement the core functionality of
  simply selecting an existing SO Line


Configuration
=============
* Set the default product to be suggested in Project Settings
* Note: for task / SO line linkages to be made, the same restrictions
  apply as in core, i.e. the project needs to be billable, the 
  partner of the task needs to match the commercial partner of the 
  SO, and the sale order bust be in state "Sale".

Usage
=====
* Click the 'Create New Sale Order Line' button in task form view header
* Select the Sale Order for which the line will be added, and select the 
  product that will be used on the line. If you do not select an existing
  SO, a new one will be created.

Known issues / Roadmap
======================
* Functionality of project_task_code is used for naming the SO line, 
  so the module is currently a dependency.

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
        :alt: Futural Oy
        :target: https://futural.fi/

This module is maintained by Futural Oy
