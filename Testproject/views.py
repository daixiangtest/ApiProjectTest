import json
import os

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import TestProject, TestFile, TestEnv
from .serializer import *
from rest_framework import permissions, mixins, status
from django_filters import rest_framework as filters
from ApiProjectTest import settings


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
    # 注册过滤器的对象(局部配置)
    # filter_backends = (filters.DjangoFilterBackend,)
    # 添加过滤的字段通过该字段来筛选指定的数据
    filterset_fields = ['project']


class TestFileView(mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    测试文件上传接口
    继承 文化上传，文件查询，文件查询接口

    """
    queryset = TestFile.objects.all()
    serializer_class = TestFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 自定义文件上传 判断文件的大小，重复上传，保存上传文件的基本信息
    def create(self, request, *args, **kwargs):
        size = request.data['file'].size
        name = request.data['file'].name
        type = request.data['file'].content_type
        if size > 1024 * 300:
            return Response({'detail': '文件过大，文件内存不能超过300kb'}, status=status.HTTP_400_BAD_REQUEST)
        if os.path.isfile(settings.MEDIA_ROOT / name):
            return Response({'detail': '文件名重复,不能重复上传'}, status=status.HTTP_400_BAD_REQUEST)
        request.data['info'] = json.dumps([name, 'files/{}'.format(name), type])
        return super().create(request, *args, **kwargs)

    # 自定义删除文件接口，删除数据库时也删除本地文件
    def destroy(self, request, *args, **kwargs):
        file_path = self.get_object().info[1]
        res = super().destroy(request, *args, **kwargs)
        os.remove(file_path)
        return res
