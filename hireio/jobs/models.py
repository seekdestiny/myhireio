from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50, blank=False)
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
            'id': str(self.id),
            'name': str(self.name),
            'tag_name': str(self.tag_name),
            'product': str(self.product),
            'why_us': str(self.why_us),
            'traction': str(self.traction),
            'funding': str(self.funding),
            'size': str(self.size),
            'last_active': self.last_active.strftime('%Y-%m-%d'),
            'market': str(self.market),
            'company_link': str(self.company_link),
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
            'description': str(self.description.encode('ascii', 'ignore')),
            'requirements': str(self.requirements),
            'skills': str(self.skills),
            'location': str(self.location),
            'salary': str(self.salary),
            'equity': str(self.equity),
            'job_type': str(self.job_type),
            'job_title': str(self.job_title),
            'responsibility': str(self.responsibility),
            'id': str(self.id),
        }

