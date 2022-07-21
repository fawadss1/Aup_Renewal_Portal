from django.contrib import admin
from . import models
from django.contrib.admin.models import LogEntry

admin.site.site_header = "Welcome to AUP Renewal Panel"
admin.site.site_title = "AUP Admin Panel"
admin.site.index_title = "AUP Admin"

admin.site.register(models.ValidUptoDate)
admin.site.register(models.Semester)
admin.site.register(models.Department)
admin.site.register(models.Student)
LogEntry.objects.all().delete()
