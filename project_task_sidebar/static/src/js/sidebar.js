odoo.define('project_task_sidebar.SidebarButton', function (require) {
    "use strict";

    var core = require('web.core');
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');

    var QWeb = core.qweb;
    var _t = core._t;

    var SidebarButton = Widget.extend({
        template: 'systray.ProjectTaskSidebarButton',
        events: {
            'click': '_onButtonClick',
        },

        start: function () {
            this._super.apply(this, arguments);
            this.$sidebar = $(QWeb.render('systray.ProjectTaskSidebar'));
            $('body').append(this.$sidebar);

            var self = this;
            $('body').on('click', '.o_sidebar_close_button', function () {
                self.$sidebar.hide();
            });
        },

        _onButtonClick: function () {
            var self = this;
            rpc.query({
                route: '/project_task_sidebar/tasks',
            }).then(function (result) {
                var content = $('<div/>');

                // Handle project tasks
                var projectTasksDiv = $('<div/>', {class: 'project-tasks'}).appendTo(content);
                projectTasksDiv.append('<h5>Project Tasks</h5>');
                _.each(result.project_tasks, function (project) {
                    var projectDiv = $('<div/>', {
                        class: 'project-div',
                    }).append($('<h6/>', {
                        text: project.name,
                    })).appendTo(projectTasksDiv);

                    var taskList = $('<ul/>', {
                        class: 'list-group',
                    }).appendTo(projectDiv);

                    _.each(project.tasks, function (task) {
                        $('<li/>', {
                            text: task.name,
                            class: 'list-group-item',
                        }).appendTo(taskList);
                    });
                });

                // Handle helpdesk tasks
                var helpdeskTasksDiv = $('<div/>', {class: 'helpdesk-tasks'}).appendTo(content);
                helpdeskTasksDiv.append('<h5>Helpdesk Tasks</h5>');
                var helpdeskTaskList = $('<ul/>', {class: 'list-group'}).appendTo(helpdeskTasksDiv);
                _.each(result.helpdesk_tasks, function (task) {
                    $('<li/>', {
                        text: task.name,
                        class: 'list-group-item',
                    }).appendTo(helpdeskTaskList);
                });

                self.$sidebar.find('.o_sidebar_content').html(content);
                self.$sidebar.toggle();
            });
        },


    });

    SystrayMenu.Items.push(SidebarButton);

    return SidebarButton;
});
