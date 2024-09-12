from django.db import models

from TestInterface.models import IterFace


# Create your models here.
class BugManage(models.Model):
    """
    bug信息管理表格数据模型
    """
    interface = models.ForeignKey(IterFace, on_delete=models.CASCADE, help_text='关联用例', verbose_name='关联用例')
    create_time = models.DateTimeField(auto_now_add=True, help_text="提交时间", verbose_name="提交时间")
    status = models.CharField(max_length=10, help_text='bug的状态', verbose_name='bug的状态')
    user = models.CharField(max_length=20, help_text='提交者', verbose_name='提交者', blank=True, null=True)
    info = models.JSONField(help_text="用例执行信息", verbose_name='用例执行信息', default=dict, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        db_table = 'BugManage'
        verbose_name_plural = 'bug管理表'


class BugHandle(models.Model):
    """
    bug 操作记录表数据模型
    """

    create_time = models.DateTimeField(auto_now_add=True, help_text="操作时间", verbose_name="操作时间")
    bug = models.ForeignKey(BugManage, on_delete=models.CASCADE, help_text='关联的bug', verbose_name='关联的bug')
    handle = models.TextField(help_text='处理操作', verbose_name='处理操作', blank=True, null=True)
    update_user = models.CharField(max_length=20, help_text='操作人', verbose_name='操作人', blank=True, null=True)

    def __str__(self):
        return self.update_user

    class Meta:
        db_table = 'BugHandle'
        verbose_name_plural = 'bug记录表'
