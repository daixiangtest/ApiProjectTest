from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework import permissions
from django_filters import rest_framework as filters


class TestProjectView(ModelViewSet):
    """
    dango中的drf 框架提供了常规的增删改查方法，只需要继承ModelViewSet类，然后声明模型类对象和对应的序列化器即可
    测试项目的增删查改
    """
    # 声明数据操作的模型类表
    queryset = TestProject.objects.all()
    # 针对该模型类的序列化器
    serializer_class = TestProjectSerializer
    # 声明该视图类型的访问需要Token 鉴权
    permission_classes = [permissions.IsAuthenticated]


class TestEnvView(ModelViewSet):
    """
    测试环境的接口增删查改
    """
    queryset = TestEnv.objects.all()
    serializer_class = TestEnvSerializer
    permission_classes = [permissions.IsAuthenticated]
    # 注册过滤器的对象
    filter_backends = (filters.DjangoFilterBackend,)
    # 添加过滤的字段通过该字段来筛选指定的数据
    filterset_fields = ['project']
