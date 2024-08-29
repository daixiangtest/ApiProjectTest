from django.shortcuts import render
from rest_framework import permissions, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .filters import TestRecordFilterSet
from .models import *
from .serializer import *


class TestTaskView(ModelViewSet):
    queryset = TestTask.objects.all()
    serializer_class = TestTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TestTaskGetSerializer
        else:
            return self.serializer_class


class TestRecordView(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = TestRecord.objects.all()
    serializer_class = TestRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    # 添加自定义的过滤器类
    filterset_class = TestRecordFilterSet


class TestReportView(mixins.ListModelMixin, GenericViewSet):
    queryset = TestReport.objects.all()
    serializer_class = TestReportSerializer
    permission_classes = [permissions.IsAuthenticated]
