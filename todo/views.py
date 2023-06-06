from django.http import HttpResponse
from todo import serializers
from .models import todo
from django.shortcuts import render
from rest_framework import viewsets,permissions
from django.core import serializers
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [] #permissions.IsAuthenticated

    def create(self, request):   #post ruft automatisch diese Funktion auf
        _todo = todo.objects.create(title= self.request.data.get('title', ''),
                                         description= self.request.data.get('description', ''),
                                         user= request.user,
                                         )
        serialized_obj = serializers.serialize('json', [_todo,])
        return HttpResponse(serialized_obj, content_type='application/json')

