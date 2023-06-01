from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import todo


class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = todo
        fields = ['title', 'description', 'created_at']