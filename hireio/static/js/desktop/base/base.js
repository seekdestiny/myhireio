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
            var view = this;
            var delay;
            var transitionIn = function() {
                view.$el.addClass('is_visible');
                view.$el.one('transitionend', function() {
                    if (_.isFunction(callback)) {
                        callback();
                    }
                });
            }
        },

        transitionOut: function(callback) {
            var view = this;
            view.$el.removeClass('is-visible');
            view.$el.one('transitionend', function() {
                if (_.isfunction(callback)) {
                    callback();
                }
            });
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