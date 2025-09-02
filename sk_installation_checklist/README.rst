.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================
Installation Checklist (Module-driven)
======================================

This module extends the **Software Knowledge Base** by introducing a
*module-driven installation checklist*. Each installation automatically
receives checklist items based on the selected software modules, ensuring
that all mandatory steps are tracked and completed before going live.

Features
========

- **Checklist templates per module**  
  Define reusable templates (``installation.checklist.template``) with
  name, description, order (sequence), and whether the item is mandatory.

- **Automatic synchronization**  
  Checklist items are created or removed automatically when:
  
  * a new installation is created,  
  * module assignments change, or  
  * the installation type changes.

- **Progress tracking**  
  For each installation, the following KPIs are computed:  

  * ``checklist_total`` – total mandatory items  
  * ``checklist_done`` – completed mandatory items  
  * ``checklist_progress`` – completion percentage  
  * ``checklist_simple_status`` – *Not Started / In Progress / Complete*

- **Done metadata**  
  When an item is marked as done (``is_done``), the system automatically
  records ``done_by``, ``done_at`` and sets ``validation_status = 'passed'``.

- **Wizard for quick updates**  
  A smart button on the installation form opens a wizard where checklist
  items can be quickly updated in bulk.

- **Readiness validation**  
  If an installation is moved to *Ready* while mandatory items are still
  pending, the system posts a warning message listing the missing items.

- **Project integration**  
  Projects can be linked directly to an installation. From the project
  form, users can open the related installation checklist.

Usage
=====

1. Define **Checklist Templates** under each software module.  
2. Create or update an **Installation** and assign modules.  
   The checklist items will be generated automatically.  
3. Track progress and mark items as done directly on the installation form
   or via the wizard.  
4. Link projects to installations for easier onboarding management.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Valtteri Lattu <Valtteri.Lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
