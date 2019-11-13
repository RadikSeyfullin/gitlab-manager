from auth_app.serializers import GLProjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from projects_app.models import GL_Project

class GL_Project_View(APIView):
    def get(self, request, pid):
        project = GL_Project.objects.get(pid=pid)
        serializer = GLProjectSerializer(project)
        return Response({'data': serializer.data})

class GL_All_Projects_View(APIView):
    def get(self, request):
        projects = GL_Project.objects.all()
        serializer = GLProjectSerializer(projects, many=True)
        return Response({'data': serializer.data})