from .models import *
from rest_framework import serializers


class BugHandleSerializer(serializers.ModelSerializer):
    """
    对模型类bug操作记录表进行序列化
    """

    class Meta:
        model = BugHandle
        # 不展示id与bug 字段
        exclude = ['id', 'bug']


class BugManageSerializer(serializers.ModelSerializer):
    """
    对模型类bug管理数据表进行序列化
    """
    interface_url = serializers.StringRelatedField(read_only=True, source='interface.url')

    class Meta:
        model = BugManage
        fields = '__all__'


class BugManageRetrieveSerializer(serializers.ModelSerializer):
    """
    返回bug详情数据，包含bug管理和bug操作记录信息的序列化
    """
    interface_url = serializers.StringRelatedField(read_only=True, source='interface.url')
    handle = BugHandleSerializer(read_only=True, many=True, source='bughandle_set')

    class Meta:
        model = BugManage
        fields = '__all__'
