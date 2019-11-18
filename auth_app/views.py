from django.shortcuts import render
from auth_app.serializers import GLUserSerializer, GLProjectSerializer
from rest_framework.views import APIView
from auth_app.models import GL_User
from rest_framework.response import Response
from rest_framework import permissions
from projects_app.models import GL_Project
from gitlab_manager import loaddata

# Create your views here.
class GL_User_View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        loaddata.loadData(request)
        user = request.user.gl_user
        serializer = GLUserSerializer(user)
        return Response({'data': serializer.data})

class GL_Project_View(APIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request):
        projects = request.user.gl_user.member
        serializer = GLProjectSerializer(projects, many=True)
        return Response({'data': serializer.data})