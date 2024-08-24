from django.shortcuts import render
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # 返回自定义序列化内容
        serializer = InterFaceResSerializer(queryset, many=True)
        return Response(serializer.data)


class InterFaceCaseView(ModelViewSet):
    """
    接口用例执行管理，新增，更改，删除，获取列表信息，获取用例详情
    """
    queryset = IterFaceCase.objects.all()
    serializer_class = IterFaceCaseSerializer
    filterset_fields = ['interface']

    # 自定义获取
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        # 返回自定义序列化内容
        serializer = IterFaceCaseResSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(serializer.data)
