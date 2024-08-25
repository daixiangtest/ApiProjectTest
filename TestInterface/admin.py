from django.contrib import admin

from Scenes.models import ScenesToCase
from .models import *


# Register your models here.
@admin.register(IterFace)
class TestProjectAdmin(admin.ModelAdmin):
    list_display = ['project', 'name', 'url', 'method', 'type']


@admin.register(IterFaceCase)
class InterFaceCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'interface']

