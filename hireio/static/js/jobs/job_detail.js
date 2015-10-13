_.namespace('hio.jobs.views', function(ns) {
    'use strict';

    ns.JobDetail = hio.base.hio_base_view.extend({
        initialize: function(options) {
            this.job_id = options.job_id;
        },

        render: function(render) {
            var template = _.template($('#tpl_job_detail_wrapper').html());
            this.$el.html(template());
            this.load_job_detail();
        },

        render_job_detail: function(job_detail) {
            var template = _.template($('#tpl_job_detail').html());
            this.$('.job_detail_wrapper').append(template({'job': job_detail}));
        },

        load_job_detail: function() {
            $.ajax({
                url: 'http://127.0.0.1:8000/jobs/job_detail?job_id=' + this.job_id,
                context: this,
                type: 'GET',
                success: function(data) {
                    this.render_job_detail(data);
                },
                error: function() {
                },
                timeout: 3000
            });
        }

    });
});