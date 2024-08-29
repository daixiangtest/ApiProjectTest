from django.db import models

from Scenes.models import TestScent
from Testproject.models import TestProject, TestEnv


# Create your models here.
class TestTask(models.Model):
    """
    测试任务的模块类
    """
    project = models.ForeignKey(TestProject, on_delete=models.PROTECT, help_text='所属项目', verbose_name='所属项目')
    name = models.CharField(max_length=50, verbose_name='任务名称', help_text='任务名称')
    scene = models.ManyToManyField(TestScent, blank=True, help_text='关联的任务流',
                                   verbose_name='关联的任务流')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TestTask'
        verbose_name_plural = '测试任务表'


class TestRecord(models.Model):
    """
    测试运行记录表
    """
    task = models.ForeignKey(TestTask, on_delete=models.CASCADE, help_text='测试任务表', verbose_name='测试任务表')
    env = models.ForeignKey(TestEnv, on_delete=models.PROTECT, help_text='执行环境', verbose_name='执行环境')
    all = models.IntegerField(help_text='用例总数', verbose_name='用例总数', default=0, blank=True)
    success = models.IntegerField(help_text='通过用例数', verbose_name='通过用例数', default=0, blank=True)
    fail = models.IntegerField(verbose_name='失败用例数', help_text='失败用例数', default=0, blank=True)
    error = models.IntegerField(verbose_name='错误用例数', help_text='错误用例数', default=0, blank=True)
    pass_rate = models.CharField(max_length=50, verbose_name='用例通过率', help_text='用例通过率', default="0",
                                 blank=True)
    tester = models.CharField(max_length=50, verbose_name='执行者', help_text='执行者', blank=True)
    status = models.CharField(max_length=50, verbose_name='执行状态', help_text='执行状态')
    create_time = models.DateTimeField(auto_created=True, verbose_name='执行时间', help_text='执行时间')

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'TestRecord'
        verbose_name_plural = '运行记录表'


class TestReport(models.Model):
    """
    测试报告表模型类
    """
    info = models.JSONField(verbose_name='报告的数据', help_text='报告的数据', default=dict, blank=True)
    recode = models.ForeignKey(TestRecord, on_delete=models.CASCADE, verbose_name='测试记录', help_text='测试记录')

    def __str__(self):
        return self.recode.status

    class Meta:
        db_table = 'TestReport'
        verbose_name_plural = '测试报告表'
