from .models import *
from rest_framework import serializers


class TestProjectSerializer(serializers.ModelSerializer):
    """
    对模型类测试项目表进行序列化
    """

    class Meta:
        model = TestProject
        fields = '__all__'


class TestEnvSerializer(serializers.ModelSerializer):
    """
    对模型类测试环境表进行序列化
    """

    class Meta:
        model = TestEnv
        fields = '__all__'


class TestFileSerializer(serializers.ModelSerializer):
    """
    对模型类测试文件表进行序列化
    """

    class Meta:
        model = TestFile
        fields = '__all__'
