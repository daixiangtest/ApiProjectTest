from TestInterface.serializer import IterFaceCaseResSerializer
from .models import *
from rest_framework import serializers


class TestScentSerializer(serializers.ModelSerializer):
    """
    对模型类任务流信息表进行序列化
    """

    class Meta:
        model = TestScent
        fields = '__all__'


class ScenesToCaseSerializer(serializers.ModelSerializer):
    """
    测试任务流执行顺序管理序列化
    """

    class Meta:
        model = ScenesToCase
        fields = '__all__'


class ScenesToCaseListSerializer(serializers.ModelSerializer):
    """
    自定义返回任务流执行列表顺序
    """
    icase = IterFaceCaseResSerializer()

    class Meta:
        model = ScenesToCase
        fields = '__all__'


