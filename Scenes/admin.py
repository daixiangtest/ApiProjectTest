from django.contrib import admin

from Scenes.models import TestScent, ScenesToCase


# Register your models here.
@admin.register(TestScent)
class TestScentAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name']


# @admin.register(ScenesToCase)
# class SceneToCaseAdmin(admin.ModelAdmin):
#     list_display = ['id', 'icase', 'scene', 'sort']


class SceneToCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'icase', 'scene', 'sort']  # 显示在列表中的字段
    # search_fields = ('name',)  # 搜索字段


admin.site.register(ScenesToCase, SceneToCaseAdmin)
