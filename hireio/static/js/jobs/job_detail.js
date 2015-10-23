_.namespace('hio.jobs.views', function(ns) {
    'use strict';

    ns.JobDetail = hio.base.hio_base_view.extend({
        initialize: function(options) {
            this.job_id = options.job_id;
        },

        render: function(render) {
            var template = _.template($('#tpl_job_detail_wrapper').html());
            this.$el.html(template());
        }
    });
});
