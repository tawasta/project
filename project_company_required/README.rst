.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================
Project: Company required
=========================

* A project must have a company. The company is taken from the company of the
  user by default, also for the projects created from a project template.
* Project templates stay without a company, so every user can see them and
  create projects from them.

Configuration
=============
\-

Usage
=====
* New projects get the company of the user as the default company, unless the
  company of the customer or the analytic account sets it. The company of the
  user is used only if it is one of the active companies, otherwise the current
  company is used. The company can be changed to another company of the user.
* A project that is not a template can't be saved without a company. Existing
  projects without a company are not changed, but the company is required when
  their company is edited.
* When "Is Template?" is checked, the company is cleared and not required.

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
