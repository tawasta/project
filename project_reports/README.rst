.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============
Project reports
===============

Module that gives dynamic reports of projects

Installation
============

Modules that are required:

* project (https://www.odoo.com/apps/modules/online/project/)
* web_graph_improved (https://www.odoo.com/apps/modules/8.0/web_graph_improved/)
* hr (https://www.odoo.com/apps/modules/online/hr/)

Configuration
=============
\-

Usage
=====
You can use this module in Projects -> Project costs analysis.


Features
========

* Adds a dynamic report for projects
* Makes it easier to observe project costs (both current and estimated)
* Takes project expenses into account, which are declared in hr->expenses
* Employee hourly wage can be determined in hr->employee->personal information->hourly wage, which is used to count project costs. Not yet working as intended (multiple workers on task).

Need fixing
===========

* Hourly wage fields value comes as the sum of hourly wages of users in project
* Average price field isn't needed after hourly wage starts working as inteded. 
* There are two different fields (current_cost and current_cost_overall), overall has the expenses included, other doesn't. One of them could be removed, unless felt necessary to have both fields. 
* Fields current_cost + current_cost_overall and estimated fields are both calculated with avg_price at the moment. When hourly wages is correct, avg_price should be replaced with hourly_wage.

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.

