from django.shortcuts import render
from rest_framework import mixins, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
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

    # permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.action == 'list':
            return ScenesToCaseListSerializer
        else:
            return self.serializer_class


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
