from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [

]
route = routers.SimpleRouter()
route.register(r'tasks', TestTaskView)
route.register(r'records', TestRecordView)
route.register(r'report', TestReportView)
urlpatterns += route.urls
