from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50, primary_key=True, blank=False)
    tag_name = models.CharField(max_length=100, blank=True)
    product = models.CharField(max_length=1500, default='', blank=False)
    why_us = models.CharField(max_length=1500, blank=True)
    traction = models.CharField(max_length=500, default='', blank=False)
    funding = models.CharField(max_length=500, blank=True)
    size = models.CharField(max_length=20, blank=True, default='2~5')
    last_active = models.DateTimeField()
    market = models.CharField(max_length=100, blank=True)
    company_link = models.CharField(max_length=50, blank=True)

    def serialize(self):
        return {
            'name': unicode(self.name),
            'tag_name': unicode(self.tag_name),
            'product': unicode(self.product),
            'why_us': unicode(self.why_us),
            'traction': unicode(self.traction),
            'funding': unicode(self.funding),
            'size': unicode(self.size),
            'last_active': self.last_active.strftime('%Y-%m-%d'),
            'market': unicode(self.market),
            'company_link': unicode(self.company_link),
        }

class JobPost(models.Model):
    description = models.CharField(max_length=1500, null=False, default='', blank=False)
    requirements = models.CharField(max_length=1500, null=False, default='', blank=False)
    skills = models.CharField(max_length=500, null=False, default='', blank=False)
    location = models.CharField(max_length=100, null=False, default='', blank=False)
    salary = models.CharField(max_length=50, null=False, default='', blank=False)
    equity = models.CharField(max_length=50, null=False, default='', blank=False)
    job_type = models.CharField(max_length=20, null=False, default='', blank=False)
    job_title = models.CharField(max_length=30, null=False, default='', blank=False)
    responsibility = models.CharField(max_length=1000, null=False, default='', blank=False)
    company = models.ForeignKey(Company)

    def serialize(self):
        return {
            'description': unicode(self.description),
            'requirements': unicode(self.requirements),
            'skills': unicode(self.skills),
            'location': unicode(self.location),
            'salary': unicode(self.salary),
            'equity': unicode(self.equity),
            'job_type': unicode(self.job_type),
            'job_title': unicode(self.job_title),
            'responsibility': unicode(self.responsibility),
            'id': unicode(self.id),
        }

