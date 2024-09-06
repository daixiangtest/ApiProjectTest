from django.urls import path
from rest_framework import routers

from Scenes.views import *

urlpatterns = [
    path(r'icases/order/', ScenesOrderView.as_view(), name='updete_icase'),
    path(r'scenes/run/', ScenesToCaseView.as_view({"post": "run_scene"}), name='run_scene')
]
route = routers.SimpleRouter()
route.register(r'scenes', TestScensView)
route.register(r'icases', ScenesToCaseView)
urlpatterns += route.urls
