from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [

]
route = routers.SimpleRouter()
route.register(r'projects', TestProjectView)
route.register(r'envs', TestEnvView)
route.register(r'files', TestFileView)
urlpatterns += route.urls
