from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GL_Project(models.Model):
    pid = models.IntegerField(verbose_name='GitLab: ID проекта', primary_key=True)
    description = models.TextField(verbose_name='GitLab: Описание проекта')
    name = models.CharField(max_length=255, verbose_name='GitLab: Название проекта')
    name_with_namespace = models.CharField(max_length=255, verbose_name='GitLab: Название проекта (полное)')
    created_at = models.DateTimeField(verbose_name='GitLab: Дата создания проекта')
    creator = models.ForeignKey(User, verbose_name='GitLab: Создатель', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'GitLab Проект'
        verbose_name_plural = 'GitLab Проекты'