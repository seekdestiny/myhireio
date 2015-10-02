_.namespace('hio.events.views', function(ns) {
    'use strict';

    ns.EventList = hio.base.hio_base_view.extend({
        events: {},

        initialize: function() {
            this.index = 0;
        },

        render: function() {
            var template = _.template($('#tpl_event_list_wrapper').html());
            this.$el.html(template());
        }
    });
});

