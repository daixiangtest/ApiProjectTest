from django.shortcuts import render
from rest_framework import permissions, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Cronjob.models import Cronjob
from Cronjob.serializer import CronjobSerializer


# Create your views here.
class CronjobView(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    """
    定义定时任务增加，删除，修改，查询列表的视图类
    """
    queryset = Cronjob.objects.all()
    serializer_class = CronjobSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project', 'task']
