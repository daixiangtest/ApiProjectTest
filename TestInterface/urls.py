from django.urls import path
from rest_framework import routers
from .views import *

urlpatterns = [
    # 运行单条测试用例
    path('cases/run/', InterFaceCaseView.as_view({"post": "run_cases"}), name='run_cases')
]
route = routers.SimpleRouter()
route.register(r'interfaces', InterFaceView)
route.register(r'cases', InterFaceCaseView)

urlpatterns += route.urls
