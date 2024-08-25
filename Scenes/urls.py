from django.urls import path
from rest_framework import routers

from Scenes.views import *

urlpatterns = [
    path(r'icases/order/', ScenesOrderView.as_view(), name='updete_icase')
]
route = routers.SimpleRouter()
route.register(r'scenes', TestScensView)
route.register(r'icases', ScenesToCaseView)
urlpatterns += route.urls
