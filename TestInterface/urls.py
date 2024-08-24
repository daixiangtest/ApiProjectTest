from rest_framework import routers
from .views import *

urlpatterns = [

]
route = routers.SimpleRouter()
route.register(r'interfaces', InterFaceView)
route.register(r'cases', InterFaceCaseView)

urlpatterns += route.urls
