_.namespace('hio.talents', function(ns) {
    'use strict';

    ns.session = new Backbone.Model();
    ns.session.companies = new Backbone.Model();
    ns.global = ns.global || {};
    ns.global.data = ns.global.data || {};

    ns.bootstrap = function(options) {
        var talents_view = {
            Router: null,

            init: function() {
                this.instance = new hio.base.hio_app();
                return this;
            }
        };

        var app = new talents_view.init();

        app.Router = Backbone.Router.extend({
            routes: {
                '': 'talent_list',
                'talent?talent_id=:talent_id': 'talent_profile'
            },

            talent_list: function() {
                var view = new ns.views.TalentList;
                app.instance.goto(view);
            },

            talent_profile: function(talent_id) {
                var view = new ns.views.TalentProfile({ talent_id: talent_id });
                app.instance.goto(view);
            }
        });

        ns.router = new app.Router();
        ns.router.navigate('', {trigger: true});
        Backbone.history.start();
    };
});

