from django.db import models
from django.contrib.auth.models import User
from projects_app.models import GL_Project

# Create your models here.
class GL_User(models.Model):
    uid = models.IntegerField(verbose_name='GitLab: ID пользователя', primary_key=True)
    name = models.CharField('GitLab: Имя', max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Локальный пользователь')
    p_user = models.CharField('GitLab: ***Parol***', max_length=255)
    member = models.ManyToManyField(GL_Project, verbose_name='GitLab: Проекты', related_name='user_projects')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'GitLab Пользователь'
        verbose_name_plural = 'GitLab Пользователи'

