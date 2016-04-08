.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Project Extension
=================

This module was written to extend the functionality of projects. This module  creates new fields accuracy, real_planned and real_effective that count estimation accuracy between planned and effective hours as accuracy, planned and effective hours despite the fact if the task is in folded state in kanban. This module aswell adds priority-field to projects. In addition to that this module changes float-widgets to time-widgets in projects' and tasks' kanban views. 

Features
--------

* **New fields for planned and effective (if task moves to folded state, hours stay visible)**

* **Estimation accuracy, which calculates subtraction between planned and effective hours**

* **Float_time-widgets to kanban-view**

* **Beginning and end dates to tasks are inherited from project**

* **Open tasks filter**

* **Red color on tree view when estimation accuracy is negative**

* **Group tasks by assignation week**

* **Group projects by start month and end month**

* **Adds a smart button to partner, where you can check partner's projects**

* **New menu items My tasks, My projects and Project templates**

* **Adds partner to project kanban view and tasks kanban view**

* **Adds company to projects form view**

* **Adds default values for project and task

Installation
============

Install the module form Settings->Local Modules

Configuration
=============
\-

Usage
=====
You can get to partner-spesific projects from partner form by pressing projects-button.
Projects have new menuitems for My procects/My tasks/Project Templates.
Kanban views have been modified.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd..
