from django.shortcuts import render
from rest_framework import mixins, permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from BugManage.models import BugManage, BugHandle
from BugManage.serializer import BugManageSerializer, BugManageRetrieveSerializer


# Create your views here.

class BugManageView(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """
    bug 管理的视图类操作
    """

    queryset = BugManage.objects.all()
    serializer_class = BugManageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BugManageRetrieveSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        # 调用父类方法添加请求数据到BugManage表中
        result = super().create(request, *args, **kwargs)
        # 获取操作记录相关字段信息
        bug = BugManage.objects.get(id=result.data.get('id'))
        handle = f"提交bug,提交的bug状态是：{result.data.get('status')}"
        name = request.user.username
        BugHandle.objects.create(bug=bug, handle=handle, update_user=name).save()
        return result

    def update(self, request, *args, **kwargs):
        # 调用父类方法先更新bug关联表数据
        result = super().update(request, *args, **kwargs)
        # 添加一条操作记录
        bug = BugManage.objects.get(id=result.data.get('id'))
        handle = f"修改bug,修改的bug状态是：{result.data.get('status')}"
        name = request.user.username
        BugHandle.objects.create(bug=bug, handle=handle, update_user=name).save()
        return result
