from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(BugManage)
class BugManageAdmin(admin.ModelAdmin):
    list_display = ['status', 'create_time', 'user']


@admin.register(BugHandle)
class BugHandleAdmin(admin.ModelAdmin):
    list_display = ['create_time', 'handle', 'update_user']
