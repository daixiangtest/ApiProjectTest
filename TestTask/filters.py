from django_filters.rest_framework import FilterSet
from django_filters import filters

from TestTask.models import TestRecord


class TestRecordFilterSet(FilterSet):
    """
    自定定义过滤器，针对测试执行记录模型类的过滤查询参数
    """
    # project 字段不存在task模型中,在task字段关联的模型中存在，task__project 表示通过task字段关联的project作为过滤字段
    project = filters.NumberFilter(field_name='task__project')

    class Meta:
        model = TestRecord
        # 指定过滤查询参数的字段
        fields = ['task', 'project']
