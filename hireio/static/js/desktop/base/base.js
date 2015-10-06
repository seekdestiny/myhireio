_.namespace('hio.base', function(ns) {
    "use strict";

    ns.views = {};

    ns.hio_base_view = Backbone.View.extend({

        initialize: function() {
        },

        render: function(options) {
            return this;
        },

        transitionIn: function(callback) {
            // this is for transition animation
            if (callback) {
                callback();
            }
        },

        transitionOut: function(callback) {
            if (callback) {
                callback();
            }
        }

    });

    ns.hio_app = Backbone.View.extend({
        el: '.hireio_body',

        goto: function(view) {
            var previous = this.currentPage || null;
            var next = view;

            if (previous) {
                previous.transitionOut(function() {
                    previous.remove();
                });
            }

            next.render();
            $('.hireio_body').append(next.$el);
            next.transitionIn();
            this.currentPage = next;
        }
    });
});
