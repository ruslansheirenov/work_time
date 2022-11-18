from django.contrib import admin

from .models import Organization, OrganizationWorkTime, WorkTime



# Register your models here.

admin.site.register(Organization)
admin.site.register(OrganizationWorkTime)
admin.site.register(WorkTime)