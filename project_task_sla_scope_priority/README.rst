=================================
Project Task: SLA & Scope Priority
=================================

This module adds automatic priority calculation for project tasks based on their SLA and Scope levels.

Configuration
============

To use this module, you need to:

* Install the module
* Have project_task_sla and project_task_scope modules installed and configured
* Have project_task_add_very_high module installed for extended priority levels

Usage
=====

The module automatically:

* Calculates task priority based on SLA and Scope:

  * SLA 1 (Critical) -> Highest priority (3)
  * SLA 2 (Medium) -> Very High priority (2)
  * SLA 3 (Low) -> High priority (1)
  * SLA 4 (Development) -> Normal priority (0)

* Adjusts priority based on task scope:

  * Tasks with hard/undefined scope (levels 3,4) get reduced priority
  * Priority is reduced by one level but never below normal (0)

* Adds new filters for task search:

  * By SLA priority level (Highest/Very High/High)
  * By task complexity (Easy/Complex)

Contributors
===========

* Patrik Torn <patrik.torn@outlook.com>

Maintainer
=========

.. image:: https://futural.fi/web/image/website/1/logo
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy. 