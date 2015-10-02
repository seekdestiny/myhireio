_.namespace('hio.widgets', function(ns) {
    "use strict";

    ns.Modal = Backbone.View.extend({
        initialize: function() {

        },

        render: function(options) {
            var template = _.template($('tpl_modal'.html()));
            this.$el.html(template());
        }
    });
});

