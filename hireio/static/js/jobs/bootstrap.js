_.namespace('hio.jobs', function(ns) {
    'use strict';

    ns.session = new Backbone.Model();
    ns.session.companies = new Backbone.Model();
    ns.global = ns.global || {};
    ns.global.data = ns.global.data || {};

    ns.bootstrap = function(options) {
        var job_view = {
            Router: null,

            init: function() {
                this.instance = new hio.base.hio_app();
                return this;
            }
        };

        var app = new job_view.init();

        app.Router = Backbone.Router.extend({
            routes: {
                '': 'dashboard',
                'job_detail?job_id=:job_id': 'job_detail',
                'company_profile?company_id=:company_id': 'company_profile'
            },

            dashboard: function() {
                var view = new ns.views.Dashboard;
                app.instance.goto(view);
            },

            job_detail: function(job_id) {
                var view = new ns.views.JobDetail({ job_id: job_id });
                app.instance.goto(view);
            },

            company_profile: function(company_id) {
                var view = new ns.views.CompanyProfile({ company_id: company_id });
                app.instance.goto(view);
            }
        });

        ns.router = new app.Router();
        ns.router.navigate('', {trigger: true});
        Backbone.history.start();
    };
});
