"""
URL configuration for ApiProjectTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/login/', LoginView.as_view(), name='login'),  # 直接引入实现token登录接口
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新token
    path('api/users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # 校验token
    re_path(r'^api/testPro/', include('Testproject.urls')),
    re_path(r'^api/TestInterFace/', include('TestInterface.urls')),
    re_path(r'^api/testFlow/', include('Scenes.urls')),
    re_path(r'^api/testTask/', include('TestTask.urls')),
    re_path(r'^api/crontab/', include('Cronjob.urls'))

]
