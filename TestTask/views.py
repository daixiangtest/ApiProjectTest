from ApiTestEngine.core2.cases import run_test
from django.shortcuts import render
from rest_framework import permissions, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Scenes.serializer import SceneCaseReadSerializer
from .filters import TestRecordFilterSet
from .models import *
from .serializer import *


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
        if not all([env_id, task_id]):
            return Response({"error": "env与cases字段为必填参数"}, status=status.HTTP_400_BAD_REQUEST)
        # 获取测试环境数据
        env = TestEnv.objects.get(id=env_id)
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
        # 获取测试任务的执行数据进行组装
        task = TestTask.objects.get(id=task_id)
        # 获取任务中的任务流信息
        scenes = task.scene.all()
        case_data = []
        for scene in scenes:
            # 通过任务流来获取测试的任务执行用例
            cases = scene.scenestocase_set.all()
            # 对执行用例的数据对象进行序列化
            res = SceneCaseReadSerializer(cases, many=True).data
            # 对执行用例的数据进行排序
            datas = sorted(res, key=lambda x: x['sort'])
            # 添加任务到执行顺序中
            case_data.append({
                "name": scene.name,
                "Cases": [item['icase'] for item in datas]
            })
        # 运行测试前创建一个运行记录
        record = TestRecord.objects.create(task=task, env=env, tester=request.user.username, status='执行中')
        # 运行测试任务
        result = run_test(env_config=env_config, case_data=case_data)[0]
        # 更新测试报告

        record.all = result['all']
        record.success = result['success']
        record.fail = result['fail']
        record.error = result['error']
        record.pass_rate = '{:.2f}'.format(result['success'] / result['all'])
        record.status = '执行结束'
        record.save()
        # 保存测试报告
        TestReport.objects.create(info=result, recode=record).save()
        # 返回测试执行结果
        return Response(result, status=status.HTTP_200_OK)


class TestRecordView(mixins.ListModelMixin,
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
        record = TestRecord.objects.get(id=kwargs['pk'])
        report = TestReport.objects.get(recode=record)
        serializer = self.get_serializer(report)
        return Response(serializer.data)
