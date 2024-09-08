from django.contrib import admin

from Cronjob.models import Cronjob


# Register your models here.
@admin.register(Cronjob)
class CronjobAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rule', 'status']
