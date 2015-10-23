_.namespace('hio.jobs.views', function(ns) {
    'use strict';

    ns.CompanyProfile = hio.base.hio_base_view.extend({
        events: {
            'click .company_profile_open_positions_position_table .table_row:not(:first)': 'show_job_detail'
        },

        initialize: function(options) {
            this.company_id = options.company_id;
        },

        render: function() {
            var template = _.template($('#tpl_company_profile_wrapper').html());
            this.$el.html(template());
            this._load_company_profile();

            return this;
        },

        _render_company_profile: function(response) {
            hio.jobs.global.data.company = response.company;
            hio.jobs.global.data.jobs = response.jobs;
            var template = _.template($('#tpl_company_profile').html());
            this.$('#company_profile_wrapper').append(template({
                company: response.company,
                jobs: response.jobs
            }));
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
        },

        show_job_detail: function(event) {
            var id = $(event.currentTarget).find('.position_id_column').text();
            debugger;
            hio.jobs.router.navigate('job_detail?' + 'job_id=' + id, {trigger: true});
        }
    });

});
