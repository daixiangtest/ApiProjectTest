from django.db import models
from Testproject.models import TestProject


# Create your models here.

class IterFace(models.Model):
    """
    接口信息表模型类
    """
    CHOICES = [('1', '项目接口'), ('2', '外部接口')]
    name = models.CharField(max_length=50, verbose_name='接口名称', help_text='接口名称')
    url = models.CharField(max_length=50, verbose_name='接口地址', help_text='接口地址')
    method = models.CharField(max_length=20, verbose_name='请求方法', help_text='请求方法')
    # 固定模型类的枚举值
    type = models.CharField(max_length=50, verbose_name='接口类型', help_text='接口类型', choices=CHOICES)
    project = models.ForeignKey(TestProject, on_delete=models.CASCADE, help_text='项目id', verbose_name='项目id')

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'interface'
        verbose_name_plural = '接口信息表'


class IterFaceCase(models.Model):
    """
    接口用例管理表
    """
    title = models.CharField(max_length=50, verbose_name='用例名称', help_text='用例名称')
    interface = models.ForeignKey(IterFace, on_delete=models.CASCADE, verbose_name='所属项目id', help_text='所属项目id')
    headers = models.JSONField(verbose_name='请求头信息', help_text='请求头信息', default=dict, null=True, blank=True)
    request = models.JSONField(verbose_name='请求体参数', help_text='请求体参数', default=dict, null=True, blank=True)
    file = models.JSONField(verbose_name='上传文件参数', help_text='上传文件参数', default=dict, null=True, blank=True)
    setup_script = models.TextField(verbose_name='前置执行脚本', help_text='前置执行脚本', default="", null=True,
                                    blank=True)
    teardown_script = models.TextField(verbose_name='后置执行脚本', help_text='后置执行脚本', default="", null=True,
                                       blank=True)

    def __str__(self):
        return self.file

    class Meta:
        db_table = 'IterFaceCase'
        verbose_name_plural = '测试用例执行表'
