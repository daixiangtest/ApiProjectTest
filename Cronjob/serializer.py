from .models import *
from rest_framework import serializers


class CronjobSerializer(serializers.ModelSerializer):
    """
    对模型类定时任务表进行序列化
    """
    # 添加自定义的序列化化返回字段
    task_name = serializers.StringRelatedField(read_only=True, source='task.name')
    env_name = serializers.StringRelatedField(read_only=True, source='env.name')

    class Meta:
        model = Cronjob
        fields = '__all__'
