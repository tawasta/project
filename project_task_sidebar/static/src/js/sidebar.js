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
            'click .o_toggle_list': '_onToggleListClick',
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
        _onToggleListClick: function (event) {
            var $list = $(event.currentTarget).parent().siblings('.o_task_list');
            console.log($list);
            if ($list.is(':visible')) {
                console.log("NAYTA");
                $list.slideUp();
                $(event.currentTarget).find('i').removeClass('fa-chevron-up').addClass('fa-chevron-down');
            } else {
                $list.slideDown();
                console.log("PIILOTA");
                $(event.currentTarget).find('i').removeClass('fa-chevron-down').addClass('fa-chevron-up');
            }
        },
    });

    SystrayMenu.Items.push(Sidebar);

    return Sidebar;
});
