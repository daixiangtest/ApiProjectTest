from rest_framework.viewsets import ModelViewSet
from .models import TestProject
from .serializer import TestProjectSerializer
from rest_framework import permissions


class TestProjectView(ModelViewSet):
    """
    dango中的drf 框架提供了常规的增删改查方法，只需要继承ModelViewSet类，然后声明模型类对象和对应的序列化器即可
    """
    # 声明数据操作的模型类表
    queryset = TestProject.objects.all()
    # 针对该模型类的序列化器
    serializer_class = TestProjectSerializer
    # 声明该视图类型的访问需要Token 鉴权
    permission_classes = [permissions.IsAuthenticated]
