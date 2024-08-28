from Scenes.serializer import TestScentSerializer
from .models import *
from rest_framework import serializers


class TestTaskSerializer(serializers.ModelSerializer):
    """
    对模型类测试任务表进行序列化
    """

    class Meta:
        model = TestTask
        fields = '__all__'


class TestTaskGetSerializer(serializers.ModelSerializer):
    """
    定义返回任务详情的序列化器返回内容增加scene 关联内容
    """
    scene = TestScentSerializer(many=True)

    class Meta:
        model = TestTask
        fields = '__all__'
