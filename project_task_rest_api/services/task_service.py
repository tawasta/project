# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from odoo.tools import html2plaintext

from odoo.addons.base_rest import restapi
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


def to_date(val):
    if datetime.strptime(val, "%Y-%m-%d"):
        return val
    return None


def to_int(val):
    if val in (None, False, ""):
        return None
    return int(val)


def to_bool(val):
    if val in (True, False):
        return val
    if val is None:
        return False
    if isinstance(val, str):
        return val.strip().lower() in ("1", "true", "yes", "y")
    return bool(val)


class ProjectTaskService(Component):
    _inherit = "base.rest.service"
    _name = "project.task.service"
    _usage = "task"
    _collection = "project.task.rest.services"
    _description = """
        Project Task REST Services
        Access to the services is only allowed to authenticated users.
    """

    @restapi.method(
        [(["/report"], "GET")],
        input_param=restapi.CerberusValidator(schema="_validator_report"),
        output_param=restapi.CerberusValidator(
            schema="_validator_report_response"
        ),
    )
    def report(self, start, end=None, project_id=None, all_projects=False):
        """
        Return support-ticket style export from project tasks.

        Filter:
        - task.write_date >= start
        - task.write_date <= end 23:59:59 if end is given

        Project scope:
        - default: only tasks under project marked as default_rest_api_project
        - override with project_id
        - if all_projects is true, do not filter by project
        """
        _logger.info("Generating project task report")

        domain = [("write_date", ">=", start)]
        if end:
            domain.append(("write_date", "<=", end + " 23:59:59"))

        default_project = self._get_default_rest_api_project()
        effective_project_id = False

        if not all_projects:
            effective_project_id = project_id or (
                default_project.id if default_project else False
            )
            if effective_project_id:
                domain.append(("project_id", "=", effective_project_id))

        tasks = self.env["project.task"].search(
            domain, order="project_id asc, id asc"
        )
        _logger.info("Found %s tasks", len(tasks))

        rows = []
        for task in tasks:
            customer_data = self._get_customer_data(task)
            communication_history = self._get_task_communication_history(task)
            responses = self._get_task_responses(task)

            rows.append(
                {
                    "ticket_id": task.id,
                    "title": task.name or "",
                    "description": self._html_to_text(task.description),
                    "customer_name": customer_data.get("customer_name", ""),
                    "assigned_user": task.user_id.name or "",
                    "status_name": task.stage_id.name or "",
                    "tag_list": self._get_tag_data(task),
                    "commercial_entity_name": customer_data.get(
                        "commercial_entity_name", ""
                    ),
                    "response_count": len(responses),
                    "resolution_days": self._get_resolution_time_days(task),
                    "created_datetime": (
                        task.create_date and task.create_date.isoformat() or ""
                    ),
                    "updated_datetime": (
                        task.write_date and task.write_date.isoformat() or ""
                    ),
                    "contact_name": customer_data.get("contact_name", ""),
                    "customer_id": customer_data.get("customer_id", 0),
                    "country_name": customer_data.get("country_name", ""),
                    "project_info": self._get_project_data(task),
                    "communication_history": communication_history,
                }
            )

        result = {
            "count": len(rows),
            "project_filter": {
                "default_project_id": (
                    default_project.id if default_project else False
                ),
                "effective_project_id": effective_project_id,
                "all_projects": bool(all_projects),
            },
            "rows": rows,
        }
        _logger.info("Project task report generated with %s rows", len(rows))
        return result

    def _validator_report(self):
        return {
            "start": {
                "type": "string",
                "nullable": False,
                "required": True,
                "coerce": to_date,
            },
            "end": {
                "type": "string",
                "nullable": True,
                "required": False,
                "coerce": to_date,
            },
            "project_id": {
                "type": "integer",
                "nullable": True,
                "required": False,
                "coerce": to_int,
            },
            "all_projects": {
                "type": "boolean",
                "nullable": True,
                "required": False,
                "coerce": to_bool,
            },
        }

    def _validator_report_response(self):
        return {
            "count": {
                "type": "integer",
                "required": True,
            },
            "project_filter": {
                "type": "dict",
                "required": True,
                "schema": {
                    "default_project_id": {
                        "type": ["integer", "boolean"],
                        "required": True,
                    },
                    "effective_project_id": {
                        "type": ["integer", "boolean"],
                        "required": True,
                    },
                    "all_projects": {
                        "type": "boolean",
                        "required": True,
                    },
                },
            },
            "rows": {
                "type": "list",
                "required": True,
                "schema": {
                    "type": "dict",
                    "schema": self._validator_report_row(),
                },
            },
        }

    def _validator_report_row(self):
        return {
            "ticket_id": {
                "type": "integer",
                "required": True,
            },
            "title": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "description": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "customer_name": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "assigned_user": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "status_name": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "tag_list": {
                "type": "list",
                "required": True,
                "schema": {
                    "type": "dict",
                    "schema": {
                        "id": {
                            "type": "integer",
                            "required": True,
                        },
                        "name": {
                            "type": "string",
                            "required": True,
                            "nullable": True,
                        },
                    },
                },
            },
            "commercial_entity_name": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "response_count": {
                "type": "integer",
                "required": True,
            },
            "resolution_days": {
                "type": "float",
                "required": True,
            },
            "created_datetime": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "updated_datetime": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "contact_name": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "customer_id": {
                "type": "integer",
                "required": True,
            },
            "country_name": {
                "type": "string",
                "required": True,
                "nullable": True,
            },
            "project_info": {
                "type": "dict",
                "required": True,
                "schema": {
                    "project_id": {
                        "type": "integer",
                        "required": True,
                    },
                    "project_name": {
                        "type": "string",
                        "required": True,
                        "nullable": True,
                    },
                },
            },
            "communication_history": {
                "type": "list",
                "required": True,
                "schema": {
                    "type": "dict",
                    "schema": {
                        "timestamp": {
                            "type": "string",
                            "required": True,
                            "nullable": True,
                        },
                        "author_name": {
                            "type": "string",
                            "required": True,
                            "nullable": True,
                        },
                        "message_body": {
                            "type": "string",
                            "required": True,
                            "nullable": True,
                        },
                        "message_type": {
                            "type": "string",
                            "required": True,
                            "nullable": True,
                        },
                    },
                },
            },
        }

    def _get_default_rest_api_project(self):
        return self.env["project.project"].search(
            [("default_rest_api_project", "=", True)],
            limit=1,
        )

    def _html_to_text(self, value):
        if not value:
            return ""
        return html2plaintext(value).strip()

    def _get_tag_data(self, task):
        return [
            {
                "id": tag.id,
                "name": tag.name or "",
            }
            for tag in task.tag_ids
        ]

    def _get_project_data(self, task):
        return {
            "project_id": task.project_id.id or 0,
            "project_name": task.project_id.name or "",
        }

    def _get_customer_data(self, task):
        partner = task.partner_id
        commercial_partner = (
            partner.commercial_partner_id if partner else self.env["res.partner"]
        )

        return {
            "contact_name": partner.name or "",
            "customer_name": commercial_partner.name or "",
            "customer_id": commercial_partner.id or 0,
            "commercial_entity_name": commercial_partner.name or "",
            "country_name": commercial_partner.country_id.name or "",
        }

    def _get_resolution_time_days(self, task):
        if not task.create_date:
            return 0.0

        end_dt = False

        if "date_end" in task._fields and task.date_end:
            end_dt = task.date_end
        elif task.stage_id and (task.stage_id.is_closed or task.stage_id.fold):
            end_dt = task.write_date or False

        if not end_dt:
            return 0.0

        delta = end_dt - task.create_date
        return round(delta.total_seconds() / 86400.0, 2)

    def _get_task_responses(self, task):
        return [
            row
            for row in self._get_task_messages(task)
            if row["message_type"] in ("email", "comment", "internal_note")
        ]

    def _get_task_messages(self, task):
        messages = (
            self.env["mail.message"]
            .sudo()
            .search(
                [
                    ("model", "=", "project.task"),
                    ("res_id", "=", task.id),
                ],
                order="date asc, id asc",
            )
        )

        rows = []
        for message in messages:
            body = self._html_to_text(message.body)
            subtype_name = message.subtype_id.name or ""
            message_type = self._map_message_type(message)

            if not body and not subtype_name:
                continue

            rows.append(
                {
                    "timestamp": message.date and message.date.isoformat() or "",
                    "author_name": message.author_id.name or "",
                    "message_body": body,
                    "message_type": message_type,
                }
            )
        return rows

    def _map_message_type(self, message):
        if message.message_type == "email":
            return "email"
        if message.subtype_id and getattr(message.subtype_id, "internal", False):
            return "internal_note"
        if message.message_type == "comment":
            return "comment"
        if message.message_type == "notification":
            return "notification"
        return message.message_type or ""

    def _get_task_activities(self, task):
        activities = (
            self.env["mail.activity"]
            .sudo()
            .search(
                [
                    ("res_model", "=", "project.task"),
                    ("res_id", "=", task.id),
                ],
                order="create_date asc, id asc",
            )
        )

        rows = []
        for activity in activities:
            body = self._html_to_text(activity.note) or activity.summary or ""
            rows.append(
                {
                    "timestamp": (
                        activity.create_date
                        and activity.create_date.isoformat()
                        or ""
                    ),
                    "author_name": activity.user_id.name or "",
                    "message_body": body,
                    "message_type": "activity",
                }
            )
        return rows

    def _get_task_communication_history(self, task):
        history = self._get_task_messages(task) + self._get_task_activities(task)
        history.sort(key=lambda item: item.get("timestamp") or "")
        return history