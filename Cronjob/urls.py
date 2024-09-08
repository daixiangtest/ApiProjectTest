from rest_framework import routers

from Cronjob.views import CronjobView

urlpatterns = [

]
route = routers.SimpleRouter()
route.register(r'cronjob', CronjobView)
urlpatterns += route.urls
