from django.urls import path
from auth_app.views import GL_User_View, GL_Project_View

urlpatterns = [
    path('', GL_User_View.as_view()),
    path('projects/', GL_Project_View.as_view()),
]
