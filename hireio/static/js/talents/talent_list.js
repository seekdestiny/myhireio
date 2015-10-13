_.namespace('hio.talents.views', function(ns) {
    'use strict';

    ns.TalentList = hio.base.hio_base_view.extend({
        events: {},

        initialize: function() {
            this.index = 0;
        },

        render: function() {
            var template = _.template($('#tpl_talent_list_wrapper').html());
            this.$el.html(template());
        }
    });
});

