from django.db import models


# Create your models here.
class TestProject(models.Model):
    """
    创建测试项目表
    """
    name = models.CharField(max_length=50, verbose_name='项目名称', help_text='项目名称')
    leader = models.CharField(max_length=50, verbose_name='负责人', help_text='负责人')
    create_time = models.TimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TestProject'
        verbose_name = '测试项目表'


class TestEnv(models.Model):
    """
    创建测试环境表
    """
    project = models.ForeignKey(TestProject, on_delete=models.CASCADE, verbose_name='项目名称', help_text='项目名称')
    global_variable = models.JSONField(verbose_name='全局变量', help_text='全局变量', default=dict, null=True,
                                       blank=True)
    debug_global_variable = models.JSONField(verbose_name='调试模式全局变量', help_text='调试模式全局变量',
                                             default=dict, null=True, blank=True)
    db = models.JSONField(verbose_name='数据库配置', help_text='数据库配置', default=dict, null=True, blank=True)
    host = models.CharField(verbose_name='测试环境的host地址', help_text='测试环境的host地址',max_length=50)
    headers = models.JSONField(verbose_name='全局请求头信息', help_text='全局请求头信息', default=dict, null=True,
                               blank=True)
    global_func = models.TextField(verbose_name='全局工具函数', help_text='全局工具函数', default='', null=True,
                                   blank=True)
    name = models.CharField(verbose_name='测试环境名称', help_text='测试环境名称',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'TestEnv'
        verbose_name = '测试环境表'


class TestFile(models.Model):
    """
    创建测试文件表
    """
    file = models.FileField(verbose_name='文件', help_text='文件')
    info = models.JSONField(verbose_name='文件信息', help_text='文件信息', default=list)

    def __str__(self):
        return self.info

    class Meta:
        db_table = 'TestFile'
        verbose_name = '测试文件表'
