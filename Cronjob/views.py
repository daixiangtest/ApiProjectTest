import json

from django.shortcuts import render
from rest_framework import permissions, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from Cronjob.models import Cronjob
from Cronjob.serializer import CronjobSerializer
from django.db import transaction


# Create your views here.
class CronjobView(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """
    定义定时任务增加，删除，修改，查询列表的视图类
    """
    queryset = Cronjob.objects.all()
    serializer_class = CronjobSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project', 'task']

    # 创建定时任务
    def create(self, request, *args, **kwargs):
        # 操作多张数据表时创建一个事务管理操作
        with transaction.atomic():
            # 创建事务的保存节点
            trans_point = transaction.savepoint()
            try:
                # 调用父类的方法来创建定时数据信息
                result = super().create(request, *args, **kwargs)
                # 获取定时任务的时间配置参数
                rule = result.data['rule']
                crontab = rule.split(' ')
                cron_dict = dict(zip(('minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year'), crontab))
                # 创建数据到django-celery-CrontabSchedule表中配置时间
                print(cron_dict, type(cron_dict))
                try:
                    Cronjob.objects.get(**cron_dict)
                except:
                    cron = CrontabSchedule.objects.create(**cron_dict)
                else:
                    cron = Cronjob.objects.get(**cron_dict)
                # 创建数据到django-celery-PeriodicTask 表中配置执行任务信息
                PeriodicTask.objects.create(
                    name=result.data.get('id'),
                    task='TestTask.tasks.run_task',
                    crontab=cron,
                    kwargs=json.dumps({"env_id": result.data.get('env'),
                                       "task_id": result.data.get('task'),
                                       "username": request.user.username, }),
                    enabled=result.data.get('status'),
                )
            except Exception as e:
                # 出现异常事务回滚
                transaction.savepoint_rollback(trans_point)
                raise e
                # return Response({"message": "创建定时任务异常"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                # 执行完成提交事务
                transaction.savepoint_commit(trans_point)
                return result

    # 更改定时任务信息
    def update(self, request, *args, **kwargs):
        with transaction.atomic():
            trans_point = transaction.savepoint()
            try:
                # 更改定时任务表数据获取需要更改的数据
                result = super().update(request, *args, **kwargs)
                # 更改定时周期任务表
                cron_job = PeriodicTask.objects.get(name=result.data.get('id'))
                print(result.data.get('status'))
                cron_job.enabled = result.data.get('status')
                cron_job.kwargs = json.dumps({"env_id": result.data.get('env'),
                                              "task_id": result.data.get('task'),
                                              "username": request.user.username})
                rule = result.data['rule']
                crontab = rule.split(' ')
                cron_dict = dict(zip(('minute', 'hour', 'day_of_week', 'day_of_month', 'month_of_year'), crontab))
                # 获取定时配置没有则创建
                try:
                    Cronjob.objects.get(**cron_dict)
                except:
                    cron = CrontabSchedule.objects.create(**cron_dict)
                    cron.save()
                else:
                    cron = Cronjob.objects.get(**cron_dict)
                # 更改为新的定时配置
                print(cron)
                cron_job.crontab = cron
                print(cron_job.crontab)
                cron_job.save()

            except Exception as e:
                transaction.savepoint_rollback(trans_point)
                raise e
            else:
                transaction.savepoint_commit(trans_point)
                return result

    # 删除定时任务
    def destroy(self, request, *args, **kwargs):
        with transaction.atomic():
            trans_point = transaction.savepoint()
            try:
                # 删除定时任务配置表
                del_obj = self.get_object()
                # 删除定时周期表数据
                cron_job = PeriodicTask.objects.get(name=del_obj.id)
                cron_job.enabled = False
                cron_job.delete()
            except Exception as e:
                transaction.savepoint_rollback(trans_point)
                raise e
            else:
                transaction.savepoint_commit(trans_point)
                return super().destroy(self, request, *args, **kwargs)
