from ApiTestEngine.core2.cases import run_test
from celery.result import AsyncResult
from django.shortcuts import render
from rest_framework import permissions, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from TestTask.tasks import run_task, run_demo
from Scenes.serializer import SceneCaseReadSerializer
from .filters import TestRecordFilterSet
from .models import *
from .serializer import *
from ApiProjectTest.celery import celery_app


class TestTaskView(ModelViewSet):
    """
    测试任务信息的增删查改
    """
    queryset = TestTask.objects.all()
    serializer_class = TestTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TestTaskGetSerializer
        else:
            return self.serializer_class

    def run_task(self, request):
        """
        运行测试执行任务
        :param request: 请求参数对象
        :return: 运行结果
        """

        # 获取请求参数并进行校验
        env_id = request.data.get('env')
        task_id = request.data.get('task')
        name = request.user.username
        if not all([env_id, task_id]):
            return Response({"error": "env与cases字段为必填参数"}, status=status.HTTP_400_BAD_REQUEST)
        # celery 异步执行 测试任务
        res = run_task.delay(env_id, task_id, name)
        # async_result = AsyncResult(id=res.id, app=celery_app)
        # print(async_result.status)
        # 返回测试执行结果
        return Response({"message": '执行中', "task_id": res.id}, status=status.HTTP_200_OK)


class TestRecordView(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    """
    测试执行记录的查询
    """
    queryset = TestRecord.objects.all().order_by('-create_time')
    serializer_class = TestRecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    # 添加自定义的过滤器类
    filterset_class = TestRecordFilterSet


class TestReportView(mixins.RetrieveModelMixin, GenericViewSet):
    """
    测试报告详情查询
    """

    queryset = TestReport.objects.all()
    serializer_class = TestReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    # 自定义通过测试执行记录的id来查询对应的测试报告
    def retrieve(self, request, *args, **kwargs):
        print(kwargs['pk'])
        try:
            record = TestRecord.objects.get(id=kwargs['pk'])
            report = TestReport.objects.get(recode=record)
            serializer = self.get_serializer(report)
            return Response(serializer.data)
        except Exception:
            return Response({"code":"error","msg":"查询报告失败未查询到该测试报告"},status=status.HTTP_400_BAD_REQUEST)