_.namespace('hio.jobs.views', function(ns) {
    'use strict';

    ns.Dashboard = hio.base.hio_base_view.extend({

        events: {
            'click .login.button': 'show_login_form',
            'click .signup.button': 'show_signup_form',
            'click .company_info_wrapper': 'show_company_profile'
        },

        initialize: function() {
            this.index = 0;
        },

        render: function() {
            var template = _.template($('#tpl_dashboard').html());
            this.$el.html(template());
            this.load_more_companies();

            return this;
        },

        render_company_row: function(companies) {
            _.each(companies, function(company) {
                var template = _.template($('#tpl_company_info').html());
                this.$('#company_list').append(template({'company': company}));
            }, this);
        },

        load_more_companies() {
            $.ajax({
                url: 'http://127.0.0.1:8000/jobs/load_more_companies',
                context: this,
                type: 'GET',
                data: {
                    index: 0
                },
                success: function(data) {
                    this.render_company_row(data);
                },
                error: function() {
                },
                timeout: 3000
            });
        },

        show_company_profile: function(e) {
            var id = $(e.currentTarget).data('company-id');
            hio.jobs.router.navigate('company_profile?' + 'company_id=' + id, {trigger: true});
        }
    });
});
