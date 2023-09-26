odoo.define('project_task_sidebar.Sidebar', function (require) {
    "use strict";

    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var ajax = require('web.ajax');

    var Sidebar = Widget.extend({
        template: 'my_module.Sidebar',
        events: {
            'click .o_sidebar_toggle': '_toggleSidebar',
            'click .o_sidebar_close_button': '_closeSidebar',
            'click .o_sidebar_close_icon': '_onCloseIconClick',
        },
        willStart: function() {
            var self = this;
            return this._loadTasks().then(function(tasks) {
                self.tasks = tasks;
            });
        },
        _loadTasks: function() {
            return ajax.jsonRpc('/get_tasks', 'call').then(function(data) {
                console.log(data);
                return data;
            });
        },
        _toggleSidebar: function () {
            this.$el.toggleClass('o_open');
        },
        _closeSidebar: function () {
            this.$el.removeClass('o_open');
        },
        /**
         * Handles the clicking of the close icon.
         *
         * @private
         */
        _onCloseIconClick: function (event) {
            var $taskList = $(event.currentTarget).closest('.o_task_list');
            $taskList.animate({width: 'toggle'}, 350); // 350ms animaatio
        },
    });

    SystrayMenu.Items.push(Sidebar);

    return Sidebar;
});
