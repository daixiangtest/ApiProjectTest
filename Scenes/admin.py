from django.contrib import admin

from Scenes.models import TestScent, ScenesToCase


# Register your models here.
@admin.register(TestScent)
class TestScentAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'name']


@admin.register(ScenesToCase)
class SceneToCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'icase', 'scene', 'sort']
