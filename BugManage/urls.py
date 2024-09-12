from rest_framework import routers
from BugManage.views import BugManageView

urlpatterns = [

]
route = routers.SimpleRouter()
route.register(r'bugs', BugManageView)
urlpatterns += route.urls
