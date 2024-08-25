from django.db import models

from Testproject.models import TestProject
from TestInterface.models import *


# Create your models here.
class TestScent(models.Model):
    """
    定义业务流相关表格模型
    """
    project = models.ForeignKey(TestProject, on_delete=models.PROTECT, help_text='所属项目id',
                                verbose_name='所属项目id')
    name = models.CharField(max_length=50, help_text='任务流名称', verbose_name='任务流名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TestScent'
        verbose_name_plural = '任务流信息表'


class ScenesToCase(models.Model):
    """
    测试任务流中的执行顺序
    """
    icase = models.ForeignKey(IterFaceCase, on_delete=models.PROTECT, verbose_name='接口用例关联id',
                              help_text='接口用例关联id')
    scene = models.ForeignKey(TestScent, on_delete=models.PROTECT, verbose_name='关联的任务流id',
                              help_text='关联的任务流id')
    sort = models.IntegerField(verbose_name='执行顺序', help_text='执行顺序', null=True, blank=True)

    class Meta:
        db_table = 'ScenesToCase'
        verbose_name_plural = '测试业务流执行步骤'

    def __str__(self):
        return self.icase.title
