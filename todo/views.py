from .models import todo
from django.shortcuts import render
from rest_framework import viewsets,permissions

from todo.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] #permissions.IsAuthenticated
