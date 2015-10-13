_.namespace('hio.events', function(ns) {
    'use strict';

    ns.session = new Backbone.Model();
    ns.session.companies = new Backbone.Model();
    ns.global = ns.global || {};
    ns.global.data = ns.global.data || {};

    ns.bootstrap = function(options) {
        var events_view = {
            Router: null,

            init: function() {
                this.instance = new hio.base.hio_app();
                return this;
            }
        };

        var app = new events_view.init();

        app.Router = Backbone.Router.extend({
            routes: {
                '': 'event_list',
                'event?event_id=:event_id': 'event_detail'
            },

            event_list: function() {
                var view = new ns.views.EventList;
                app.instance.goto(view);
            },

            event_detail: function(talent_id) {
                var view = new ns.views.EventDetail({ event_id: event_id });
                app.instance.goto(view);
            }
        });

        ns.router = new app.Router();
        ns.router.navigate('', {trigger: true});
        Backbone.history.start();
    };
});

