.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================
Project Task auto reopen
========================

This module automatically reopens project tasks when a new **incoming email**
is received on a task that is in a *folded (closed)* stage.

In Odoo, folded stages are typically used to represent completed or cancelled
tasks. This module leverages that convention and restores the task back to an
active workflow stage.

Features
========

- Automatically reopens tasks when receiving incoming emails
- Uses stage configuration instead of task state
- Lightweight and fully aligned with Odoo messaging flow
- No override of core state logic

Configuration
=============

1. Go to **Project → Configuration → Stages**
2. Select the stage where tasks should move when reopened
3. Enable:

   - *Re-open Stage*

4. Ensure that your "closed" stages have:

   - *Folded* enabled (this is the trigger condition)

Usage
=====
- Move a task to a folded stage (e.g. Done / Cancelled)
- Send an email to the task

Result:

- Task is automatically moved to the configured *Re-open Stage*
- A log note is posted in the chatter:

  *"Re-opening task due to a new message."*

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Jarmo Kortetjärvi <jarmo.kortetjarvi@futural.fi>
* Valtteri Lattu <valtteri.lattu@futural.fi>
* Timo Kekäläinen <timo.kekalainen@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
