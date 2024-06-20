.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================
Project Resolution Time
=======================

* Adds Resolution time and Number of responses fields
* Resolution time is calculated when task is moved to a closing stage.
  Calculation is based on the difference between task creation date and 
  latest stage update.
* Numer of responses indicated how many chatter-based email responses 
  to customer it took to resolve the task

Configuration
=============
* Configure all relevant stages (done, settled, rejected etc.) with "Is closing stage" checkbox checked.

Usage
=====
\-

Known issues / Roadmap
======================
* Consider if Number of Responses could be moved to a separate module,
  as it is a standalone functionality

Credits
=======

Contributors
------------

* Kalle Rantalainen <kalle.rantalainen@tawasta.fi>
* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
        :alt: Oy Tawasta OS Technologies Ltd.
        :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
