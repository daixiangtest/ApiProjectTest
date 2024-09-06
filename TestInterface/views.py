from ApiTestEngine.core2.cases import run_test
from django.shortcuts import render
from rest_framework import mixins, permissions, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Testproject.models import TestEnv
from .models import *
from .serializer import *


class InterFaceView(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """
    接口信息管理，新增，更改，删除，获取列表信息
    """
    queryset = IterFace.objects.all()
    serializer_class = InterFaceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']

    # 定义接口返回的内容可以重写请求方法，也可以更改序列化器的返回对象
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     #
    #     # page = self.paginate_queryset(queryset)
    #     # if page is not None:
    #     #     serializer = self.get_serializer(page, many=True)
    #     #     return self.get_paginated_response(serializer.data)
    #     # 返回自定义序列化内容
    #     serializer = InterFaceResSerializer(queryset, many=True)
    #     # serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def get_serializer_class(self):
        # 判断方法名是否为list 如果是list更改返回的序列化器
        if self.action == 'list':
            return InterFaceResSerializer
        else:
            return self.serializer_class


class InterFaceCaseView(ModelViewSet):
    """
    接口用例执行管理，新增，更改，删除，获取列表信息，获取用例详情
    """
    queryset = IterFaceCase.objects.all()
    serializer_class = IterFaceCaseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['interface']

    # 自定义获取列表数据，通过序列化器来展示
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     # 返回自定义序列化内容
    #     serializer = IterFaceCaseResSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #  # 自定义返回数据结果，更改序列化器来实现
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = IterFaceCaseGetSerializer(instance)
    #     return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'list':
            return IterFaceCaseResSerializer
        elif self.action == 'retrieve':
            return IterFaceCaseGetSerializer
        else:
            return self.serializer_class

    def run_cases(self, request):
        """
        运行接口测试用例
        :param request: 请求数据
        :return: 响应结果
        """
        # 获取接口的请求参数
        env_id = request.data.get('env')
        cases = request.data.get('cases')
        if not all([env_id, cases]):
            return Response({"error": "env与cases字段为必填参数"}, status=status.HTTP_400_BAD_REQUEST)
        # 获取环境环境变量的值
        env = TestEnv.objects.get(id=env_id)
        # print(cases)
        # 组装请求的配置数据
        env_config = {
            "ENV": {
                "host": env.host,
                "headers": env.headers,
                **env.global_variable,
                **env.debug_global_variable
            },
            "DB": env.db,
            "global_func": env.global_func
        }
        print(env_config)
        # 组装请求的用例请求信息
        cases_data = [
            {
                'name': '调试执行',
                'Cases': [cases]
            }
        ]
        result1, env1 = run_test(env_config=env_config, case_data=cases_data)
        # 保存接口用例的环境变量到调试模式中
        env.debug_global_variable = env1
        env.save()
        return Response(result1['results'][0]['cases'][0], status=status.HTTP_200_OK)
