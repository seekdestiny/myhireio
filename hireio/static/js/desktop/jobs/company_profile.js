_.namespace('hio.jobs.views', function(ns) {
    'use strict';

    ns.CompanyProfile = hio.base.hio_base_view.extend({
        initialize: function(options) {
            this.company_id = options.company_id;
        },

        render: function() {
            var template = _.template($('#tpl_company_profile_wrapper').html());
            this.$el.html(template());
            this._load_company_profile();

            return this;
        },

        _render_company_profile: function(profile) {
            this.profile = profile;
            var template = _.template($('#tpl_company_profile').html());
            this.$('#company_profile_wrapper').append(template({profile: this.profile}));
        },

        _load_company_profile: function() {
            $.ajax({
                url: 'http://127.0.0.1:8000/jobs/load_company_profile',
                context: this,
                type: 'GET',
                data: {
                    company_id: this.company_id
                },
                success: function(data) {
                    this._render_company_profile(data);
                },
                error: function() {
                },
                timeout: 3000
            });
        }
    });

});
