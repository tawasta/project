.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

=================================
Project Task Stage Ensure Partner
=================================
This module prevents project tasks from being moved to another stage unless a
customer is set on the task.

The validation is applied when the task stage is changed, regardless of whether
the change is made from the form view, kanban view, RPC, imports, or automated
actions.

Configuration
=============
No configuration is required.

Usage
=====
1. Go to **Project → Tasks**
2. Open or create a task without a customer
3. Try to move the task to another stage

The operation is blocked with the following validation error:

``Can not move task to the next stage without a customer.``

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Miika Nissi <miika.nissi@futural.fi>
* Kalle Rantalainen <kalle.rantalainen@futural.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
        :alt: Futural Oy
        :target: https://futural.fi/

This module is maintained by Futural Oy.
