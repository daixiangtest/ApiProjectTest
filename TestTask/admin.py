from django.contrib import admin

from TestTask.models import *


# Register your models here.
@admin.register(TestTask)
class TestTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project']


@admin.register(TestRecord)
class TestRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'env', 'pass_rate', 'all']


@admin.register(TestReport)
class TestReportAdmin(admin.ModelAdmin):
    list_display = ['id']
