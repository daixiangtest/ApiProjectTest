from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [

]
route = routers.SimpleRouter()
route.register(r'projects', TestProjectView)
urlpatterns += route.urls