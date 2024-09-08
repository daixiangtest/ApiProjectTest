from django.db import models

from TestTask.models import TestTask
from Testproject.models import TestProject, TestEnv


# Create your models here.
class Cronjob(models.Model):
    """
    定时任务运行表
    """
    project = models.ForeignKey(TestProject, on_delete=models.CASCADE, help_text='关联项目id',
                                verbose_name='关联项目id')
    create_time = models.DateTimeField(auto_created=True, auto_now_add=True, help_text='创建时间',
                                       verbose_name='创建时间')
    name = models.CharField(max_length=100, help_text='任务名称', verbose_name='任务名称')
    task = models.ForeignKey(TestTask, on_delete=models.CASCADE, help_text='关联的测试任务',
                             verbose_name='关联的测试任务')
    rule = models.CharField(max_length=200, default='* * * * *', verbose_name='定时任务的规则',
                            help_text='定时任务的规则')
    status = models.BooleanField(default=False, verbose_name='状态', help_text='状态')
    env = models.ForeignKey(TestEnv, on_delete=models.CASCADE, verbose_name='执行环境', help_text='执行环境')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cronjob'
        verbose_name_plural = '定时任务表'
