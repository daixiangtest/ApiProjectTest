from ApiTestEngine.core2.cases import run_test
from django.shortcuts import render
from rest_framework import mixins, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Testproject.models import TestEnv
from .models import *
from .serializer import *


# Create your views here.

class TestScensView(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """
    任务流创建，更改，删除，获取任务列表，视图函数实现
    """
    queryset = TestScent.objects.all()
    serializer_class = TestScentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']


class ScenesToCaseView(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
    queryset = ScenesToCase.objects.all()
    serializer_class = ScenesToCaseSerializer
    filterset_fields = ['scene']
    # permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'list':
            return ScenesToCaseListSerializer
        else:
            return self.serializer_class

    def list(self, request, *args, **kwargs):
        """
        对用例执行列表进行排序后返回
        :param request:
        :param args:
        :param kwargs: 
        :return:
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        paginated_data = serializer.data
        sorted_data = sorted(paginated_data, key=lambda x: x['sort'])
        return Response(sorted_data)

    def run_scene(self, request):
        """
        根据测试任务流的执行顺序来运行测试用例
        :param request:
        :return:
        """
        # 获取请求参数
        env_id = request.data.get('env')
        scene_id = request.data.get('scene')
        if not all([env_id, scene_id]):
            return Response({"error": "env与scene字段为必填参数"}, status=status.HTTP_400_BAD_REQUEST)
        env = TestEnv.objects.get(id=env_id)
        scene = TestScent.objects.get(id=scene_id)
        # 根据env参数获取配置参数
        env_config = {
            "ENV": {
                "host": env.host,
                "headers": env.headers,
                **env.global_variable
            },
            "DB": env.db,
            "global_func": env.global_func
        }
        cases = scene.scenestocase_set.all()

        res = SceneCaseReadSerializer(cases, many=True).data

        datas = sorted(res, key=lambda x: x['sort'])
        # cases1 = []
        # for item in datas:
        #     cases1.append(item['icase'])
        # 执行的用例数据
        case_data = [
            {
                "name": scene.name,
                "Cases": [item['icase'] for item in datas]
            }
        ]
        print(len(cases))
        result = run_test(env_config=env_config, case_data=case_data)
        return Response(result[0]['results'][0], status=status.HTTP_200_OK)


class ScenesOrderView(APIView):
    def patch(self, request):
        datas = request.data
        if isinstance(datas, list):
            for item in datas:
                obj = ScenesToCase.objects.get(id=item['id'])
                obj.sort = item['sort']
                obj.save()
            return Response({'data': datas, "message": "成功"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "失败,请求参数不正确,应该为数组", 'data': datas}, status=status.HTTP_200_OK)
