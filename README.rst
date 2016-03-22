.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================
Project's tasks feed
====================

This module was written to extend the functionality of project module to keep track what has happened in projects tasks.

Features
--------

* Adds a new tab to project's form view called Project Feed
* Tracks project's tasks' task_works and messages and gathers them to project
* Events are represented in Project Feed-section from newest to oldest
* Project_event_feed-table is cleared every time computed function is called (removing duplicates)
* Feed shows the task, short description, time used, date and creator fields
* In message events, time used is considered zero

Installation
============

Install the module form Settings->Local Modules

Configuration
=============
\-

Usage
=====
You can use the module by going to project's form view and clicking the "Project Feed"-tab

Known issues / Roadmap
======================
\-

Bug Tracker

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

This module is maintained by Oy Tawasta OS Technologies Ltd..
