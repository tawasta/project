.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

==================================
Project Task: Single Assignee Only
==================================
* Prevent setting more than one assignee for a task
* Also adds a helper field user_id that can be used when
  e.g. Ninja reports require accessing a m2o field instead
  of a m2m

Configuration
=============
* None needed

Usage
=====
* Do a create/write operation for a task. If there are more than 1 
  assignee, error message is shown

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@futural.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
        :alt: Oy Tawasta OS Technologies Ltd.
        :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
