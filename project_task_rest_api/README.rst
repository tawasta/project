.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=====================
Project Task REST API
=====================

This module provides a REST API for exporting project task data together
with its communication history.

The implementation is intended for integration use cases where project
tasks are used as support tickets or service cases and selected ticket
data needs to be made available outside Odoo.

The API is built on top of:

* ``base_rest``
* ``base_rest_auth_api_key``
* ``component``

Features
========

The module exposes a report endpoint for project tasks.

Returned ticket data includes:

* Ticket ID
* Title
* Description
* Customer name
* Assigned user
* Status name
* Tags
* Commercial entity name
* Response count
* Resolution time (days)
* Created datetime
* Updated datetime
* Contact name
* Customer ID
* Country name
* Project information
* Full communication history

Communication history includes:

* Mail messages linked to the task
* Activities linked to the task
* Timestamp
* Author name
* Message body
* Message type

Configuration
=============

To configure this module:

#. Install required dependencies:

   * ``project``
   * ``mail``
   * ``base_rest``
   * ``base_rest_auth_api_key``
   * ``component``

#. Create an API key for the integration user.
#. Ensure the integration user has access rights to:

   * project tasks
   * partners
   * mail messages
   * activities

#. Configure the default REST API project:

   * Go to **Project → Projects**
   * Enable the field *"Default REST API project"* on exactly one project

   Only one project can be marked as default. This is enforced by a constraint.

Usage
=====

Base path::

    /project_task_rest_api/

Endpoint::

    GET /project_task_rest_api/task/report

Authentication
--------------

Authentication is handled via API key using ``base_rest_auth_api_key``.

Pass the API key in request headers::

    API-KEY: your_api_key_here

Query parameters
----------------

* ``start`` (required)
  Start date in format ``YYYY-MM-DD``

* ``end`` (optional)
  End date in format ``YYYY-MM-DD``

* ``project_id`` (optional)
  Override default project selection

* ``all_projects`` (optional, boolean)
  If true, disables project filtering entirely

Filtering behavior
------------------

Project filtering works as follows:

* If ``all_projects=true`` → all tasks are returned
* Else if ``project_id`` is provided → that project is used
* Else → project marked with ``default_rest_api_project = True`` is used
* If no default project exists → no project filter is applied

Example requests
----------------

Default project::

    GET /project_task_rest_api/task/report?start=2024-01-01

Specific project::

    GET /project_task_rest_api/task/report?start=2024-01-01&project_id=12

All projects::

    GET /project_task_rest_api/task/report?start=2024-01-01&all_projects=true

Response structure
------------------

The endpoint returns JSON:

::

    {
        "count": 1,
        "project_filter": {
            "default_project_id": 5,
            "effective_project_id": 5,
            "all_projects": false
        },
        "rows": [
            {
                "ticket_id": 123,
                "title": "Example ticket",
                "description": "Description text",
                "customer_name": "Customer Ltd",
                "assigned_user": "John Doe",
                "status_name": "In Progress",
                "tag_list": [
                    {"id": 1, "name": "Support"}
                ],
                "commercial_entity_name": "Customer Ltd",
                "response_count": 3,
                "resolution_days": 1.25,
                "created_datetime": "2024-01-01T10:00:00",
                "updated_datetime": "2024-01-02T12:00:00",
                "contact_name": "Jane Doe",
                "customer_id": 45,
                "country_name": "Finland",
                "project_info": {
                    "project_id": 5,
                    "project_name": "Support"
                },
                "communication_history": [
                    {
                        "timestamp": "2024-01-01T10:05:00",
                        "author_name": "John Doe",
                        "message_body": "Initial message",
                        "message_type": "comment"
                    }
                ]
            }
        ]
    }

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

.. image:: https://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: https://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
