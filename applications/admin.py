from django.contrib import admin

from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("company","job_title","status","date_applied","user")
    list_filter = ("status","date_applied")
    search_fields = ("company","job_title","notes")