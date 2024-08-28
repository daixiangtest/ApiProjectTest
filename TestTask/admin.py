from django.contrib import admin

from TestTask.models import TestTask


# Register your models here.
@admin.register(TestTask)
class TestTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project']
