from django.contrib import admin
from .models import *


# 将模型类型数据表注册到Dango的admin项目管理中

@admin.register(TestProject)
class TestProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'leader']


@admin.register(TestEnv)
class TestEnvAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'project', 'host']


@admin.register(TestFile)
class TestFileAdmin(admin.ModelAdmin):
    list_display = ['id', 'file', 'info']
