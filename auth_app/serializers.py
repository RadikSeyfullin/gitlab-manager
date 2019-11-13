from rest_framework import serializers
from auth_app.models import GL_User
from projects_app.models import GL_Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

"""Сериализация проектов"""
class GLProjectSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = GL_Project
        fields = ('pid', 'name', 'description', 'name_with_namespace', 'created_at', 'creator')

"""Сериализация юзера"""
class GLUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    member = GLProjectSerializer(many=True)
    class Meta:
        model = GL_User
        fields = ('uid', 'name', 'user', 'member')