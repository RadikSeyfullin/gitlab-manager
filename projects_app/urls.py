from django.urls import path
from projects_app.views import GL_Project_View, GL_All_Projects_View

urlpatterns = [
    path('', GL_All_Projects_View.as_view()),
    path('<int:pid>/', GL_Project_View.as_view()),
]