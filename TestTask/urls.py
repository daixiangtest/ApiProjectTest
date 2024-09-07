from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [
    path('tasks/run/', TestTaskView.as_view({'post': 'run_task'}))

]
route = routers.SimpleRouter()
route.register(r'tasks', TestTaskView)
route.register(r'records', TestRecordView)
route.register(r'report', TestReportView)
urlpatterns += route.urls
