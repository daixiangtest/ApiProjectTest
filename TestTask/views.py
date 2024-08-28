from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *


class TestTaskView(ModelViewSet):
    queryset = TestTask.objects.all()
    serializer_class = TestTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['project']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TestTaskGetSerializer
        else:
            return self.serializer_class
