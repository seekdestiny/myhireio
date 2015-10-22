from django.contrib import admin

from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = (    
                          'name', 
                          'tag_name', 
                          'product', 
                          'why_us', 
                          'traction', 
                          'funding', 
                          'size',
                          'market', 
                          'company_link', 
                          'last_active'
                   )

    list_filter = ['last_active']
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)
