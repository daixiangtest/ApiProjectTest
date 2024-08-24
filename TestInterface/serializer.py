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
    interface = InterFaceSerializer()

    class Meta:
        model = IterFaceCase
        fields = "__all__"


class InterFaceResSerializer(serializers.ModelSerializer):
    """
    自定义返回接口信息表进行序列化
    """
    # 新增一个序列化器字段 many 展示多条数据，只读，source 指定主键关联的多条数据
    cases = IterFaceCaseResSerializer(many=True, read_only=True, source='iterfacecase_set')

    class Meta:
        model = IterFace
        fields = '__all__'
