.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
        :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
        :alt: License: AGPL-3

=======================
Project Stage Mail Once
=======================
This module extends the standard stage-based email template behavior of Odoo
Project tasks by ensuring that a stage email template is sent **only once per task**.

By default, Odoo sends the configured email template every time a task enters
a stage. This module prevents repeated sending when a task is moved back to
the same stage later.

Features
========

- Add a per-stage option to send email templates only once
- Prevent duplicate email notifications when tasks re-enter the same stage
- Lightweight implementation fully compatible with Odoo core logic
- No override of mail sending mechanism (uses core ``_track_template`` flow)

Configuration
=============
1. Go to **Project → Configuration → Stages**
2. Open or create a stage
3. Set an **Email Template**
4. Enable:

   - *Send Email Template Only Once*

Usage
=====
- When a task enters a stage with an email template:
  
  - The email is sent normally on the **first entry**
  - The task is marked as "email sent"

- If the task is later moved back to the same stage:
  
  - The email **will not be sent again**

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

This module is maintained by Futural Oy.
