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


class TestRecordSerializer(serializers.ModelSerializer):
    """
    定义运行记录表的序列化器
    """
    env = serializers.StringRelatedField(read_only=True)
    # 指定返回关键外键的模型类的__str__方法返回的字符串
    task = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TestRecord
        fields = '__all__'


class TestReportSerializer(serializers.ModelSerializer):
    """
    定义测试报告表序列化器
    """

    class Meta:
        model = TestReport
        fields = '__all__'
