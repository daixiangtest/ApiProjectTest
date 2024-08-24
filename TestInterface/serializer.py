from .models import *
from rest_framework import serializers


class InterFaceSerializer(serializers.ModelSerializer):
    """
    对模型类接口信息表进行序列化
    """

    class Meta:
        model = IterFace
        fields = '__all__'


class IterFaceCaseSerializer(serializers.ModelSerializer):
    """
    对模型类测试用例表序列化
    """

    class Meta:
        model = IterFaceCase
        fields = '__all__'


class IterFaceCaseResSerializer(serializers.ModelSerializer):
    """
    自定义返回测试用例固定字段
    """

    class Meta:
        model = IterFaceCase
        fields = ('id', 'title')


class IterFaceCaseGetSerializer(serializers.ModelSerializer):
    """
    自定义返回测试用例详情
    """
    interface = IterFaceCaseSerializer()

    class Meta:
        model = IterFaceCase
        fields = "__all__"


class InterFaceResSerializer(serializers.ModelSerializer):
    """
    自定义返回接口信息表进行序列化
    """
    cases = IterFaceCaseResSerializer(many=True, read_only=True, source='interfacecase_set')

    class Meta:
        model = IterFace
        fields = '__all__'
